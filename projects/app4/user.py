"""
created by Nagaj at 18/04/2021
"""
from projects.app4.cmd import CMD, AcceptOrIgnore
from projects.app4.constants import (
    CLOSE,
    ADD,
    LIST,
    ACCEPT,
    BASIC_MSG,
    HTML_MSG,
    JSON_MSG,
    ENTER_TEXT,
    NO_ITEMS_TO_SHOW,
    BYE
)
from projects.app4.db import load, save, to_html, to_json
from projects.app4.journal import Journal


class User:
    def __init__(self):
        self.entries = []

    def add_entry(self) -> None:
        text = input(ENTER_TEXT)
        journal = Journal(text)
        self.entries.append(journal.text + "\n")

    def show_entries(self) -> None:
        if self.entries:
            for start, entry in enumerate(self.entries, start=1):
                print(start, entry)
        else:
            print(NO_ITEMS_TO_SHOW)

    def event_loop(self) -> None:
        command = self.run_command()
        self.entries = load()
        while command != CLOSE:

            if command == ADD:
                self.add_entry()

            if command == LIST:
                self.show_entries()

            command = self.run_command()

        save(self.entries)

        if self.accept_export(HTML_MSG) == ACCEPT:
            to_html(self.entries)

        if self.accept_export(JSON_MSG) == ACCEPT:
            to_json(self.entries)

        print(BYE)

    @staticmethod
    def accept_export(msg):
        return AcceptOrIgnore(input(msg))

    @staticmethod
    def run_command(msg=BASIC_MSG):
        command = input(msg)
        cmd = CMD(command)
        return cmd
