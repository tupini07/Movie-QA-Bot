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


def _wrap_answer_commas_and(answrs):
    answrs = list(answrs)
    if len(answrs) > 1:
        res = ""
        for an in answrs[:-1]:
            res += f"{an.strip()}, "
        return f"{res.strip()} and {answrs[-1].strip()}"

    elif len(answrs) == 1:
        return f"{answrs[0].strip()}"

    else:
        return ""


class ActionSearchPerson(Action):
    def name(self):
        return 'action_search_person'

    def run(self, dispatcher, tracker: DialogueStateTracker, domain: TemplateDomain):

        slots = extract_non_empty_slots(tracker)
        latest_intent = tracker.latest_message.intent["name"]

        if "director" in latest_intent:
            column = "director"
        else:
            column = "actors"

        # returns something of the shape [rows x columns]
        data = moviedb.make_search_on_slots(slots, column=column)
        data = [dr[0] for dr in data]  # extract the only value of each row

        if column == "director":
            # just the name of the directors
            matches = _wrap_answer_commas_and(set(data))

        else:
            matches = []
            for rw in data:  # this can be made nicer
                matches += rw.split("|") if rw else ""
            matches = _wrap_answer_commas_and(matches)

        return [SlotSet("matches", matches)]


class ActionSearchPersonInfo(Action):
    def name(self):
        return 'action_search_person_info'

    def run(self, dispatcher, tracker: DialogueStateTracker, domain: TemplateDomain):

        slots = extract_non_empty_slots(tracker)

        data = moviedb.make_search_on_slots(slots, column="title")
        data = [dr[0] for dr in data]  # extract the only value of each row

        return [SlotSet("matches", "dummy ActionSearchPersonInfo data")]


class ActionSearchMovie(Action):
    def name(self):
        return 'action_search_movie'

    def run(self, dispatcher, tracker: DialogueStateTracker, domain: TemplateDomain):

        slots = extract_non_empty_slots(tracker)

        data = moviedb.make_search_on_slots(slots, column="title")
        data = [dr[0] for dr in data]  # extract the only value of each row

        matches = "This are the movies I found: " + _wrap_answer_commas_and(data)

        return [SlotSet("matches", matches)]


class ActionSearchMovieInfo(Action):
    def name(self):
        return 'action_search_movie_info'

    def run(self, dispatcher, tracker: DialogueStateTracker, domain: TemplateDomain):

        slots = extract_non_empty_slots(tracker)

        data = moviedb.make_search_on_slots(slots, column="title")
        data = [dr[0] for dr in data]  # extract the only value of each row


        return [SlotSet("matches", "dummy ActionSearchMovieInfo data")]


class ActionAnswer(Action):
    def name(self):
        return 'action_answer'

    def run(self, dispatcher, tracker, domain):
        matches = tracker.get_slot("matches")  # matches of last search

        if matches == "":
            matches = "I'm sorry, I couldn't find anything that could answer your question"

        dispatcher.utter_message(matches)
        return []
