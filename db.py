"""Creates a sqlite database for storing weather data"""

import sqlite3
import os
import sys

DB_FILE = "weather.db"

# Confirm deletion and recreation if database already exists
if os.path.exists(DB_FILE):
    confirmation = input("Database exists? Delete and recreate? (y/n): ")
    if confirmation.lower().startswith("y"):
        db_path = os.path.join(os.getcwd(), DB_FILE)
        os.remove(db_path)
    else:
        print("Exiting.")
        sys.exit(0)

cnx = sqlite3.connect("weather.db")
cursor = cnx.cursor()

sql_table = """
create table weather
(id INTEGER PRIMARY KEY,
city TEXT,
county_code TEXT,
timestamp INTEGER,
temp REAL,
description TEXT);
"""

cursor.execute(sql_table)

cursor.close()
cnx.close()
