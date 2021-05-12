"""
created by Nagaj at 12/05/2021
"""
import os
from http import HTTPStatus

import requests

from constants import CATS_URL, DOWNLOAD


def get_cat(folder, catname):
    data = get_data_from_url(CATS_URL)
    if data is not None:
        save_image(folder, catname, data)


def get_data_from_url(url):
    # USING stream=True
    # look instructor code at (https://github.com/mikeckennedy/python-jumpstart-course-demos/blob/master/apps/
    # 06_lolcat_factory/final/cat_service.py)
    response = requests.get(url)
    if response.status_code != HTTPStatus.OK:
        return None
    return response.content


def save_image(folder, catname, data):
    single_catpath = os.path.join(folder, catname + ".jpg")
    if not os.path.isfile(single_catpath):
        with open(single_catpath, "wb") as f:
            f.write(data)
            print(DOWNLOAD.format(catname))
