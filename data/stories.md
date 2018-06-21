## say hello
* greet
 - utter_greet
 - utter_ask_howcanhelp

## say goodbye
* goodbye
 - utter_goodbye

## happy
* thankyou
 - utter_youarewelcome


## Generated Story -2103620548391019178
* greet
    - utter_greet
    - utter_ask_howcanhelp
* actor_name{"movie_name": "the matrix", "character_name": "Neo"}
    - slot{"character_name": "Neo"}
    - slot{"movie_name": "the matrix"}
    - utter_on_it
    - action_search_person
    - slot{"matches": "dummy matches data"}
    - action_answer
* release_date
    - action_search_movie_info
    - slot{"matches": "dummy matches data"}
    - action_answer
* budget
    - action_search_movie_info
    - slot{"matches": "dummy matches data"}
    - action_answer
* thankyou
 - utter_youarewelcome
* goodbye
 - utter_goodbye


## Generated Story -2176525455732157718
* greet
    - utter_greet
    - utter_ask_howcanhelp
* release_date{"movie_name": "the matrix"}
    - slot{"movie_name": "the matrix"}
    - utter_on_it
    - action_search_movie_info
    - slot{"matches": "dummy ActionSearchMovieInfo data"}
    - action_answer
* budget
    - action_search_movie_info
    - slot{"matches": "dummy ActionSearchMovieInfo data"}
    - action_answer
* thankyou
    - utter_youarewelcome
* goodbye
    - utter_goodbye


## Generated Story 1603727790632376103
* movie_count{"movie_name": "the matrix"}
    - slot{"movie_name": "the matrix"}
    - action_search_movie_info
    - slot{"matches": "dummy ActionSearchMovieInfo data"}
    - action_answer
* actor_name{"character_name": "neo"}
    - slot{"character_name": "neo"}
    - action_search_person
    - slot{"matches": "dummy ActionSearchMovieInfo data"}
    - action_answer
* goodbye
    - utter_goodbye


## Generated Story 325349564661128329
* award_category_count{"award_ceremony": "oscars", "person_name": "tom hanks"}
    - slot{"award_ceremony": "oscars"}
    - slot{"person_name": "tom hanks"}
    - action_search_person_info
    - slot{"matches": "dummy ActionSearchPersonInfo data"}
    - action_answer


## Get director of movie, show other movies directed by him, and show the number of movies directed by him
* director{"movie_name": "eragon"}
    - slot{"movie_name": "eragon"}
    - action_search_person
    - slot{"director_name": "Stefen Fangmeier"}
    - slot{"matches": "dummy ActionSearchPerson data"}
    - action_answer
* movie
    - action_search_movie
    - slot{"matches": "dummy ActionSearchMovie data"}
    - action_answer
* movie_count
    - action_search_movie_info
    - slot{"matches": "dummy ActionSearchMovieInfo data"}
    - action_answer
* goodbye
    - utter_goodbye

## Get composer of movie and then ask what other movies has he composed for
* composer{"movie_name": "the lord of the rings"}
    - slot{"movie_name": "the lord of the rings"}
    - action_search_person
    - slot{"person_name": "Howard Shore"}
    - slot{"matches": "dummy ActionSearchPerson data"}
    - action_answer
* movie
    - action_search_movie
    - slot{"matches": "dummy ActionSearchMovie data"}
    - action_answer

 
## Generated Story 2210326579374744474
* greet
    - utter_greet
    - utter_ask_howcanhelp
* trailer{"movie_name": "eragon"}
    - slot{"movie_name": "eragon"}
    - utter_on_it
    - action_search_movie_info
    - slot{"matches": "dummy ActionSearchMovieInfo data"}
    - action_answer
* thankyou
    - utter_youarewelcome
* goodbye
    - utter_goodbye


