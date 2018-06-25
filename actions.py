import pprint

from rasa_core.actions import Action
from rasa_core.domain import TemplateDomain
from rasa_core.events import SlotSet
from rasa_core.trackers import DialogueStateTracker
from rasa_core.actions.action import ACTION_LISTEN_NAME

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
            res += f"{an}, "

        return f"{res} and {answrs[-1]}"

    elif len(answrs) == 1:
        return f"{answrs[0]}"

    else:
        return ""


def _wrap_movie_title_answer(answrs, multiple_text="There are multiple answers to your question:"):
    """
    If possible (when len(answrs) > 1, transforms the database answers
    which come in the shape ( [title, value] )
    into a string presenting the results in a nice way

    answrs -- ( [title, value] ) - holds the results from the database
    multiple_text -- the text that will be shown when there are multiple results
    """
    res = ""
    if len(answrs) > 1:
        res = f"{multiple_text} \n"
        # movie_title: answer
        res += "".join(f"-> {r[0]}: {r[1]}\n" for r in answrs)

    elif len(answrs) == 1:

        res = ("\n" if answrs[0][1].startswith("http") else "") + answrs[0][1]

    return res


class ActionSearchPerson(Action):
    def name(self):
        return 'action_search_person'

    def run(self, dispatcher, tracker: DialogueStateTracker, domain: TemplateDomain):
        ActionFalloutSlots._last_custom_action = self.name()

        slots = extract_non_empty_slots(tracker)
        latest_intent = tracker.latest_message.intent["name"]

        extra_slots = []
        if "director" in latest_intent:

            column = "director"

            # if we're searching for a director then we won't use the name
            slots.pop("director_name", None)

            # if we're asked for a director and we have a movie name in our slot then very probably
            # we want to know the name of the director who directed "movie_name". So we can just go
            # ahead and delete the others. Because of ActionFalloutSlots we know that movie_name
            # has at most one turn of being in memory, so it's recent

            # basically, just remove every other slot from the search
            # we can only suppose that this is the intent of the user if move_name was given in the
            # last message or in the preious one (so, if provided in last message or in memory)
            last_and_current_slots = [k["entity"] for k in tracker.latest_message.entities] + \
                list(ActionFalloutSlots._memory.keys())

            if "movie_name" in last_and_current_slots:
                for uneeded_slot in [k_s for k_s in slots.keys() if k_s != "movie_name"]:
                    slots.pop(uneeded_slot, None)

        else:
            column = "actors"
            # if we're searching for an actor then we won't use its name
            slots.pop("actor_name", None)

        # returns something of the shape [rows x columns]
        data = moviedb.make_search_on_slots(slots, column=column)
        data = [dr[0] for dr in data]  # extract the only value of each row

        if column == "director":
            # just the name of the directors
            data = set(data)
            matches = _wrap_answer_commas_and(data)

            if len(data) == 1:  # if there is only one director then we save it the director slot
                # in this way we can answer follow up questions regarding the director that the user may make
                extra_slots.append(SlotSet("director_name", matches))
                ActionFalloutSlots.add_slot_to_memory("director_name", matches) # we must also ensure to ta add director name to memory

        else:
            matches = []
            for rw in data:  # this can be made nicer
                matches += rw.split("|") if rw else ""
            matches = _wrap_answer_commas_and(set(matches))

            if matches != "" and "movie_name" in slots.keys() and "character_name" in slots.keys():
                matches = f"I don't have in my database the information to tell you who is the actor " + \
                          f"of '{slots['character_name'].title()}' in '{slots['movie_name'].title()}' " + \
                          "but I can tell you that these are the actors in the movie: " + matches

        return [SlotSet("matches", matches)] + extra_slots


class ActionSearchPersonInfo(Action):
    def name(self):
        return 'action_search_person_info'

    def run(self, dispatcher, tracker: DialogueStateTracker, domain: TemplateDomain):
        ActionFalloutSlots._last_custom_action = self.name()

        slots = extract_non_empty_slots(tracker)

        matches = ""

        # get the person we want to get information on
        name = [slots[x]
                for x in ["actor_name", "person_name"] if x in slots.keys()]
        if len(name) > 0:  # if we found the name

            matches = "I'm sorry but I don't have any information regarding actors in my database. But you can find such information in their IMDB page! \n"
            matches += f"https://www.imdb.com/find?ref_=nv_sr_fn&q={name[0].replace(' ', '+')}&s=nm"

        return [SlotSet("matches", matches)]


