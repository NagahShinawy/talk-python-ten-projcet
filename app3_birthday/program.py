import datetime


def print_header():
    print("---------------------------")
    print("      BIRTHDAY APP")
    print("---------------------------")
    print()


def get_birthday_from_user():
    print("When were you born? ")
    year = int(input("Year [YYYY]: "))
    month = int(input("Month [MM]: "))
    day = int(input("Day [DD]: "))

    birthday = datetime.date(year, month, day)
    return birthday


def compute_days_between_dates(bday, today):
    this_year = datetime.date(today.year, bday.month, bday.day)

    dt = this_year - today
    return dt.days


def print_birthday_information(days):
    if days < 0:
        print("You had your birthday {} days ago this year.".format(-days))
    elif days > 0:
        print("Your birthday is in {} days!".format(days))
    else:
        print("Happy birthday!!!")


def main():
    print_header()
    bday = get_birthday_from_user()
    today = datetime.date.today()
    number_of_days = compute_days_between_dates(bday, today)
    print_birthday_information(number_of_days)


if __name__ == '__main__':
    main()
