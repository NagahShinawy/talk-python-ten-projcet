"""
created by Nagaj at 18/04/2021

Handle journal operations
load journals, save journal, add new journal
"""

import os
from typing import List
from projects.app4.journal import Journal


def load() -> List[str]:
    """
    if file exist , add entries to data list
    :return: list of journals
    """
    fullpath = get_full_path()
    if os.path.exists(fullpath):
        with open(fullpath, 'r') as fin:
            entries = fin.readlines()
            return entries
    return []


def save(entries: List[Journal]):
    fullpath = get_full_path()
    print(f"saving to '{fullpath}'")
    with open(fullpath, 'w') as f:
        for entry in entries:
            f.write(entry.text)


def get_full_path():
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    app_dir = os.path.join(parent_dir, 'app4')
    filepath = os.path.join(
       app_dir, "saves", "journals.txt"
    )

    fullpath = os.path.abspath(filepath)
    return fullpath
