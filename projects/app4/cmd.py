"""
created by Nagaj at 18/04/2021
"""
from projects.app4.constants import (
    INVALID__OPTION_COMMAND,
    INVALID_ACCEPT_REFUSE_COMMAND,
    ACTION_OPTIONS,
    ACCEPT_REFUSE_OPTIONS,
)


class CMD:
    COMMANDS = ACTION_OPTIONS

    def __init__(self, command):
        self.command = self.set_command(command)

    def set_command(self, command):
        while command not in self.COMMANDS:
            command = input(INVALID__OPTION_COMMAND.format(command=command))
        return command

    def __eq__(self, other):
        return self.command == other


class AcceptOrIgnore(CMD):
    COMMANDS = ACCEPT_REFUSE_OPTIONS

    def set_command(self, command):
        while command not in self.COMMANDS:
            command = input(INVALID_ACCEPT_REFUSE_COMMAND.format(command=command))
        return command
