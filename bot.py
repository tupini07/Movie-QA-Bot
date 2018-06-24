import argparse
import logging
import warnings

from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RasaNLUInterpreter, RegexInterpreter

from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.policies.keras_policy import KerasPolicy
from policy import MoviePolicy

try:
    from channels import VoiceInputChannel
except ImportError as e:
    import traceback
    traceback.print_exc()
    print("It seems that there are some issues when loading the voice module. Error: ")
    print("Execution will proceed but defaulting to text input/output instead of voice")
    def VoiceInputChannel (**kw):
        return ConsoleInputChannel()

warnings.filterwarnings(action='ignore', category=DeprecationWarning)


def train_dialogue(domain_file="movie_domain.yml",
                   model_path="models/dialogue",
                   training_data_file="data/stories.md"):
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(max_history=2),
                            KerasPolicy(),
                            MoviePolicy()])  # ScriptedPolicy()])

    training_data = agent.load_data(training_data_file)
    agent.train(
        training_data,
        epochs=400,
        batch_size=100,
        validation_split=0.2
    )

    agent.persist(model_path)
    return agent


def train_online(domain_file="movie_domain.yml",
                 training_data_file='data/stories.md',
                 use_nlu_interpreter=False):

    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(max_history=2),
                            KerasPolicy(),
                            MoviePolicy()],
                  interpreter=RasaNLUInterpreter("models/nlu/default/current") if use_nlu_interpreter else RegexInterpreter())

    training_data = agent.load_data(training_data_file)
    agent.train_online(training_data,
                       input_channel=ConsoleInputChannel(),
                       batch_size=50,
                       epochs=200,
                       max_training_samples=300)

    return agent


def train_nlu(aggregated=False):
    """
    Sets up training the NLU module. If aggregated is false then model is trained only with the 
    training data. If it is true then it is trained with training+testing data.

    aggregated -- bool - whether we train with the aggregated (if True) or only training (if false) data
    """
    from rasa_nlu.training_data import load_data
    from rasa_nlu import config
    from rasa_nlu.model import Trainer 

    training_data = load_data(
        "data/" + ("train_rasa" if not aggregated else "aggregated") + ".json")
    trainer = Trainer(config.load("nlu_model_config.yml"))
    trainer.train(training_data)
    model_directory = trainer.persist('models/nlu/',
                                      fixed_model_name="current")
    return model_directory


def run(serve_forever=True, voice=False, voice_only_in_output=False):
    interpreter = RasaNLUInterpreter("models/nlu/default/current")
    agent = Agent.load("models/dialogue", interpreter=interpreter)

    if serve_forever:
        if voice:
            agent.handle_channel(VoiceInputChannel(
                prefer_text_input=voice_only_in_output))
        else:
            agent.handle_channel(ConsoleInputChannel())

    return agent


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Script that starts different functionalities of the bot.')

    parser.add_argument(
        'task',
        choices=["train-nlu", "train-nlu-agg", "train-dialogue",
                 "train-online-wnlu", "train-online",
                 "run", "run-voice", "run-voice-only-output"],
        help="Specify what action you want the bot to make: train (in various ways) or run?")
    task = parser.parse_args().task

    # decide what to do based on first parameter of the script
    if task == "train-nlu":
        train_nlu()
    elif task == "train-nlu-agg":
        train_nlu(aggregated=True)
    elif task == "train-dialogue":
        train_dialogue()
    elif task == "train-online":
        train_online(use_nlu_interpreter=False)
    elif task == "train-online-wnlu":
        train_online(use_nlu_interpreter=True)

    elif task == "run-voice-only-output":
        run(voice=True, voice_only_in_output=True)
    elif task == "run-voice":
        run(voice=True)
    elif task == "run":
        run()
    else:
        warnings.warn(
            "The argument passed to the bot is not recognized. Please run this script with '-h' to see the supported actions.")
        exit(1)
