"""
created by Nagaj at 12/05/2021
"""
import os
import platform
import subprocess

import cat_service
from app import print_the_header
from constants import (
    OUTPUT_FOLDER,
    CAT_NAME,
    CAT_COUNTS,
    APPNAME,
    WINDOWS,
    WINDOWS_COMMAND,
    LINUX,
    LINUX_COMMAND,
    MACOS,
    MACOS_COMMAND,
)


def get_or_create_output_folder():
    # print(os.path.dirname(__file__))  # E:/containers/learn-projects/talk-python/ten-apps/app6_cat_factory
    # cats_path = os.path.join(".", OUTPUT_FOLDER)  # .\CATS
    # cats_fullpath = os.path.abspath(
    #     cats_path)  # E:\containers\learn-projects\talk-python\ten-apps\app6_cat_factory\CATS
    cats_fullpath = os.path.join(os.getcwd(), OUTPUT_FOLDER)
    if not os.path.exists(cats_fullpath):
        print("CREATING NEW FOLDER AT '{}'".format(cats_fullpath))
        os.makedirs(OUTPUT_FOLDER)
    return cats_fullpath


def download_cats(cats_fullpath):
    for i in range(1, CAT_COUNTS + 1):
        cat_service.get_cat(cats_fullpath, CAT_NAME.format(i=i))
    print("DONE")


def display_cats(cats_folder):
    system = platform.system()
    if system not in [WINDOWS, LINUX, MACOS]:
        print(f"Don't Support Your OS '{system}'")
        return
    if system == WINDOWS:
        command = WINDOWS_COMMAND

    elif system == LINUX:
        command = LINUX_COMMAND

    elif system == MACOS:
        command = MACOS_COMMAND
    print("Displaying Cats")
    subprocess.call([command, cats_folder])


def main():
    print_the_header(APPNAME)
    cats_folder = get_or_create_output_folder()
    download_cats(cats_folder)
    display_cats(cats_folder)


if __name__ == "__main__":
    main()
