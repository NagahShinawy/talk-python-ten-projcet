"""
created by Nagaj at 18/04/2021
"""
from projects.app4.cmd import CMD
from projects.app4.db import load, save
from projects.app4.journal import Journal


class User:
    def __init__(self):
        self.entries = []

    def add_entry(self) -> None:
        text = input("Enter Your Text: ")
        journal = Journal(text)
        self.entries.append(journal)

    def show_entries(self) -> None:
        if self.entries:
            for start, entry in enumerate(self.entries, start=1):
                print(start, entry)
        else:
            print("No Items")

    def event_loop(self):
        command = self.run_command()
        entries = load()
        if entries:
            self.entries.extend(entries)
        while command != 'x':

            if command == 'a':
                self.add_entry()

            if command == 'l':
                self.show_entries()

            command = self.run_command()

        save(self.entries)
        print("Done. Goodbye")

    @staticmethod
    def run_command():
        command = input("Enter Your Command a[add], l[list], x[close]")
        cmd = CMD(command)
        return cmd.command
