import requests
import time
import json
import os
from dotenv import load_dotenv

load_dotenv()

BOT_ID = os.getenv("BOT_ID")
GROUP_ID = os.getenv("GROUP_ID")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
LAST_MESSAGE_ID = None


def send_message(text, attachments=None):
    """Send a message to the group using the bot."""
    post_url = "https://api.groupme.com/v3/bots/post"
    data = {"bot_id": BOT_ID, "text": text, "attachments": attachments or []}
    response = requests.post(post_url, json=data)
    return response.status_code == 202


def get_group_messages(since_id=None):
    """Retrieve recent messages from the group."""
    params = {"token": ACCESS_TOKEN}
    if since_id:
        params["since_id"] = since_id

    get_url = f"https://api.groupme.com/v3/groups/{GROUP_ID}/messages"
    response = requests.get(get_url, params=params)
    if response.status_code == 200:
        # this shows how to use the .get() method to get specifically the messages but there is more you can do (hint: sample.json)
        return response.json().get("response", {}).get("messages", [])
    return []

def process_message(message):
    """Process and respond to a message."""
    global LAST_MESSAGE_ID
    text = message["text"].lower()

    # i.e. responding to a specific message (note that this checks if "hello bot" is anywhere in the message, not just the beginning)
    if "hello bot" in text:
        if message["sender_id"] == "49203588":    
            send_message("sup")

    if "good morning" in text:
        if message["sender_type"] != "bot":
            send_message("good morning, " + message["name"])

    if "good night" in text:
        if message["sender_type"] != "bot":
            send_message("good night, " + message["name"])
    
    if "tell me a joke" in text:
        if message["sender_type"] != "bot":
            response = requests.get('https://official-joke-api.appspot.com/random_joke')
            send_message(response.json()['setup'])
            time.sleep(5)
            send_message(response.json()['punchline'])

    LAST_MESSAGE_ID = message["id"]


def main():
    global LAST_MESSAGE_ID
    # this is an infinite loop that will try to read (potentially) new messages every 10 seconds, but you can change this to run only once or whatever you want
    messages = get_group_messages(LAST_MESSAGE_ID)
    for message in reversed(messages):
            LAST_MESSAGE_ID = message["id"]

    while True:
        messages = get_group_messages(LAST_MESSAGE_ID)
        for message in reversed(messages):
            process_message(message)


if __name__ == "__main__":
    main()
