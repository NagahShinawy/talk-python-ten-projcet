"""
created by Nagaj at 10/05/2021
"""
from http import HTTPStatus

import requests

from constants import WEATHER_ENDPOINT
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


def main():
    print_the_header()
    validated_zipcode = get_zipcode_from_user()
    html = get_html_from_web(validated_zipcode)


if __name__ == "__main__":
    # main()
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
