"""
created by Nagaj at 10/05/2021
"""
import re


def print_the_header():
    print("-" * 70)
    print(" " * 30 + "WEATHER APP")
    print("-" * 70)


def get_zipcode_from_user():
    zipcode = input("Type Zipcode which you want weather for (97201)? ")
    while not validate_zipcode(zipcode):
        zipcode = input(f"Invalid zipcode '{zipcode}'. Type Again? ")
    return zipcode


def validate_zipcode(zipcode):
    codes = re.findall(r"^[0-9]{5}(?:-[0-9]{4})?$", zipcode)
    return True if codes else False


def main():
    print_the_header()
    # todo : get the zipcode from user
    get_zipcode_from_user()
    # todo : get html from web
    # todo: parse the html
    # todo: display for the forecast.


if __name__ == "__main__":
    main()
