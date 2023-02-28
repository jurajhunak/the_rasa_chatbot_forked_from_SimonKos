from typing import Any, Text, Dict, List, Tuple
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
import re
from rasa_sdk.forms import FormValidationAction


BACK_BOOL = True
MOT_BOOL = True
EXP_BOOL = True


class EmailValidationForm(FormValidationAction):
    
    def name(self) -> Text:
        return "validate_email_form"

    def validate_email(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """
        Check if the email is in the correct format using a regular expression.
        """
        if not re.match(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]", slot_value):
            dispatcher.utter_message(text=f"Sorry, the email {slot_value} is not in correct format. Please enter a valid email.")
            return {"email": None}
        else:
            dispatcher.utter_message(text="OK. The email seems good to me.")
            return {"email": slot_value}


class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_hello_world"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="Hello World!")

         return []
     

class ActionBackground(Action):
    def name(self) -> Text:
         return "action_background"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
        background = []

        global BACK_BOOL, MOT_BOOL, EXP_BOOL
         
        
        if BACK_BOOL == True:
            dispatcher.utter_message(text="I have quite diverse background, including 3 years part-time experience of UI/UX testing for a web-based e-learning app in 2010 - 2013." )
            dispatcher.utter_message(text="I also studied architecture while working part-time as a graphic designer and an author for lifestyle magazines writing about design.")
            dispatcher.utter_message(text="In 2016 I joined a platform for independent architects and professionals called collcoll.cc")
            dispatcher.utter_message(text="From 2020 to 2022 I have worked as a versatile architectural designer, project manager and consultant in architecture.")
            dispatcher.utter_message(text="Recent advancements in AI and in the creative industry have inspired me to pursue career in data science")
            dispatcher.utter_message(text="I have recently finished 6 months training in Data Science with Software Development Academy.")
            dispatcher.utter_message(text="In 240 hours of training I explored Python, EDA, MLA, CV, NLP, etc.")
            BACK_BOOL = False
        else:
            dispatcher.utter_message(text="As I said before. My background is diverse and I carry working experience in UI/UX, architecture, management. I also finished a course in Data Science.")
         
        return []
     

class ActionMotivation(Action):

     def name(self) -> Text:
         return "action_motivation"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
         global BACK_BOOL, MOT_BOOL, EXP_BOOL
         
         motivation = ["My main motivation to work in Data Science is that I believe it is promising to be stable and inspiring field of work.","I am curently motivated in a team that explores Data and the use of Data in developing successful solutions.","I see my role in the team as a very open minded analyst and strategist with wide scope of insight.","My former experience in UI/UX and in architecte gives me deep insight into how information emerges and lives in the real worl, physical and virtual.","My dream job is in a team that is oriented on making positive impact on environmental and social issues of today and future."]
         
         if MOT_BOOL == True:
            for i in motivation:
                dispatcher.utter_message(text= i )
            MOT_BOOL = False
         else:
           dispatcher.utter_message(text="To sum it up, my main motivation is a stable, promising and inspiring work, with positive impact in the world.")
         
         return []
     
class ActionExpectation(Action):

     def name(self) -> Text:
         return "action_expectation"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
         global BACK_BOOL, MOT_BOOL, EXP_BOOL
         
         expectation = ["I am looking for a job that offers prospect of learning, career growth and flexibility.",
          "I am advocating for a 4 days workweek and for now I would prefer working in office and meeting people personally"
          ]
         

         if EXP_BOOL == True:
            for i in expectation:
                dispatcher.utter_message(text= i )
            EXP_BOOL = False
     
         else:
            dispatcher.utter_message(text="Again, my main expecation is prospect of learning, career growth and future flexibility.")
         
         return []
     





# hope it works