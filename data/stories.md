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
    - action_fallout_slots
* release_date
    - action_search_movie_info
    - slot{"matches": "dummy matches data"}
    - action_answer
    - action_fallout_slots
* budget
    - action_search_movie_info
    - slot{"matches": "dummy matches data"}
    - action_answer
    - action_fallout_slots
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
    - action_fallout_slots
* budget
    - action_search_movie_info
    - slot{"matches": "dummy ActionSearchMovieInfo data"}
    - action_answer
    - action_fallout_slots
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
    - action_fallout_slots
* actor_name{"character_name": "neo"}
    - slot{"character_name": "neo"}
    - action_search_person
    - slot{"matches": "dummy ActionSearchMovieInfo data"}
    - action_answer
    - action_fallout_slots
* goodbye
    - utter_goodbye


## Generated Story 325349564661128329
* award_category_count{"award_ceremony": "oscars", "person_name": "tom hanks"}
    - slot{"award_ceremony": "oscars"}
    - slot{"person_name": "tom hanks"}
    - action_search_person_info
    - slot{"matches": "dummy ActionSearchPersonInfo data"}
    - action_answer
    - action_fallout_slots


## Get director of movie, show other movies directed by him, and show the number of movies directed by him
* director{"movie_name": "eragon"}
    - slot{"movie_name": "eragon"}
    - action_search_person
    - slot{"director_name": "Stefen Fangmeier"}
    - slot{"matches": "dummy ActionSearchPerson data"}
    - action_answer
    - action_fallout_slots
* movie
    - action_search_movie
    - slot{"matches": "dummy ActionSearchMovie data"}
    - action_answer
    - action_fallout_slots
* movie_count
    - action_search_movie_info
    - slot{"matches": "dummy ActionSearchMovieInfo data"}
    - action_answer
    - action_fallout_slots
* goodbye
    - utter_goodbye

## Get composer of movie and then ask what other movies has he composed for
* composer{"movie_name": "the lord of the rings"}
    - slot{"movie_name": "the lord of the rings"}
    - action_search_person
    - slot{"person_name": "Howard Shore"}
    - slot{"matches": "dummy ActionSearchPerson data"}
    - action_answer
    - action_fallout_slots
* movie
    - action_search_movie
    - slot{"matches": "dummy ActionSearchMovie data"}
    - action_answer
    - action_fallout_slots

 
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
    - action_fallout_slots
* thankyou
    - utter_youarewelcome
* goodbye
    - utter_goodbye


## Generated Story -1294562172553945387
* greet
    - utter_greet
    - utter_ask_howcanhelp
* movie{"movie_language": "german"}
    - slot{"movie_language": "german"}
    - action_search_movie
    - slot{"matches": "'Animals United', 'The Baader Meinhof Complex', 'The White Ribbon', 'Metropolis', 'Downfall', 'Das Boot', 'The Wave', 'Aimee & Jaguar', 'Good Bye Lenin!', 'Soul Kitchen', 'Cargo', 'Summer Storm', 'Anatomy', 'The Lives of Others', 'The Torture Chamber of Dr. Sadism', 'Run Lola Run', 'Pandora's Box', ' and '3'"}
    - action_answer
    - action_fallout_slots
* director{"movie_language": "german"}
    - slot{"movie_language": "german"}
    - action_search_person
    - slot{"matches": "'Max F\u00e4rberb\u00f6ck', 'Reinhard Klooss', 'Dennis Gansel', 'Marco Kreuzpaintner', 'Uli Edel', 'Georg Wilhelm Pabst', 'Fatih Akin', 'Oliver Hirschbiegel', 'Wolfgang Becker', 'Fritz Lang', 'Tom Tykwer', 'Michael Haneke', 'Harald Reinl', 'Florian Henckel von Donnersmarck', 'Wolfgang Petersen', 'Stefan Ruzowitzky', ' and 'Ivan Engler'"}
    - action_answer
    - action_fallout_slots
* thankyou
    - utter_youarewelcome
* goodbye
    - utter_goodbye



## Generated Story -2456184888361863864
* movie{"movie_release_date": "2012"}
    - slot{"movie_release_date": "2012"}
    - action_search_movie
    - slot{"matches": "This are the movies I found: 'The Dark Knight Rises', and 'Shanghai Calling'"}
    - action_answer
    - action_fallout_slots
