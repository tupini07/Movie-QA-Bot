"""
For the moment, extract entities, extract intents (from train data only)
"""

import json
from pprint import pprint

import nltk
from nltk import ConditionalFreqDist

ff = json.load(open("../train_rasa.json", "r"))

data = ff["rasa_nlu_data"]["common_examples"]

# get entities and print
entities = [[entity["entity"] for entity in entry["entities"]]
            for entry in data]
entities = set(item for sub in entities for item in sub)
print("--- Entities: ")
[print(x) for x in sorted(entities)]

# Get entities that have repeated values
print("\nEntity-values that appear with different entity types")
entity_values = [[(entity["entity"], entity["value"]) for entity in entry["entities"]]
                 for entry in data]
entity_values = [i for i in entity_values if entity_values.count(i) > 1 and len(i) >= 1]
entity_values = set(pair for entities in entity_values for pair in entities)

get_entities_with_value = lambda x: [e for e in entity_values if e[1] == x]

entity_values = [e for e in entity_values if len(get_entities_with_value(e[1])) > 1]
entity_values = sorted(entity_values, key=lambda x: x[1])

pprint(entity_values)


# get intents and print
intents = [d["intent"] for d in data]
print("\n--- Intents:")
[print(x) for x in sorted(set(intents))]


texts = [d["text"] for d in data]
first_words = [s.split(" ")[0] for s in texts]

cfdist = ConditionalFreqDist()
for t, i in zip(first_words, intents):
    cfdist[t][i] += 1
