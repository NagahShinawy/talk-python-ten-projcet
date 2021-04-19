"""
created by Nagaj at 18/04/2021

Handle journal operations
load journals, save journal, add new journal
"""

import os
from typing import List

import jinja2


def load() -> List[str]:
    """
    if file exist , add entries to data list
    :return: list of journals
    """
    data = []
    fullpath = get_full_path()
    if os.path.exists(fullpath):
        with open(fullpath, 'r') as fin:
            entries = fin.readlines()
            for entry in entries:
                data.append(entry)
            entries.append("#" * 30 + '\n')
    return data


def save(entries: List[str]):
    fullpath = get_full_path()
    print(f"saving to '{fullpath}'")
    with open(fullpath, 'w') as f:
        for entry in entries:
            f.write(entry)
        f.write("#" * 50 + '\n')


def to_html(entries):
    saves_path = os.path.dirname(get_full_path())
    html_path = os.path.join(saves_path, '_home.html')
    with open(html_path, 'r') as htmlfile:
        content = htmlfile.read()
    template = jinja2.Template(content)
    home = template.render(title='All Journals', entries=entries)
    with open(os.path.join(saves_path, 'home.html'), 'w') as f:
        f.write(home)


def get_full_path():
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    app_dir = os.path.join(parent_dir, 'app4')
    filepath = os.path.join(
        app_dir, "saves", "journals.txt"
    )

    fullpath = os.path.abspath(filepath)
    return fullpath