* director
    - action_search_person
    - slot{"matches": "''Vladlen Barbe', 'Dean Wright', and 'Dominic Burns'"}
    - action_answer
    - action_fallout_slots
* other
    - utter_youarewelcome
* goodbye
    - utter_goodbye


## Generated Story -3022729455999025182
* language{"movie_name": "eragon"}
    - slot{"movie_name": "eragon"}
    - action_search_movie_info
    - slot{"matches": "dummy ActionSearchMovieInfo data"}
    - action_answer
    - action_fallout_slots


## Generated Story -4332909198575793979
* greet
    - utter_greet
    - utter_ask_howcanhelp
* movie_count{"movie_name": "harry potter"}
    - slot{"movie_name": "harry potter"}
    - action_search_movie_info
    - slot{"matches": "In my database I have that there are 8 movies in the series."}
    - action_answer
    - action_fallout_slots
* language
    - action_search_movie_info
    - slot{"matches": "English"}
    - action_answer
    - action_fallout_slots
* director
    - action_search_person
    - slot{"matches": "David Yates, Mike Newell, Matt Birch, Alfonso Cuar\u00f3n, and Chris Columbus"}
    - action_answer
    - action_fallout_slots
* goodbye
    - utter_goodbye


## Generated Story -2793568108789131751
* movie_count{"movie_name": "harry potter"}
    - slot{"movie_name": "harry potter"}
    - action_search_movie_info
    - slot{"matches": "In my database I have that there are 8 movies in the series."}
    - action_answer
    - action_fallout_slots
* producer
    - action_search_movie_info
    - slot{"matches": "I'm sorry but I don't have the information to answer your question. You can find information on the producer, organization, or other, in the movie's IMDB page: 'http://www.imdb.com/title/tt0241527/?ref_=fn_tt_tt_1'"}
    - action_answer
    - action_fallout_slots
* goodbye
    - utter_goodbye


## Generated Story 7147360338074471253
* country{"movie_name": "star wars"}
    - slot{"movie_name": "star wars"}
    - action_search_movie_info
    - slot{"matches": "USA, USA, USA, USA, USA, USA, and USA"}
    - action_answer
    - action_fallout_slots
* movie_count{"movie_name": "star wars"}
    - slot{"movie_name": "star wars"}
    - action_search_movie_info
    - slot{"matches": "In my database I have that there are 8 movies in the series."}
    - action_answer
    - action_fallout_slots


## Generated Story 7833119839046042866
* movie_count{"movie_name": "harry potter"}
    - slot{"movie_name": "harry potter"}
    - action_search_movie_info
    - slot{"matches": "In my database I have that there are 8 movies in the series."}
    - action_answer
    - action_fallout_slots
* release_date
    - action_search_movie_info
    - slot{"matches": "There are multiple answers to your question: \n-> Harry Potter and the Sorcerer's Stone\u00a0: 2001 \n-> Harry Potter and the Chamber of Secrets\u00a0: 2002 \n-> Harry Potter and the Prisoner of Azkaban\u00a0: 2004 \n-> Harry Potter and the Goblet of Fire\u00a0: 2005 \n-> Harry Potter and the Order of the Phoenix\u00a0: 2007 \n-> Harry Potter and the Half-Blood Prince\u00a0: 2009 \n-> Harry Potter and the Deathly Hallows: Part I\u00a0: 2010 \n-> Harry Potter and the Deathly Hallows: Part II\u00a0: 2011 \n"}
    - action_answer
    - action_fallout_slots
* thankyou
    - utter_youarewelcome
* goodbye
    - utter_goodbye


## Generated Story 4045736408020085604
* actor_name{"character_name": "new", "movie_name": "the matrix"}
    - slot{"character_name": "new"}
    - slot{"movie_name": "the matrix"}
    - action_search_person
    - slot{"matches": "I don't have in my database the information to tell you who is the actor of 'New' in 'The Matrix' but I can tell you that these are the actors in the movie: Keanu Reeves, Marcus Chong, Gloria Foster, Essie Davis, Collin Chou, Nona Gaye, Steve Bastoni, Daniel Bernhardt,  and Helmut Bakaitis"}
    - action_answer
    - action_fallout_slots