class ActionSearchMovie(Action):
    def name(self):
        return 'action_search_movie'

    def run(self, dispatcher, tracker: DialogueStateTracker, domain: TemplateDomain):
        ActionFalloutSlots._last_custom_action = self.name()

        slots = extract_non_empty_slots(tracker)

        # we're definately not using the movie name to search for a movie so we pop it
        slots.pop("movie_name", None)

        data = moviedb.make_search_on_slots(slots, column="title")
        data = [dr[0] for dr in data]  # extract the only value of each row

        matches = ""

        if len(data) > 0:  # if not we didn't find any movies
            matches = "This are the movies I found: " + \
                _wrap_answer_commas_and(data)
        else:
            matches = "I'm sorry, I couldn't find any movies that matched your criteria"

        return [SlotSet("matches", matches)]


class ActionSearchMovieInfo(Action):
    def name(self):
        return 'action_search_movie_info'

    def run(self, dispatcher, tracker: DialogueStateTracker, domain: TemplateDomain):
        ActionFalloutSlots._last_custom_action = self.name()

        intent_column_map = {
            "language": "language",
            "country": "country",
            "genre": "genres",
            "budget": "budget",
            "date": "year",
            "director": "director",
            "subjects": "plot_keywords",

            "rating": "imdb_score",
            "review": "imdb_score",

            "revenue": "gross",
        }

        slots = extract_non_empty_slots(tracker)
        latest_intent = tracker.latest_message.intent["name"]
        matches = ""

        # basically, just remove every other slot from the search
        # we can only suppose that this is the intent of the user if move_name was given in the
        # last message or in the preious one (so, if provided in last message or in memory)
        last_and_current_slots = [k["entity"] for k in tracker.latest_message.entities] + \
            list(ActionFalloutSlots._memory.keys())

        if "movie_name" in last_and_current_slots:
            for uneeded_slot in [k_s for k_s in slots.keys() if k_s != "movie_name"]:
                slots.pop(uneeded_slot, None)


        def kws_in_latest_intent(*kws):
            is_in = [x in latest_intent for x in kws]
            return any(is_in)

        # if we can just get away with searching the DB then we do that, if not then we handle the special cases
        column_idx = [mkk for mkk in intent_column_map.keys()
                      if mkk in latest_intent]
        if len(column_idx) > 0:

            column = intent_column_map[column_idx[0]]
            data = moviedb.make_search_on_slots(
                slots, column=f"title, {column}")

            matches = _wrap_movie_title_answer(data)

        ###########################################

            # if we only have one result then we can present it nicely :)
            if len(data) == 1 and "have this information in my database" not in data[0][1]:
                if kws_in_latest_intent("rating", "review"):
                    matches = f"It has a score of {matches} in IMDB"

                elif kws_in_latest_intent("date"):
                    matches = f"It was released in the year {matches}"

                elif kws_in_latest_intent("budget"):
                    matches = f"It had a budger of ${matches}"

                elif kws_in_latest_intent("language"):
                    matches = f"It was originally made in {matches}"

                elif kws_in_latest_intent("revenue"):
                    matches = f"It made a total revenue of ${matches}"

        ###########################################
        # If we can't just check the answer in the database
        # - can't provide the information because we don't have it
        # - or we have to present the informatio in a special way
        # then we check for the different cases and handle them separately

        # if we're asked for the count of the movies in the series
        
        elif kws_in_latest_intent("count"):
            data = moviedb.make_search_on_slots(slots, column="title")
            if len(data) > 0:
                matches = f"In my database I have that there are {len(data)} movies in the series: \n" + "\n".join(
                    " - " + x[0] for x in data)

        ###########################################

        elif kws_in_latest_intent("runtime"):  # if we're asked for the runtime
            data = moviedb.make_search_on_slots(
                slots, column="title, duration")

            matches = _wrap_movie_title_answer(data, multiple_text="")

            if len(data) > 1:
                matches = "There are multiple movies which correspond to your question. Here is a list " + \
                          "of them and thier respective duration in minutes:" + \
                          matches
            elif len(data) == 1:
                matches = f"The duration is of {matches} minutes."

        ###########################################
        else:
            # We can't really provide all the other
            data = moviedb.make_search_on_slots(
                slots, column="title, movie_imdb_link")

            links = _wrap_movie_title_answer(data, multiple_text="")

            if links == "":
                matches = ""

            ###########################################
            elif kws_in_latest_intent("trailer", "media", "picture"):
                matches = "I'm sorry but I don't have information on trailers. You can find the trailer and other media about the movie on its IMDB page: " + links

            ###########################################
            elif kws_in_latest_intent("producer", "picture", "organization", "other"):
                matches = "I'm sorry but I don't have the information to answer your question. You can find information on the producer, organization, or other, in the movie's IMDB page: " + links

            ###########################################
            elif kws_in_latest_intent("theater"):
                matches = "I'm sorry but I have no information on theaters. You can check your favourite cinema's page to find showings :)"

            ###########################################
            elif kws_in_latest_intent("synopsis"):
                matches = "I'm sorry but I don't have access to synopsis information on the movies. But you can find it in its IMDB page: " + links

        return [SlotSet("matches", matches)]


