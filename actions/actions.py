from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict, TrackerState


class ValidateReservationForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_reservation_form"

    def validate_time(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `time value."""
        print(slot_value)
        hour = int(slot_value[11:13])
        min = int(slot_value[14:16])
        
        #print(hour)
        if(hour < 23 and hour >= 12):
            if(min <= 15 and min > 0):
                final_time = str(hour-12) + ":" + "15pm"
            elif(min <= 30 and min > 15):
                final_time = str(hour-12) + ":" + "30pm"
            elif(min <= 45 and min > 30):
                final_time = str(hour-12) + ":" + "45pm"
            elif(min < 60  and min > 45):
                final_time = str(hour+1-12) + "pm"
            else:
                final_time = str(hour-12) + "pm"
            #print(final_time)
            return {"time": final_time}
        elif(hour < 12 and hour >= 6):
            if(min <= 15 and min > 0):
                final_time = str(hour) + ":" + "15am"
            elif(min <= 30 and min > 15):
                final_time = str(hour) + ":" + "30am"
            elif(min <= 45 and min > 30):
                final_time = str(hour) + ":" + "45am"
            elif(min < 60  and min > 45):
                if(hour == 11):
                    final_time = str(hour+1) + "pm"
                else:
                    final_time = str(hour+1) + "pm"
            else:
                final_time = str(hour) + "am"
            #print(final_time)
            return {"time": final_time}
        else:
            dispatcher.utter_message(text=f"We are not open at that time. We are only open from 7pm to 10pm")
            return {"time": None}