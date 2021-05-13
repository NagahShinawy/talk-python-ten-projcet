"""
created by Nagaj at 13/05/2021
"""
from constants import PROMPT, INVALID


def validated_cmd():
    cmd = input(PROMPT).strip().lower()
    choices = ['a', 'r', 'l', 'e']
    while cmd not in choices:
        cmd = input(INVALID.format(cmd=cmd)).strip().lower()
    return cmd