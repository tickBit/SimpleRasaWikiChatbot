from typing import Any, Dict, List, Text
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.interfaces import Action, Tracker

import wikipedia

class ActionFetchData(Action):

    def name(self) -> Text:
        return "action_fetch_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            sci = tracker.latest_message['entities'][0]["value"]
            dispatcher.utter_message("Field of science recognized. Trying to fetch info on it.")
            try:
                info = wikipedia.summary(sci, sentences = 2)
                #info = wikipedia.suggest(sci, senteces = 2)
                #info = wikipedia.page(title=None, pageid=None, auto_suggest=True, redirect=True, preload=False)
                dispatcher.utter_message(text=info)
            except:
                pass
                
        except:
            pass
            
        
        return []
