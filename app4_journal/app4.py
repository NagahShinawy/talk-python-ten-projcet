import os
import journal
from app import app

BASEDIR = os.getcwd().split("\\")[-1]


def run_event_loop():
    print("What do you want to do with your journal ?")
    journal_name = "default"
    journal_data = journal.load(journal_name)
    command = None
    count_journals = 1
    while command != "x":
        command = input("[L]ist entries [A]dd an entry, E[x]it: ").lower().strip()
        if command == "":
            print("Can not be empty")
            continue
        if command == "l":
            list_entries(journal_data)
        elif command == "a":
            add_entry(count_journals, journal_data)
            count_journals += 1
        elif command != "x":
            print("Sorry , we don't understand your choice '{}'".format(command))
    print("Done, Good Bye")
    journal.save(journal_name, journal_data)


def list_entries(data: list):
    if data:

        print("Your have <{}> entries".format(len(data)))
        latest = data[::-1]
        for counter, entry in enumerate(latest, start=1):
            print(f"* [{counter}]-{entry}")
    else:
        print("You have no entries . Type <a> to add")


def add_entry(count_journals, data: list):
    text = input("Type Your entry. <enter> to exit")
    # data.append(text)
    text = f"[*][{count_journals}]-{text}\n"
    journal.add_entry(text, data)
    print("Entry Added Successfully")


def main():
    run_event_loop()


def find(arr, k):
    return "Yes" if k in arr else "No"


if __name__ == "__main__":
    app(BASEDIR)
    main()
    # print(find([2, 3, 1], 1))
