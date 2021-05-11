"""
created by Nagaj at 10/05/2021
"""
import re


def validate_zipcode(zipcode):
    codes = re.findall(r"^[0-9]{5}(?:-[0-9]{4})?$", zipcode)
    return True if codes else False
