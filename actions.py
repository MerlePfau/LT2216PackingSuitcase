from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet
from rasa_core_sdk.events import Restarted
import random

vocabulary = ["shoes",
              "sunglasses",
              "shirts",
              "jackets",
              "socks",
              "pajamas",
              "speakers",
              "toothpaste",
              "tissues",
              "multivitamins",
              "eye drops",
              "a toothbrush",
              "a book",
              "a phone charger",
              "shampoo",
              "pants",
              "snacks",
              "water",
              "headphones"
              ]

affirmations = ["Correct! ",
               "Well done! ",
               "Good job! ",
               "That's right. ",
               "That's correct. ",
               "Yes. ",
               "Ok. ",
               "You're right. ",
               "You're correct. ",
               "Ok, let's see. ",
                ""
               ]


class ActionSetUpGame(Action):    
    
    def name(self) -> Text:
        return "action_setup_game"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        used_words = []
        
        possible_words = list(vocabulary)
        
        word_choice_index = random.choice(range(len(possible_words)))
        word_choice = possible_words[word_choice_index]
        
        possible_words.remove(word_choice)
          
        used_words.append(word_choice)
        
        output = "I'm packing a suitcase and I'm bringing " + word_choice + "."

        dispatcher.utter_message(text=output)

        return [SlotSet("used_words", used_words), SlotSet("possible_words", possible_words)]

    
class ActionPlay(Action):

    def name(self) -> Text:
        return "action_play"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        possible_words = tracker.get_slot("possible_words")
        used_words = tracker.get_slot("used_words")
        
        if len(possible_words) == 0:
            dispatcher.utter_message(text="Sorry, I don't know any other words. This means you beat me! Congratulations :) Do you want to start over?")
            return [SlotSet("used_words", None), SlotSet("possible_words", None)]
        
        user_input = tracker.get_slot("user_words")
        
        user_list = user_input.split("bringing ")
        
        user_string = str(user_list[1])
        user_string_comp = user_string
        
        position_comp = 0
        
        # tests if user is missing a word or saying them in the wrong order
        for i in range(len(used_words)):
            if str(used_words[i]) in user_string:
                current_word = used_words[i]
                user_string = user_string.replace(current_word, "")
                position = user_string_comp.index(current_word)
                if position < position_comp:
                    message = "You said " + current_word + " in the wrong position. You lost. Do you want to start over?"
                    dispatcher.utter_message(text=message)
                
                    return [SlotSet("used_words", None), SlotSet("possible_words", None)]
                position_comp = position
        
            else:
                message = "You did not say " + used_words[i] + ". You lost. Do you want to start over?"
                dispatcher.utter_message(text=message)
                
                return [SlotSet("used_words", None), SlotSet("possible_words", None)]
                
        if "." in user_string:
            user_string = user_string.replace(".", "")
        
        if "," in user_string:
            user_string = user_string.replace(",", "")  
            
        user_string_l = user_string.split("and ") 
        
        # tests if user is saying additional words        
        for i in range(len(user_string_l)-1):
            additional_words = user_string_l[i].strip(' ')
            if additional_words:
                message = "You said " + additional_words + ". That's wrong. You lost. Do you want to start over?"
                dispatcher.utter_message(text=message)
            
                return [SlotSet("used_words", None), SlotSet("possible_words", None)]
    
        added_word = user_string_l[len(user_string_l)-1].strip(' ')
        
        if added_word in possible_words:
            possible_words.remove(added_word)
        
        # tests if user is adding already used word
        if not added_word:
            message = "You either did not add a new object or said something we already used! You lost. Do you want to start over?"
            dispatcher.utter_message(text=message)
            
            return [SlotSet("used_words", None), SlotSet("possible_words", None)]
        else: 
            # accept user input
            used_words.append(added_word)
        
        word_choice_index = random.choice(range(len(possible_words)))
        word_choice = possible_words[word_choice_index]   
        
        possible_words.remove(word_choice)
        
        affirm_index = random.choice(range(len(affirmations)))
        affirm = affirmations[affirm_index]
        
        output = affirm + "I'm packing a suitcase and I'm bringing "    
        
        for word in used_words:    
            output += word
            output += ", "
        output += "and " + word_choice + "."

        dispatcher.utter_message(text=output)
                                 
        used_words.append(word_choice)

        return [SlotSet("used_words", used_words), SlotSet("possible_words", possible_words)]
    
    
class ActionRestarted(Action):
    """ This is for restarting the game """

    def name(self):
        return "action_restart"

    def run(self, dispatcher, tracker, domain):
        
        dispatcher.utter_message(text="Let's start over.")
        
        return [Restarted()]


class ActionExtractInput(Action):
    def name(self):
        return "action_extract_input"

    def run(self, dispatcher, tracker, domain):
 
        message = tracker.latest_message.get('text')
        return [SlotSet('user_words', message)]