class ActionAnswer(Action):
    def name(self):
        return 'action_answer'

    def run(self, dispatcher, tracker, domain):

        matches = tracker.get_slot("matches")  # matches of last search

        if matches == " " or matches == "" or matches is None:  # we didn't find anything or there was an error
            matches = "I'm sorry, I couldn't find anything that could answer your question"

        dispatcher.utter_message(matches)
                
        tracker.trigger_follow_up_action(
            domain.action_map["action_fallout_slots"][1]
        )

        return []


class ActionFalloutSlots(Action):
    """
    This is to force the bot to use a kind of "short term memory" in which the slots values are
    forgotten after some time, instead of the standard "permanent memory" in which the slot
    values are remembered forever.
    This lets the bot handle multiple topics (or at least handle them more easily) in longer conversations
    """
    # this is the amount of life all new memories have (the extra amount of turns for which the bot will)
    # remember the slot
    _last_custom_action = ""
    
    LIFETIME = 1

    _memory = {
        # each entry will have the following shape
        # entity: {value: , life: ,}

        # life will decrease, once it reaches 0 then that slot is deleted
        # and the entry is removed from memory
    }

    @classmethod
    def add_slot_to_memory(cls, slotname, slotvalue):
        cls._memory[slotname] = {"value": slotvalue, "life": cls.LIFETIME + 1}


    @classmethod
    def _countdown_memory(cls, tracker: DialogueStateTracker):
        """
        Decrease the "life" value of all memory units by one, and return a [ SlotSet() ]
        array to remove "dead" units from bot slots
        """
        to_remove = []

        # we do this so we don't get a "dict changed during iteration" error
        current_items = cls._memory.copy().items()
        for k, vd in current_items:
            vd["life"] -= 1

            if vd["life"] <= 0:
                # if last action was to answer some movie information and we have the movie
                # name then it is possible that the user will still want to talk about the movie.
                # so we extend movie_name entity life by one more turn
                if cls._last_custom_action == "action_search_movie_info" and \
                        k == "movie_name":
                    vd["life"] += 1

                else:
                    to_remove.append(SlotSet(k, None))
                    cls._memory.pop(k, None)

        return to_remove

    @classmethod
    def _update_memory_with_new(cls, new_entities):
        """
        Add new entities to memory (note that we use one extra life value because
        it will inmediatelly be decreased in the next line)
        """
        for k, v in new_entities.items():
            cls.add_slot_to_memory(k, v)


    def name(self):
        return "action_fallout_slots"

    def run(self, dispatcher, tracker: DialogueStateTracker, domain: TemplateDomain):

        ents = {e["entity"]: e["value"]
                for e in tracker.latest_message.entities}

        # add new entities to memory
        ActionFalloutSlots._update_memory_with_new(ents)

        # "forgetting procedure"
        to_remove = ActionFalloutSlots._countdown_memory(tracker)

        # for debugging
        # print("-- last action: " + str(tracker.latest_action_name))
        # print("-- memory: " + str(ActionFalloutSlots._memory))
        # print("-- intent: " + str(tracker.latest_message.intent["name"]))
        # print("-- stuff to pop: " + str(to_remove))
        # print("-- what slots we have: " + str(extract_non_empty_slots(tracker)))

        # this action is always followed by listen
        tracker.trigger_follow_up_action(
            domain.action_map[ACTION_LISTEN_NAME][1]
        )

        # clean slots
        return [SlotSet("matches", None)] + to_remove
