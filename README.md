# Dependencies

- For the basic bot functionality:
    - [rasa_core](https://github.com/RasaHQ/rasa_core)
    - [rasa_nlu](https://github.com/RasaHQ/rasa_nlu)
- For using TTS and STT:
    - [pyttsx3](https://github.com/nateshmbhat/pyttsx3)
    - [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
    - [PyAudio](http://people.csail.mit.edu/hubert/pyaudio/)


# Example of an actual conversation with the bot

```
User: hi
Bot: Hi
Bot: How may I help you?

User: who was the director of Avatar
Bot: James Cameron

User: show me other movies by him
Bot: This are the movies I found: The Terminator, Aliens, The Abyss, Terminator 2: Judgment Day, True Lies, Titanic, and Avatar

User: who was the producer of Titanic
Bot: I'm sorry but I don't have the information to answer your question. You can find information on the producer, organization, or other, in the movie's IMDB page: http://www.imdb.com/title/tt0120338/?ref_=fn_tt_tt_1

User: what are its reviews
Bot: It has a score of 7.7 in IMDB

User: thank you
Bot: Any time ;)

User: bye
Bot: Goodbye. Have a nice day!
```