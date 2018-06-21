import sqlite3
import os

if "movie.db" in os.listdir("../db/"):
    os.remove("../db/movie.db")

conn = sqlite3.connect('../db/movie.db')
c = conn.cursor()

c.executescript(open("../db/moviedb.sql", "r", encoding="utf-8").read())

conn.commit()

conn.close()