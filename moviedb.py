import sqlite3
import os

conn = sqlite3.connect('data/db/movie.db')


def _build_basic_query_where(slots):
    """
    Build the "where" part of a query by looking at the available slots
    """
    # mappings from slot name to column name in DB
    mappings = {
        "actor_name": "actors",
        "country_name": "country",
        "director_name": "director",
        "movie_description": "plot_keywords",
        "movie_genre": "genres",
        "movie_gross_revenue": "gross",
        "movie_language": "language",
        "movie_location": "country",
        "movie_name": "title",
        "movie_release_date": "year",
        "movie_release_region": "country",
        "movie_star_rating": "imdb_score",
        "movie_subject": "plot_keywords",
        "person_name": "actors",
    }

    # replace every space with at least one character followed by
    # multiple characters
    def preprocess_slot_value(x): return x.replace(" ", "_%")

    query = ""

    # available slots
    av_slots = [x for x in slots.keys() if x in mappings.keys()]

    if len(av_slots) > 0:
        for slt in av_slots:
            query += f" {mappings[slt]} like " + \
                f"\"%{preprocess_slot_value(slots[slt])}%\" and "

        query = " where " + query[:-4]  # remove the last "and"

    return query 


def make_search_on_slots(slots, column="*", extra_where="", order_by="year"):
    c = conn.cursor()

    basic_where = _build_basic_query_where(slots) 

    if basic_where == "" and extra_where != "":
        basic_where = " where "

    query = f"select {column} from movie {basic_where} {extra_where} order by {order_by}"
    cursor = conn.execute(query)

    data = [[str(itm).strip() if itm != "" else "I don't have this information in my database" for itm in row]
                for row in cursor.fetchall()]

    cursor.close()

    return data
