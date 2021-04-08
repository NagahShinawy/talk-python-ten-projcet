import os
from app import app
import random
BASEDIR = os.getcwd().split("\\")[-1]


def user_number():
    return int(input("Enter Number between 1 to 100"))


def computer_number():
    return random.randint(1, 100)


def main():
    user_num = user_number()
    while user_num not in range(1, 101):
        user_num = user_number()

    computer_num = computer_number()
    while user_num != computer_num:
        if user_num > computer_num:
            print("You Number is HIGHER than computer number")
        else:
            print("You Number is LOWER than computer number")
        user_num = user_number()


if __name__ == '__main__':
    app(BASEDIR)
    main()