"""Click cli command to get weather from an API by and store weather-related
data in a database.
"""

import os
import sqlite3
from textwrap import dedent

import click
import requests

# Get api key from environment variable
API_KEY = os.environ.get("WEATHERBIT_API_KEY")
if not API_KEY:
    msg = "Can't find an api key set in environment variables."
    raise RuntimeError(msg)


def get_weather(city, units, lang):
    """API request to get current weather"""
    base_url = "https://api.weatherbit.io/v2.0/current?"
    querystring = f"key={API_KEY}&lang={lang}&city={city}&units={units}"
    url = base_url + querystring
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    else:
        return r.text


def log_weather(weather_data):
    """Log the full json respose to a file"""

    cnx = sqlite3.connect("weather.db")
    cursor = cnx.cursor()

    sql_insert = """
    insert into weather
    (city, county_code, timestamp, temp, description)
    values
    (?, ?, ?, ?, ?);
    """
    data = (
        weather_data["city_name"],
        weather_data["country_code"],
        weather_data["ts"],
        weather_data["temp"],
        weather_data["weather"]["description"],
    )
    cursor.execute(sql_insert, data)
    cnx.commit()

    cursor.close()
    cnx.close()


@click.command()
@click.option(
    "--city",
    "-c",
    default="Austin,TX",
    help=dedent(
        """
    The location for which to get current weather. Should be in the format:
    {city},{state code},{country code} (i.e Austin,tx,us or Austin,tx).
    Defaults to "Austin,TX".
    """.strip()
    ),
)
@click.option(
    "--units",
    "-u",
    default="I",
    help=dedent(
        """Units for results:
        M - Metric (Celcius, m/s, mm)
        S - Scientific (Kelvin, m/s, mm)
        I - Fahrenheit (F, mph, in)
        Defaults to "I" for Fahrenheit.
        """
    ),
)
@click.option(
    "--language",
    "--lang",
    "-l",
    default="en",
    help=dedent(
        """
    The ISO language code for desired language.
    Defaults to "en" for English.
    """
    ),
)
def cli(city, units, language):
    weather = get_weather(city, units, language)["data"][0]
    log_weather(weather)
    output = 'The weather in {}, {} is "{}" with a temp of {}.'.format(
        weather["city_name"],
        weather["country_code"],
        weather["weather"]["description"],
        weather["temp"],
    )
    click.echo(output)


if __name__ == "__main__":
    cli()
