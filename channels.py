
import six
from builtins import input

import pyttsx3
import speech_recognition as sr
from rasa_core import utils
from rasa_core.channels.channel import InputChannel, OutputChannel, UserMessage
from rasa_core.interpreter import INTENT_MESSAGE_PREFIX


class VoiceOutputChannel(OutputChannel):
    """Simple bot that outputs the bots messages to the command line."""

    default_output_color = utils.bcolors.OKBLUE
    TTSENGINE = pyttsx3.init()

    def send_text_message(self, recipient_id, message):
        # type: (Text, Text) -> None
        what_to_say = message
        if len(what_to_say) > 250: # if we're going to say something very long then truncate it
            what_to_say = "I found to much results to speak them, so I'll just print them to the console instead"

        what_to_say = what_to_say.split("\n")[0]

        self.TTSENGINE.say(what_to_say)
        print("Bot: " + message)
        self.TTSENGINE.runAndWait() 


class VoiceInputChannel(InputChannel):
    """Input channel that reads the user messages from the command line."""

    def __init__(self, prefer_text_input=False, sender_id=UserMessage.DEFAULT_SENDER_ID):
        # type: (Text) -> None
        self.sender_id = sender_id
        self.prefer_text_input = prefer_text_input

        if not prefer_text_input:
            self.SRECOGNIZER = sr.Recognizer()
            self.MICROPHONE = sr.Microphone()


    def _record_messages(self, on_message, max_message_limit=None):
        utils.print_color("Bot loaded with voice capabilities!",
                          utils.bcolors.OKGREEN)
        num_messages = 0
        while max_message_limit is None or num_messages < max_message_limit:
            try:
                if self.prefer_text_input: ## if we want to do normal text input and have audio output:
                    text = input("\nYour Input: ").strip()
                    
                else: # if we want to use text input as well
                    with self.MICROPHONE as source:
                        self.SRECOGNIZER.adjust_for_ambient_noise(source)
                        input("\nBot is ready! Press enter when you're ready to speak.")
                        audio = self.SRECOGNIZER.listen(source)
                    
                    print("Bot is recognizing what you said ...")
                    text = self.SRECOGNIZER.recognize_google(audio)
                    print("You said: " + text)

            except Exception:
                text = input("Voice does not work :( input your query here: ").strip()

            if six.PY2:
                # in python 2 input doesn't return unicode values
                text = text.decode("utf-8")
            if text == INTENT_MESSAGE_PREFIX + 'stop':
                return
            on_message(UserMessage(text, VoiceOutputChannel(),
                                   self.sender_id))
            num_messages += 1

    def start_async_listening(self, message_queue):
        self._record_messages(message_queue.enqueue)

    def start_sync_listening(self, message_handler):
        self._record_messages(message_handler)
