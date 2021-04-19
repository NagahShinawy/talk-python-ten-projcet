"""
created by Nagaj at 18/04/2021
"""


class CMD:
    COMMANDS = {
        "a", 'l', 'x'
    }

    def __init__(self, command):
        self.command = self.set_command(command)

    def set_command(self, command):
        while command not in self.COMMANDS:
            command = input(f"Invalid <{command}> Enter Your Command a[add], l[list], x[close]")
        return command

    def __eq__(self, other):
        return self.command == other


class AcceptOrIgnore(CMD):
    COMMANDS = {
        'y', 'n'
    }

    def set_command(self, command):
        while command not in self.COMMANDS:
            command = input(f"Invalid <{command}> Enter Your Command y[yes], n[no]")
        return command
