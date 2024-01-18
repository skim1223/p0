# Sue Kim's GroupMe Bot

## Features of my bot:
- Responds to me: hello message
  - With the message "hello bot", my bot will only respond to me as the sender with the message "sup".
  - I achieved this through retrieving my sender_id and making a conditional statement, where my sender_id is compared in equality to the message object's sender_id. 
 - Responds to others: good morning/good night message
   - With the message "good morning" or "good night" my bot will respond to any sender with "good morning [sender's name]" or "good night [sender's name]".
   - To prevent my bot from resonding to itself and other bots, I made a conditional statement, to check if the message object's sender_type was a bot.
   - If the sender_type was not a bot, I then retireved the message object's name to respond to the sender with their name.
- Tell's jokes:
  - I made use of the following API: [Joke's API](https://official-joke-api.appspot.com/random_joke).
  - With the message "tell me a joke" from a non bot, my bot will send a message with setup line and then 5 seconds later send an additional message with a punchline.
    - The setup and punchline messages are retrieved through a json object that the api provides.

## How to run my bot:
1. I registered my bot through using cURL in the command line (where token123 was replaced with my respective access token):
```bash
curl -X POST -d '{"bot": { "name": "Sue P0, "group_id": "98324520"}}' - 'Content-Type: application/json' https://api.groupme.com/v3/bots?token=token123
```
2. I then activated the virtual environment and ran the bot
```bash
# activate virtual environment
source venv/bin/activate # for mac/linux
venv\Scripts\activate # for windows

# run bot
python3 bot.py
```
3. Done! After this, my bot can begin to respond to new messages with the features mentioned above.
  
