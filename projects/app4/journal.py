"""
created by Nagaj at 18/04/2021
"""


class Journal:
    entries = []

    def __init__(self, text: str):
        self.text = text

    def __str__(self):
        return self.text
