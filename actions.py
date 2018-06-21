import pprint

from rasa_core.actions import Action
from rasa_core.domain import TemplateDomain
from rasa_core.events import SlotSet
from rasa_core.trackers import DialogueStateTracker

import moviedb


def extract_non_empty_slots(tracker: DialogueStateTracker):
    """
    Returns all slots that are not empty
    """
    slots = tracker.current_slot_values()
    return {x: i for x, i in slots.items() if i is not None}


class ActionSearchPerson(Action):
    def name(self):
        return 'action_search_person'

    def run(self, dispatcher, tracker: DialogueStateTracker, domain: TemplateDomain):

        slots = extract_non_empty_slots(tracker)
        latest_intent = tracker.latest_message.intent

        if "director" in latest_intent:
            column = "director"
        else:
            column = "actors"

        data = moviedb.search_person(slots, column=column) # returns something of the shape [rows x columns]
        data = [dr[0] for dr in data] # extract the only value of each row

        if column == "director":
            matches = set(data)  # just the name of the directors

        else:
            matches = []            
            for rw in data: # this can be made nicer
                matches += rw.split("|")

        return [SlotSet("matches", matches)]


class ActionSearchPersonInfo(Action):
    def name(self):
        return 'action_search_person_info'

    def run(self, dispatcher, tracker: DialogueStateTracker, domain: TemplateDomain):
        dispatcher.utter_message("doing")
        latest_intent = tracker.latest_message.intent
        dispatcher.utter_message("----- " + str(latest_intent))
        # restaurants = restaurant_api.search(tracker.get_slot("cuisine"))
        return [SlotSet("matches", "dummy ActionSearchPersonInfo data")]


class ActionSearchMovie(Action):
    def name(self):
        return 'action_search_movie'

    def run(self, dispatcher, tracker: DialogueStateTracker, domain: TemplateDomain):
        dispatcher.utter_message("doing")
        latest_intent = tracker.latest_message.intent
        dispatcher.utter_message("----- " + str(latest_intent))
        # restaurants = restaurant_api.search(tracker.get_slot("cuisine"))
        return [SlotSet("matches", "dummy ActionSearchMovie data")]


class ActionSearchMovieInfo(Action):
    def name(self):
        return 'action_search_movie_info'

    def run(self, dispatcher, tracker: DialogueStateTracker, domain: TemplateDomain):
        dispatcher.utter_message("doing")
        latest_intent = tracker.latest_message.intent
        dispatcher.utter_message("----- " + str(latest_intent))
        # restaurants = restaurant_api.search(tracker.get_slot("cuisine"))
        return [SlotSet("matches", "dummy ActionSearchMovieInfo data")]


class ActionAnswer(Action):
    def name(self):
        return 'action_answer'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("here's what I found:")
        dispatcher.utter_message(tracker.get_slot("matches"))
        dispatcher.utter_message("is it ok for you? "
                                 "hint: I'm not going to "
                                 "find anything else :)")
        return []
