import argparse
import json
import re
from typing import Dict, List


# TODO: consider checking first words of sentences for extra information
# Can see what are the most common starting words of these questions. Practically we could do something like
# - list_actor
# - who_actor -> could contain show, which what
# - list_movies
# - etc

#TODO useful https://rasahq.github.io/rasa-nlu-trainer/


##########################################
# setup command line arguments

parser = argparse.ArgumentParser(
    description='Parse a data file from NLSPARQL to Rasa format (JSON).')

parser.add_argument("input_file", type=str, help="The path of the input data (ie, NLSPARQL.train.data).")

parser.add_argument("label_file", type=str, help="The name of the file that contains the labels (intentions) for each sentence"
                    "same folder as this script.")

parser.add_argument("output_file", type=str,
                    help="The name of the rasa formatted data.")
args = parser.parse_args()


##########################################
# load nlsql data and transform to [ .. (word, tag) .. ]

with open(args.input_file, "r") as input_file:
    contents = [[pair.split("\t") for pair in sentence.split("\n")]
                for sentence in input_file.read().split("\n\n")]


intents = open(args.label_file, "r", encoding="utf-8").read().split("\n")

##########################################
# convert "Contents" into dicts, similar to rasa JSON format


def extract_text(sentence: List[List[str]]) -> str:
    """
    Extracts the text of a sentece
    """
    return " ".join(p[0] for p in sentence)


def extract_tags(sentence: List[List[str]]) -> List[Dict[str, str]]:
    """
    Extracts the tags and their positions. 
    For a sentence returns an array of all non-O tags, with B- and I- stripped
    And similar tags joined
    """
    def create_ct(pair):
        return {
            "text": pair[0],
            "tag": pair[1][2:].replace(".", "_")
        }

    tags = []
    current_tag = {}
    previous_tag = "O"

    for pair in sentence:
        if pair[1] == "O":
            previous_tag = "O"
            continue  # skip words wit O
        else:
            if pair[1].startswith("B-"):
                # Sometimes there are consecutive tags that start with B-. This is not good, so we "fix" them here.
                # Since we may have consecutive B tags then we check if next tag is the same as previous one
                if previous_tag == pair[1]:
                    current_tag["text"] += " " + pair[0]

                else:
                    # if tag is a beginning tag then create a new
                    # "working tag"
                    if current_tag != {}:
                        tags.append(current_tag)

                    current_tag = create_ct(pair)

            elif pair[1].startswith("I-"):
                # There are some tags in the dataset which are not correct. The group of tags starts
                # directly with I- instead of B-.  Instead of fixing the dataset we'll manage this directly
                # here by using "previous_tag" (ugly, but works)
                if previous_tag == "O":  # it means this tag should actually start with B-
                    current_tag = create_ct(pair)

                else:
                    # append information to current working tag
                    current_tag["text"] += " " + pair[0]

            previous_tag = pair[1]  # finally re-write previous tag placeholder

    if current_tag != {}:
        # if working tag is not {} then add it to tags []
        # otherwise it means that we didn't find any tags on this sentence
        tags.append(current_tag)

    return tags


sent_dicts = []
for idx, sentence in enumerate(contents):
    s_text = extract_text(sentence)
    s_tags = extract_tags(sentence)

    entities = []
    for tag in s_tags:

        match = re.search(tag["text"], s_text)
        entities.append({
            "value": tag["text"],
            "entity": tag["tag"],
            "start": match.start(),
            "end": match.end(),

        })

    sent_dicts.append({
        "text": s_text,
        "intent": intents[idx],
        "entities": entities
    })



##########################################
# finally convert to json and write to file
# External examples is just a file that contain extra examples appart from the ones
# in the NLSPARQL dataset. These have been mainly included to account for the low number
# of examples for certain intents
external_examples = json.load(open("../external_examples.json", "r"))

with open(args.output_file, "w") as output_file:
    
    json.dump({
        "rasa_nlu_data": {
            "common_examples": sent_dicts + external_examples,
            "entity_examples": [],
            "intent_examples": []
        },
    }, output_file)

print(
    f"Done, converted {len(contents)} examples to JSON rasa format. Data has been saved to `{args.output_file}`")
