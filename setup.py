import sqlite3
import sys

from setuptools import setup

if sys.version_info < (3, 6, 0):
    sys.exit("Python 3.6+ required but lower version found. Aborted.")

DB_FILE = "weather.db"
REQS = ["click", "requests"]

"""Creates a sqlite database for storing weather data"""

cnx = sqlite3.connect(DB_FILE)
cursor = cnx.cursor()

# `if not exists` is necessary because setup.py is run twice on installation
create_table = """
create table if not exists weather
(id INTEGER PRIMARY KEY,
city TEXT,
county_code TEXT,
timestamp INTEGER,
temp REAL,
description TEXT);
"""

cursor.execute(create_table)
cursor.close()
cnx.close()

# Set up

setup(
    name="click_pkg_demo_atx_python",
    author="Chris Leonard (@cleonard)",
    author_email="ccl@chrisleonard.com",
    description="A demonstration of the Python Click package",
    entry_points="""
        [console_scripts]
        get_weather=weather_service.service:cli
     """,
    install_requires=REQS,
    version="0.0.1",
    url="https://github.com/cleonard/click_pkg_demo_atx_python",
)
