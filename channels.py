
import pyttsx3
import six
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
        self.TTSENGINE.say(message)
        self.TTSENGINE.runAndWait() 
        utils.print_color("Bot is answering ... Following is a transcription of what it's saying: ", self.default_output_color)
        utils.print_color(message, self.default_output_color)



class VoiceInputChannel(InputChannel):
    """Input channel that reads the user messages from the command line."""

    SRECOGNIZER = sr.Recognizer()
    MICROPHONE = sr.Microphone()

    def __init__(self, sender_id=UserMessage.DEFAULT_SENDER_ID):
        # type: (Text) -> None
        self.sender_id = sender_id

    def _record_messages(self, on_message, max_message_limit=None):
        utils.print_color("Bot loaded with voice capabilities! Speak: ",
                          utils.bcolors.OKGREEN)
        num_messages = 0
        while max_message_limit is None or num_messages < max_message_limit:

            with self.MICROPHONE as source:
                audio = self.SRECOGNIZER.listen(source)
                
            text = self.SRECOGNIZER.recognize_google(audio)

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
