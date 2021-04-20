"""
created by Nagaj at 18/04/2021
"""
from projects.app4.cmd import CMD, AcceptOrIgnore
from projects.app4.constants import (
    CLOSE,
    ADD,
    LIST,
    ACCEPT,
    OPENING_MSG,
    HTML_MSG,
    JSON_MSG,
    ENTER_TEXT,
    NO_ITEMS_TO_SHOW,
    BYE,
)
from projects.app4.db import load, save, to_html, to_json
from projects.app4.journal import Journal


class User:
    """
    user actions add, list, exist
    """

    def __init__(self):
        self.entries = []

    def add_entry(self) -> None:
        """

        :return:
        """
        text = input(ENTER_TEXT)
        journal = Journal(text)
        self.entries.append(journal.text + "\n")

    def show_entries(self) -> None:
        """

        :return:
        """
        if self.entries:
            for start, entry in enumerate(self.entries[::-1], start=1):
                print(start, entry)
        else:
            print(NO_ITEMS_TO_SHOW)

    def event_loop(self) -> None:
        """

        :return:
        """
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
        """

        :param msg:
        :return:
        """
        return AcceptOrIgnore(input(msg))

    @staticmethod
    def run_command(opening_msg=OPENING_MSG):
        """

        :param opening_msg:
        :return:
        """
        command = input(opening_msg)
        cmd = CMD(command)
        return cmd