* release_date
    - action_search_movie_info
    - slot{"matches": "There are multiple answers to your question: \n-> The Matrix\u00a0: 1999 \n-> The Matrix Revolutions\u00a0: 2003 \n-> The Matrix Reloaded\u00a0: 2003 \n"}
    - action_answer
    - action_fallout_slots


## Generated Story 5416002549668653143
* actor{"movie_name": "harry potter"}
    - slot{"movie_name": "harry potter"}
    - action_search_person
    - slot{"matches": "Daniel Radcliffe, Fiona Shaw, Verne Troyer, Daniel Radcliffe, Rupert Grint, Emma Watson, Daniel Radcliffe, Gary Oldman, Rupert Grint, Robert Pattinson, Daniel Radcliffe, Rupert Grint, Robert Pattinson, Daniel Radcliffe, Fiona Shaw, Alan Rickman, Daniel Radcliffe, Rupert Grint, Rupert Grint, Toby Jones, Alfred Enoch, Rupert Grint, Dave Legeno,  and Ralph Ineson"}
    - action_answer
    - action_fallout_slots
* movie{"movie_release_date": "1999"}
    - slot{"movie_release_date": "1999"}
    - action_search_movie
    - slot{"matches": "This are the movies I found: Wild Wild West,  and Smiling Fish & Goat on Fire"}
    - action_answer
    - action_fallout_slots
* release_date{"movie_name": "the phantom menace"}
    - slot{"movie_name": "the phantom menace"}
    - action_search_movie_info
    - slot{"matches": 1999}
    - action_answer
    - action_fallout_slots


## Generated Story -3238371752644367188
* trailer{"movie_name": "the matrix"}
    - slot{"movie_name": "the matrix"}
    - action_search_movie_info
    - slot{"matches": "You can find the trailer and other media about the movie on its IMDB page: \n-> The Matrix\u00a0: http://www.imdb.com/title/tt0133093/?ref_=fn_tt_tt_1 \n-> The Matrix Revolutions\u00a0: http://www.imdb.com/title/tt0242653/?ref_=fn_tt_tt_1 \n-> The Matrix Reloaded\u00a0: http://www.imdb.com/title/tt0234215/?ref_=fn_tt_tt_1 \n"}
    - action_answer
    - action_fallout_slots


## Generated Story -5620352289937645214
* trailer{"movie_name": "the matrix"}
    - slot{"movie_name": "the matrix"}
    - action_search_movie_info
    - slot{"matches": "I'm sorry but I don't have information on trailers. You can find the trailer and other media about the movie on its IMDB page:  \n-> The Matrix\u00a0: http://www.imdb.com/title/tt0133093/?ref_=fn_tt_tt_1 \n-> The Matrix Revolutions\u00a0: http://www.imdb.com/title/tt0242653/?ref_=fn_tt_tt_1 \n-> The Matrix Reloaded\u00a0: http://www.imdb.com/title/tt0234215/?ref_=fn_tt_tt_1 \n"}
    - action_answer
    - action_fallout_slots
* synopsis{"movie_name": "phantom menace"}
    - slot{"movie_name": "phantom menace"}
    - action_search_movie_info
    - slot{"matches": "I'm sorry but I don't have access to synopsis information on the movies. But you can find it in its IMDB page: http://www.imdb.com/title/tt0120915/?ref_=fn_tt_tt_1"}
    - action_answer
    - action_fallout_slots
* producer{"movie_name": "avatar"}
    - slot{"movie_name": "avatar"}
    - action_search_movie_info
    - slot{"matches": "I'm sorry but I don't have the information to answer your question. You can find information on the producer, organization, or other, in the movie's IMDB page: http://www.imdb.com/title/tt0499549/?ref_=fn_tt_tt_1"}
    - action_answer
    - action_fallout_slots
* other
    - utter_youarewelcome
* goodbye
    - utter_goodbye


## Generated Story 7120121686579649791
* runtime{"movie_name": "avatar"}
    - slot{"movie_name": "avatar"}
    - action_search_movie_info
    - slot{"matches": "The duration is of [178] minutes."}
    - action_answer
    - action_fallout_slots


