"""
created by Nagaj at 18/04/2021
"""
from projects.app4.cmd import CMD, AcceptOrIgnore
from projects.app4.constants import CLOSE, ADD, LIST, ACCEPT
from projects.app4.db import load, save, to_html
from projects.app4.journal import Journal


class User:
    def __init__(self):
        self.entries = []

    def add_entry(self) -> None:
        text = input("Enter Your Text: ")
        journal = Journal(text)
        self.entries.append(journal.text + "\n")

    def show_entries(self) -> None:
        if self.entries:
            for start, entry in enumerate(self.entries, start=1):
                print(start, entry)
        else:
            print("No Items")

    def event_loop(self):
        command = self.run_command()
        self.entries = load()
        while command != CLOSE:

            if command == ADD:
                self.add_entry()

            if command == LIST:
                self.show_entries()

            command = self.run_command()

        save(self.entries)
        is_accepted = AcceptOrIgnore(input("Do you want to export to html ? y[yes], n[no]"))
        if is_accepted == ACCEPT:
            to_html(self.entries)
        print("Done. Goodbye")

    @staticmethod
    def run_command():
        command = input("Enter Your Command a[add], l[list], x[close]")
        cmd = CMD(command)
        return cmd.command
