"""
created by Nagaj at 10/05/2021
"""
from http import HTTPStatus
from collections import namedtuple
import requests
from bs4 import BeautifulSoup

from constants import (
    WEATHER_ENDPOINT,
    LOCATION_CSS,
    WEATHER_SCALE_CSS,
    WEATHER_CONDITION_CSS,
    WEATHER_TEMP_CSS,
)
from validations import validate_zipcode


def print_the_header():
    print("-" * 70)
    print(" " * 30 + "WEATHER APP")
    print("-" * 70)


def get_zipcode_from_user():
    zipcode = input("Type Zipcode you want weather for (97201)? ")
    while not validate_zipcode(zipcode):
        zipcode = input(f"Invalid zipcode '{zipcode}'. Type Again? ")
    return zipcode


def get_html_from_web(validated_zipcode):
    weather_endpoint = WEATHER_ENDPOINT.format(zipcode=validated_zipcode)
    response = requests.get(weather_endpoint)
    if response.status_code != HTTPStatus.OK:
        return False
    return response.text


def clean_up(text: str):
    if not text:
        return text
    return text.strip()


def get_weather_from_html(html):
    soup = BeautifulSoup(html, "html.parser")
    # print(soup)
    elements = {
        "location": LOCATION_CSS,
        "condition": WEATHER_CONDITION_CSS,
        "temp": WEATHER_TEMP_CSS,
        "scale": WEATHER_SCALE_CSS,
    }
    report = dict()
    for element in elements:
        elm = soup.find(element)
        if elm is not None:
            text = elm.get_text()
        else:
            text = element + "-value"
        clean_up(text)
        report[element] = text
    return report


def main():
    print_the_header()
    validated_zipcode = get_zipcode_from_user()
    html = get_html_from_web(validated_zipcode)
    if html is not False:
        report = get_weather_from_html(html)
        print(
            f"Location is: '{report['location']}' , Condition is: '{report['condition']}', Temp is: '{report['temp']}',"
            f" Scale is: '{report['scale']}'"
        )

    else:
        print("SOMETHING WENT WRONG, TRY PLEASE TRY AGAIN.")


def primes_with_slices():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    #         0  1  2  3  4   5   6   7  8
    first_prime = primes[0]  # 2
    print(first_prime)
    last_prime = primes[-1]  # 23
    print(last_prime)
    lowest_four = primes[0:4]  # 2,3, 5, 7
    print(lowest_four)
    lowest_four = primes[:4]  # 2, 3, 5, 7
    print(lowest_four)
    middle = primes[3:6]  # 7, 11, 13
    print(middle)
    last_4 = primes[-4:]  # 13, 17, 19, 23
    print(last_4)


if __name__ == "__main__":
    main()
    # # primes_with_slices()
    WeatherReport = namedtuple(
        "WeatherReport", "location, condition, temp, scale"
    )  # define class with attrs
    egypt = WeatherReport("Egypt", "Overcast", "20", "C")  # init class values
    print(egypt)
    print(
        f"Location is: '{egypt.location}' , Condition is: '{egypt.condition}', Temp is: '{egypt.temp}', Scale is: '{egypt.scale}'"
    )
    for value in egypt:
        print(value)
