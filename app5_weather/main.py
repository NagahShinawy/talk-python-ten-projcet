"""
created by Nagaj at 10/05/2021
"""
from collections import namedtuple
from http import HTTPStatus

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
    if text:
        text = text.strip()
    return text


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
        if element == "location":
            text = find_city_and_state_from_location(element)
        report[element] = text
    return report


def find_city_and_state_from_location(loc: str):
    parts = loc.split("\n")
    return parts[0].strip() if parts else False


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
    # main()
    # # primes_with_slices()
    WeatherReport = namedtuple(
        "WeatherReport", "location, condition, temp, scale"
    )  # define class with attrs, WeatherReport is subclass of tuple, attrs is comma separated value
    egypt = WeatherReport(location="Egypt", condition="Overcast", temp="20", scale="C")  # init class values
    print(egypt)
    print(
        f"Location is: '{egypt.location}' , Condition is: '{egypt.condition}', Temp is: '{egypt.temp}', Scale is: '{egypt.scale}'"
    )
    print(f"LOCATION-TESTING: {egypt[0]}")  # you can access tuple using both index and attrs
    for value in egypt:
        print(value)

    print("#" * 100)
    t = 12, 4, "Cat", [5, 6, 7]
    print(t)  # t is tuple
    t, *others = 12, 4, "Cat", [5, 6, 7]  # using packing  (ربط) بجمع
    print(t)  # 12
    print(others)  # list of [ 4, "Cat", [5, 6, 7]]
    print(*others)  # 4 Cat [5, 6, 7]]  # using unpacking (فك الربط) بفك التجميع
    john, james, sara = ("JOHN", "JAMES", "SARA")  # using unpacking
    print(john, james, sara)
    tuple_with_one_item = 100  # this int
    print(tuple_with_one_item, type(tuple_with_one_item))
    tuple_with_one_item = 100,  # this tuple
    print(tuple_with_one_item, type(tuple_with_one_item))
    products = ("LAPTOP", "PHONE", "WATCH")
    lap, phone, watch = products  # using unpacking to back to single variables.
    print(lap)
    print("*" * 50)
    Player = namedtuple("PLayer",
                        "name, age, team")  # create Player class with attrs, Player class is subclass of tuple
    messi = Player(name="Leon Messi", age=35, team="Barca")  # create messi obj

    # you can access values by both index and attrs.
    print("Name:", messi.name, messi[0])
    print("Age:", messi.age, messi[1])
    print("Team:", messi.team, messi[2])
