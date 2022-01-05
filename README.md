# Simple Rasa Wiki Chatbot

## Python version you need:
- 3.6, 3.7 or 3.8

## Python modules you'll need:
- Rasa: pip3 install rasa==2.8.19
  (Create a virtual Python environment, if you have later Rasa installed and you want to use the same version as I.
   Probably works with Rasa 3.x, too.)

- wikipedia-api: pip install wikipedia-api


## Steps to run the app:

- rasa train
- rasa run actions
- [another terminal]
- rasa shell

## Example with the bot

- You: tell me about mathematics
- Bot: ~~ shows info about mathematics from Wikipedia

## Other info

My first version used the Wikipedia module, but I got "time out error" from Rasa with it while doing this version.
That's why I switched to wikipediaapi module.
