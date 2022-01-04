from typing import Any, Dict, List, Text
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.interfaces import Action, Tracker

import wikipediaapi

class ActionFetchData(Action):

    def name(self) -> Text:
        return "action_fetch_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            sci = tracker.latest_message["entities"][0]["value"]
            dispatcher.utter_message("Trying to retrieve info on "+sci)

            wiki_wiki = wikipediaapi.Wikipedia('en')
            try:
                page_py = wiki_wiki.page(sci)

                sentences = page_py.summary.split(".")

                # get 4 sentences of the summary
                text = ".".join(sentences[:4]) + "."

                dispatcher.utter_message(text=text)
            except:
                dispatcher.utter_message("Sorry, I couldn't find Wikipedia page on "+sci)
                pass
                
        except:
            pass
            
        
        return []
    
    
        