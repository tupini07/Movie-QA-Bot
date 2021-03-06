from rasa_core.policies import Policy
from rasa_core.actions.action import ACTION_LISTEN_NAME
from rasa_core import utils
import numpy as np


class MoviePolicy(Policy):

    def __init__(self,
                 featurizer=None,  # type: Optional[TrackerFeaturizer]
                 ):
        # type: (...) -> None

        super(MoviePolicy, self).__init__(featurizer)

    def predict_action_probabilities(self, tracker, domain):
        # These are the arrays of intents associated with each type of action
        search_movie_intents = [
            "media",
            "movie",
            "movie_name",
            "director movie date rating",
            "director movie rating",
            "director movie_name",
            "movie language",
        ]

        search_movie_info_intents = [

            "language",

            "country",

            "genre",

            "subjects",

            "budget",
            "movie budget",

            "movie date",
            "release_date",

            "movie director",

            "movie subjects",

            "movie trailer",
            "trailer",
            "movie media",

            "movie_count",

            "organization",
            "producer",
            "producer picture",
            "producer_count",
            "movie producer",

            "movie rating",
            "rating",
            "rating rating",
            "review",
            "review movie",
            "review rating",

            "revenue",

            "runtime",

            "synopsis",

            "theater",

            "picture",
            "movie_other",
        ]

        search_person_intents = [
            "actor",
            "actor_name",
            "actor_name character",
            "character",
            "composer",
            "director",
            "director producer",
            "director_name",
            "person",
            "person_name",
            "writer",
        ]

        search_person_info_intents = [
            "birth_date",
            "award_category_count",
            "award_count",
            "award_ceremony award_category",
        ]

        # we convert the arrays into dicts so that we can get the specific kind of action related to an intent
        search_movie_intents = {k: "action_search_movie"
                                for k in search_movie_intents}
        search_movie_info_intents = {k: "action_search_movie_info"
                                     for k in search_movie_info_intents}
        search_person_intents = {k: "action_search_person"
                                 for k in search_person_intents}
        search_person_info_intents = {k: "action_search_movie_info"
                                      for k in search_person_info_intents}

        # aggregate all into one dict
        intent_action_map = {**search_movie_intents,
                             **search_movie_info_intents,
                             **search_person_intents,
                             **search_person_info_intents}

        # dict -> action_name: action_id
        action_ids = {k: v[0] for k, v in domain.action_map.items()}

        # the name of the current intent
        last_intent = tracker.latest_message.intent["name"]

        # if previous action was "LISTEN" and the current intent is one of the intents we can handle
        # and the previous action was not one of our custom actions (all start with action_)
        if tracker.latest_action_name == ACTION_LISTEN_NAME and \
                last_intent in intent_action_map.keys() and \
                tracker.latest_action_name not in list(intent_action_map.values()) + ["action_fallout_slots"]:
                
            action = intent_action_map[last_intent]
            id_action = action_ids[action]
            return utils.one_hot(id_action, domain.num_actions)

        # if last action was one we gave in this policy (ie, a search action) then we want our next
        # action to be the "Answer" action.
        elif tracker.latest_action_name in intent_action_map.values():
            id_action = action_ids["action_answer"]
            return utils.one_hot(id_action, domain.num_actions)

        elif tracker.latest_action_name == "action_answer":
            return utils.one_hot(action_ids["action_fallout_slots"], domain.num_actions)

        else:  # we can't handle the current intent so just pass control to another policy
            return np.zeros(domain.num_actions)

    def train(self,
              training_trackers,  # type: List[DialogueStateTracker]
              domain,  # type: Domain
              **kwargs  # type: **Any
              ):
        # type: (...) -> None
        """
        This is just a 'scripted' policy, so there is really no need to train.
        This method is just a placeholder so that we can use this policy during online training.
        """
        pass

    def persist(self, path):
        """
        The same as train. This is only a dummy method so that we can create our own
        "scripted policy"
        """
        pass

    @classmethod
    def load(cls, path):
        """
        also this one is a placeholder method
        """
        return cls()
