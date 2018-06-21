import argparse
import json
import re

parser = argparse.ArgumentParser(
    description='Takes multiple rasa nlu data json files as input and outputs one json with all the data aggregated')

parser.add_argument("output_file",
                    type=str,
                    help="The name of the output aggregated file")

parser.add_argument("input_files",
                    type=argparse.FileType('r'),
                    nargs="+",
                    help="The path of the input data files")

args = parser.parse_args()


aggregated = {"rasa_nlu_data": {
    "common_examples": [],
    "entity_examples": [],
    "intent_examples": []
}}

for inpf in args.input_files:
    ff = json.load(inpf)
    aggregated["rasa_nlu_data"]["common_examples"] += ff["rasa_nlu_data"]["common_examples"]

with open(args.output_file, "w+") as out_f:
    json.dump(aggregated, out_f)