## Generated Story 5776347583923781594
* runtime{"movie_name": "the lord of the rings"}
    - slot{"movie_name": "the lord of the rings"}
    - action_search_movie_info
    - slot{"matches": "There are multiple movies which correspond to your question. Here is a list of them and thier respective duration in minutes: \n-> The Lord of the Rings: The Fellowship of the Ring\u00a0: 171 \n-> The Lord of the Rings: The Two Towers\u00a0: 172 \n-> The Lord of the Rings: The Return of the King\u00a0: 192 \n"}
    - action_answer
    - action_fallout_slots
* thankyou
    - utter_youarewelcome
* release_date{"movie_name": "zoolander"}
    - slot{"movie_name": "zoolander"}
    - action_search_movie_info
    - slot{"matches": "There are multiple answers to your question: \n-> Zoolander\u00a0: 2001 \n-> Zoolander 2\u00a0: 2016 \n"}
    - action_answer
    - action_fallout_slots
* goodbye
    - utter_goodbye


## Generated Story -7267269106403945694
* greet
    - utter_greet
    - utter_ask_howcanhelp
* review{"movie_name": "phantom menace"}
    - slot{"movie_name": "phantom menace"}
    - action_search_movie_info
    - slot{"matches": "6.5"}
    - action_answer
    - action_fallout_slots

## Generated Story 4522370875475128248
* birth_date{"person_name": "merryl streep"}
    - slot{"person_name": "merryl streep"}
    - action_search_person_info
    - slot{"matches": "I'm sorry but I don't have any information regarding actors in my database. But you can find such information in their IMDB page! \nhttps://www.imdb.com/find?ref_=nv_sr_fn&q=merryl+streep&s=nm"}
    - action_answer
    - action_fallout_slots

## Generated Story -1971140045517603786
* review{"movie_name": "phantom menace"}
    - slot{"movie_name": "phantom menace"}
    - action_search_movie_info
    - slot{"matches": "The movie has a score of 6.5 in IMDB"}
    - action_answer
    - action_fallout_slots
* thankyou
    - utter_youarewelcome


## Generated Story -3911119172644584637
* release_date{"movie_name": "bones"}
    - slot{"movie_name": "bones"}
    - action_search_movie_info
    - slot{"matches": "There are multiple answers to your question: \n-> Bones: I don't have this information in my database\n-> The Lovely Bones: 2009\n-> The Lovely Bones: 2009\n-> The Mortal Instruments: City of Bones: 2013\n"}
    - action_answer
    - action_fallout_slots


## Generated Story -5130224722926229947
* movie_count{"movie_name": "star wars"}
    - slot{"movie_name": "star wars"}
    - action_search_movie_info
    - slot{"matches": "In my database I have that there are 8 movies in the series: \n - Star Wars: Episode VII - The Force Awakens\n - Star Wars: The Clone Wars\n - Star Wars: Episode IV - A New Hope\n - Star Wars: Episode V - The Empire Strikes Back\n - Star Wars: Episode VI - Return of the Jedi\n - Star Wars: Episode I - The Phantom Menace\n - Star Wars: Episode II - Attack of the Clones\n - Star Wars: Episode III - Revenge of the Sith"}
    - action_answer
    - action_fallout_slots


## Generated Story -1790658372827175246
* director{"movie_name": "avatar"}
    - slot{"movie_name": "avatar"}
    - action_search_person
    - slot{"matches": "James Cameron"}
    - slot{"director_name": "James Cameron"}
    - action_answer
    - action_fallout_slots
* movie
    - action_search_movie
    - slot{"matches": "This are the movies I found: The Terminator, Aliens, The Abyss, Terminator 2: Judgment Day, True Lies, Titanic,  and Avatar"}
    - action_answer
    - action_fallout_slots
    - slot{"movie_name": null}
* actor
    - action_search_person
    - slot{"matches": "Wes Studi, Tom Arnold, Paul Winfield, Joe Morton, S. Epatha Merkerson, Joel David Moore, Kate Winslet, Gloria Stuart, Michael Biehn, Jamie Lee Curtis, CCH Pounder, Jenette Goldstein, Carrie Henn, Tia Carrere, Brian Thompson, Mary Elizabeth Mastrantonio, Leonardo DiCaprio,  and Todd Graff"}
    - action_answer
    - action_fallout_slots
