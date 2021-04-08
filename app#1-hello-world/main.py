import os
import re
from app import app
BASEDIR = os.getcwd().split("\\")[-1]


def get_username():
    return input("What is Your Name? ")


def validate_username(username):
    if not username:
        raise ValueError("username can not be empty.")
    matches = re.findall(r'^[a-zA-Z]+$', username)
    if matches:
        return matches[0]
    raise ValueError(f"Invalid username <{username}>. no numbers, symbols")


def welcome(username):
    return f"Welcome {username.title()}!"


def main():
    username = get_username()
    validated = validate_username(username)
    print(welcome(validated))


if __name__ == '__main__':
    app(BASEDIR)
    main()