"""
Handle journal operations
load journals, save journal, add new journal
"""
import os
from typing import List


def load(name: str) -> List[str]:
    """
    if file exist , add entries to data list
    :param name: filename of journal with no extension
    :return: list of journals
    """
    fullpath = get_full_path(name)
    data = []
    if os.path.exists(fullpath):
        with open(fullpath, "r") as fin:
            entries = fin.readlines()

            for entry in entries:
                data.append(entry)
            data.append("#" * 30 + "\n")
    return data


def save(name: str, journal_data: List[str]):
    fullpath = get_full_path(name)
    print(f"saving to '{fullpath}'")
    with open(fullpath, "w") as f:
        for journal in journal_data:
            f.write(journal)


def get_full_path(name):
    filepath = os.path.join(
        "journals", name + ".txt"
    )  # relative path  (journal/default.xtx)

    fullpath = os.path.abspath(filepath)  # full path : absolute path just like linux
    return fullpath


def add_entry(text: str, journal_date: list):
    journal_date.append(text)


print("__name__", __name__)
print("__file__", __file__)