* director{"movie_name": "the matrix"}
    - slot{"movie_name": "the matrix"}
    - action_search_person
    - slot{"matches": "Lana Wachowski"}
    - slot{"director_name": "Lana Wachowski"}
    - action_answer
    - action_fallout_slots
* release_date{"movie_name": "the matrix"}
    - slot{"movie_name": "the matrix"}
    - action_search_movie_info
    - slot{"matches": "There are multiple answers to your question: \n-> The Matrix: 1999\n-> The Matrix Revolutions: 2003\n-> The Matrix Reloaded: 2003\n"}
    - action_answer
    - action_fallout_slots
* country{"movie_name": "the matrix"}
    - slot{"movie_name": "the matrix"}
    - action_search_movie_info
    - slot{"matches": "There are multiple answers to your question: \n-> The Matrix: USA\n-> The Matrix Revolutions: Australia\n-> The Matrix Reloaded: USA\n"}
    - action_answer
    - action_fallout_slots
* genre
    - action_search_movie_info
    - slot{"matches": "There are multiple answers to your question: \n-> The Matrix: Action|Sci-Fi\n-> The Matrix Revolutions: Action|Sci-Fi\n-> The Matrix Reloaded: Action|Sci-Fi\n"}
    - action_answer
    - action_fallout_slots
    - slot{"movie_name": null}


## Generated Story -8836494575386583531
* movie{"movie_release_date": "1992"}
    - slot{"movie_release_date": "1992"}
    - action_search_movie
    - slot{"matches": "This are the movies I found: Batman Returns, Death Becomes Her, Alien 3, Patriot Games, Boomerang, A League of Their Own, Bram Stoker's Dracula, The Last of the Mohicans, Medicine Man, Memoirs of an Invisible Man, Lethal Weapon 3, Malcolm X, Hoffa, Radio Flyer, A Few Good Men, Aladdin, The Bodyguard, Home Alone 2: Lost in New York, Wayne's World, Unforgiven, Glengarry Glen Ross, The Muppet Christmas Carol, Fortress, My Cousin Vinny, Raising Cain, Army of Darkness, The Mighty Ducks, The Lawnmower Man, Howards End, Split Second, Light Sleeper, The Crying Game, Reservoir Dogs,  and El Mariachi"}
    - action_answer
    - action_fallout_slots
    - slot{"matches": null}
* director
    - action_search_person
    - slot{"matches": "Reginald Hudlin, Tim Burton, Jonathan Lynn, Danny DeVito, John McTiernan, Brian De Palma, Robert Rodriguez, Neil Jordan, Michael Mann, Robert Zemeckis, Quentin Tarantino, Stuart Gordon, Sam Raimi, Mick Jackson, Brett Leonard, Chris Columbus, Richard Donner, Clint Eastwood, James Foley, Penny Marshall, Penelope Spheeris, Ron Clements, David Fincher, Phillip Noyce, Rob Reiner, John Carpenter, Spike Lee, Brian Henson, Paul Schrader, Francis Ford Coppola, James Ivory, Stephen Herek,  and Tony Maylam"}
    - action_answer
    - action_fallout_slots
    - slot{"matches": null}
    - slot{"actor_name": null}
    - slot{"actor_nationality": null}
    - slot{"actor_type": null}
    - slot{"award_category": null}
    - slot{"award_ceremony": null}
    - slot{"character_name": null}
    - slot{"country_name": null}
    - slot{"director_name": null}
    - slot{"director_nationality": null}
    - slot{"movie_description": null}
    - slot{"movie_genre": null}
    - slot{"movie_gross_revenue": null}
    - slot{"movie_language": null}
    - slot{"movie_location": null}
    - slot{"movie_name": null}
    - slot{"movie_release_date": null}
    - slot{"movie_release_region": null}
    - slot{"movie_star_rating": null}
    - slot{"movie_subject": null}
    - slot{"person_name": null}
    - slot{"person_nationality": null}
    - slot{"producer_name": null}
    - slot{"rating_name": null}
* rating{"movie_name": "avatar"}
    - slot{"movie_name": "avatar"}
    - action_search_movie_info
    - slot{"matches": "It has a score of 7.9 in IMDB"}
    - action_answer
    - action_fallout_slots
    - slot{"matches": null}