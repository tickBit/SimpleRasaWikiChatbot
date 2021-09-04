# Simple Rasa Wiki Chatbot

## Python version you need:
- 3.6, 3.7 or 3.8

## Python modules you'll need:
- rasa: pip3 install -U rasa
- wikipedia: pip install wikipedia


## Steps to run the app:

- rasa train
- rasa run actions
- [another terminal]
- rasa shell

## Other info

For some reason, the wikipedia module loads summary of geology if it is asked to fetch information on biology, but if you try it with "biological", you'll get info on biology. Also, the wikipedia module doesn't seem to find summary with "theology", but it finds summary of theology with "teology".

## Last words

I'm just a beginner with Rasa. Particularly the stories part of this Rasa app could be improved. 
