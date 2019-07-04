from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk import Action, Tracker
from rasa_sdk.forms import FormAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import uuid
from app import db, User


class ActionCustomizePizza(Action):

    def name(self):
        return "action_customize_pizza"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message('cool, select the option you want to change')
        dispatcher.utter_template('utter_customize_option', tracker)
        return []


class ActionAddMorePizza(Action):

    def name(self):
        return "action_add_more_pizza"

    def run(self, dispatcher, tracker, domain):
        add_pizza = (tracker.latest_message)['text']
        if add_pizza == 'yes':
            dispatcher.utter_template('utter_main_pizza_type', tracker)
        elif add_pizza == 'No':
            dispatcher.utter_message('Got it. Let me just take your info.')
        return []


class CustomerForm(FormAction):
    def name(self):
        """Unique identifier of the form"""
        return "customer_form"

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Text, Dict, List[Text, Dict]]]
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where the first match will be picked"""

        return {
            'customer_name': [
                self.from_entity(entity='customer_name',
                                 intent='customer_details'),
                self.from_text(),
            ],
            'customer_number': [
                self.from_entity(entity='customer_number',
                                 intent='customer_details'),
                self.from_text(),
            ],
            'customer_address': [
                self.from_entity(entity='customer_address',
                                 intent='customer_details'),
                self.from_text(),
            ],
            'delivery_time': [
                self.from_entity(entity='delivery_time'),
                self.from_text(),
            ],
        }

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["customer_name", "customer_address", "customer_number", "delivery_time"]

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        dispatcher.utter_template("utter_placed_order", tracker)
        dispatcher.utter_message(
            '----- PIZZA DETAILS -----\n' +
            'TYPE   : {} ,\nSUB TYPE    : {} ,\nEXTRA CUSTOMIZE : {} ,\nSIZE    : {} ,\nTIME    : {}'.format(
                tracker.get_slot("pizza_type"),
                tracker.get_slot("pizza_sub_type"),
                tracker.get_slot("customize_details"),
                tracker.get_slot("pizza_size"),
                tracker.get_slot("delivery_time")
            )
        )

        dispatcher.utter_message(
            '----- CUSTOMER DETAILS -----\n' +
            'Name   : {},\nNumber   : {},\nAddress   : {}'.format(
                tracker.get_slot("customer_name"),
                tracker.get_slot("customer_number"),
                tracker.get_slot("customer_address")
            )
        )

        # store user details in database
        db.session.add(User(
            tracker.get_slot("customer_name"),
            tracker.get_slot("customer_address"),
            tracker.get_slot("customer_number"),
            tracker.get_slot("pizza_type"),
            tracker.get_slot("pizza_sub_type"),
            tracker.get_slot("customize_details"),
            tracker.get_slot("pizza_size"),
            tracker.get_slot("delivery_time")))
        db.session.commit()
        return []
