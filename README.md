# Movie-QA Bot

This is a bot that answers questions about movies either via text or via voice (or text input and voice output), it was developed as the second/final project of the *Language Understanding Systems* course at *UNITN*. 

This repository contains the code to run, build and evaluate the bot, and an accompaigning report that can be seen [here](https://github.com/tupini07/Movie-QA-Bot/blob/master/report/report.pdf).

If you want to see an example conversation with the bot you can see the "[Example of an actual conversation with the bot](#example-of-an-actual-conversation-with-the-bot)" section later on in this readme.

# What kind ok questions can the bot answer?

The bot can answer questions about the movie domain. All the topics it can answer are found in the [movie_domain.yml](https://github.com/tupini07/Movie-QA-Bot/blob/370d23441eeea3077dccbf46ba0e44a9fe4a1aa5/movie_domain.yml#L78) file, under *intents*, but basically it can answer this kind of queries:

- Find actor/director of a movie or movies 
    - For example: all comedy movies, or movies published in 1990, made in a given country, etc
- Find information on a given movie or movies. Basically it can answer question regarding with: *language, country, genre, budget, date, subjects (think about plot keywords), rating/reviews*, and *revenue*. Some examples:
    - *what is the gross revenue of movies published in Germany*
    - *when was Phantom Menace released*
    - *what genre is Star Wars*
- It can count movies in a series:
    - *how many Star Wars movies exist*

It can also answer follow up questions since it keeps track of the context. For an example of a conversation where context is used, see the "[Example of an actual conversation with the bot](#example-of-an-actual-conversation-with-the-bot)" section later on in this readme.


# How to run

The first thing you need to do to be able to run the bot is to install the dependencies:

- For the basic bot functionality:
    - [rasa_core](https://github.com/RasaHQ/rasa_core) version 0.9.5
    - [rasa_nlu](https://github.com/RasaHQ/rasa_nlu) version 0.12.3
- If you want to use the or using TTS and STT:
    - [pyttsx3](https://github.com/nateshmbhat/pyttsx3)
    - [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
    - [PyAudio](http://people.csail.mit.edu/hubert/pyaudio/)

After these are installed (or only the first 2 if you don't care for the speech functionality) you can proceed to check out the [Makefile](https://github.com/tupini07/Movie-QA-Bot/blob/master/Makefile) which already defines a `help`  with the bot's capabilities and provides shortcuts to run all the commands. To just run the bot you need to first train the model with:

`make train-nlu-aggregated train-dialogue`

and then you can run the bot with `make run-bot` for simple text input output. See below for other ways in which to run it.

Here is a basic rundown of the "recipes" provided in the Makefile and what they do:

- `run-bot` -- run bot on the command line (text input and output)
- `run-voice` -- run bot over voice (voice input and output)
- `run-voice-only-output` -- run bot with normal text input but voice output
- `train-nlu` -- train nlu module on training data
- `train-nlu-aggregated` -- train nlu module on aggregation of train and test data
- `train-dialogue` -- train dialogue module
- `train-online` -- start bot in interactive training mode using RegEx interpreter (see [this page](https://core.rasa.com/tutorial_interactive_learning.html) for more information on how this works)
- `train-online-with-nlu` -- start bot in interactive training mode using the NLU interpreter
- `convert-data` - converts NLSPARQL data to rasa format (this is the NLU data)
- `evaluate-nlu` -- only evaluate nlu against test data
- `evaluate-nlu-crossval` -- do a crossvalidation on aggregated dataset
- `evaluate-dialogue` -- only evaluate dialogue against test data
- `train-and-evaluate` -- train nlu and dialogue and evaluate both


# Project Structure

The functionality of the bot is separated across the following python modules:

- `bot.py` - this is the main interface with the bot. It handles training and running the bot.
- `moviedb.py` - this module is in charge of comunicating with the databaste, which by the way is an SQLite DB and is located [here](https://github.com/tupini07/Movie-QA-Bot/tree/master/data/db).
- `channels.py` - here we define the functionality for the *voice communication channels*. Here are defined both the input and the output voice channels.
- `actions.py` - this is the largest of all the modules and includes all the actions that the bot can do. They define what kind of questions the bot can answer satisfactorily and which not. The actions, and a basic definition, are the following:
    -  **ActionSearchPerson** - is in charge or searching actors and directors
    -  **ActionSearchPersonInfo** - doesn't really do much since the database doens't hold "personal information" on actors and directors. For the moment it just redirects users to the "person's" IMDB page. It was intented as the action that could answer questions like "*who played Neo in The Matrix*"
    -  **ActionSearchMovie** - it is in charge of searching for a movie or set of movies that satisfy a given query (ie, comedy movies, or those made by a given director)
    -  **ActionSearchMovieInfo** - this is the largest action and is in charge of finding all the information related to a movie. It is in charge of answering questions like "*what genre is Star Wars*"
    -  **ActionAnswer** - it is in charge of siplaying the answer to the user or saying that no answer was found
    -  **ActionFalloutSlots** - this is a special action that implements a *forgetting mechanism* that helps the bot funcion properly in longer conversations (4 or more turns). For more information on this action see the [report](https://github.com/tupini07/Movie-QA-Bot/blob/master/report/report.pdf).
- `policy.py` - this contains the main dialogue policy for the bot. It is in charge of routing a user request to the appropiate action (ie, user wants to know the director of a movie so the policy gives the request to `ActionSearchPerson`)


# Data utilities

Besides the main code of the bot (defined above) there are also some other script that are in charge of working with the dataset provided for the project. These scripts can be found in the [data/scripts](https://github.com/tupini07/Movie-QA-Bot/tree/master/data/scripts) folder. 

- `convert_to_rasa.py` - The dataset for training the NLU module was originally provided in NLSPARQL format (this original data can be found [here](https://github.com/tupini07/Movie-QA-Bot/tree/master/data/NLSPARQL)). This script is in charge of converting the NLSPARQL data into the json format that is recognized by *rasa*. It is used to convert both the training and testing data.
- `create_database.py` - this is just a simple script to create the SQLite database given the original database schema and data that were provided for the project.
- `agregate_jsons.py` - this script is in charge of aggregating 2 rasa formatted jsons into one. It it used to join the training and testing files generated by `convert_to_rasa.py` so that we can use this big, aggregated, file when training for *production*.
- `analyze_data.py` - prints some basic information on the data.


# Example of an actual conversation with the bot

```
User: Hello
Bot: Hi
Bot: How may I help you?

User: when was Phantom Menace released
Bot: It was released in the year 1999

User: who were the actors in The Matrix
Bot: Marcus Chong, Gloria Foster, Nona Gaye, Steve Bastoni, Daniel Bernhardt, Keanu Reeves, Collin Chou, Essie Davis,  and Helmut Bakaitis

User: when was it published
Bot: There are multiple answers to your question: 
-> The Matrix: 1999
-> The Matrix Revolutions: 2003
-> The Matrix Reloaded: 2003

User: what was the revenue
Bot: There are multiple answers to your question: 
-> The Matrix: 171383253
-> The Matrix Revolutions: 139259759
-> The Matrix Reloaded: 281492479

User: what year was Clueless released
Bot: It was released in the year 1995

User: who directed it
Bot: Amy Heckerling

User: which other movies did she direct
Bot: This are the movies I found: Fast Times at Ridgemont High, Clueless, Loser, and Vamps

User: who starred in Harry Potter
Bot: Gary Oldman, Verne Troyer, Daniel Radcliffe, Alfred Enoch, Ralph Ineson, Toby Jones, Dave Legeno, Robert Pattinson, Rupert Grint, Alan Rickman, Emma Watson,  and Fiona Shaw

User: show me trailers
Bot: I'm sorry but I don't have information on trailers. You can find the trailer and other media about the movie on its IMDB page:  
-> Harry Potter and the Sorcerer's Stone: http://www.imdb.com/title/tt0241527/?ref_=fn_tt_tt_1
-> Harry Potter and the Chamber of Secrets: http://www.imdb.com/title/tt0295297/?ref_=fn_tt_tt_1
-> Harry Potter and the Prisoner of Azkaban: http://www.imdb.com/title/tt0304141/?ref_=fn_tt_tt_1
-> Harry Potter and the Goblet of Fire: http://www.imdb.com/title/tt0330373/?ref_=fn_tt_tt_1
-> Harry Potter and the Order of the Phoenix: http://www.imdb.com/title/tt0373889/?ref_=fn_tt_tt_1
-> Harry Potter and the Half-Blood Prince: http://www.imdb.com/title/tt0417741/?ref_=fn_tt_tt_1
-> Harry Potter and the Deathly Hallows: Part I: http://www.imdb.com/title/tt1571403/?ref_=fn_tt_tt_1
-> Harry Potter and the Deathly Hallows: Part II: http://www.imdb.com/title/tt1680310/?ref_=fn_tt_tt_1

User: thank you
Bot: Any time ;)

User: bye
Bot: Goodbye. Have a nice day!
```