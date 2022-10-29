""" API Testing with Python """

import os
import json
import requests


def load_settings():
    """Returns a JSON file as a Python object"""
    if not os.path.exists("settings.json"):
        raise Exception('File at settings.json does not exist')
    with open("settings.json", encoding="utf-8") as data:
        return json.load(data)


# Stores the data from settings.json file as a list
settings_data = load_settings()
# URL input
url = input("Input the URL: ")

# Inform the user that we are waiting for a response from the URL
print("Waiting for a response from: ", url)

# Keeps the requested info
response = requests.get(url, timeout=10).json()


def data_check():
    """Checking the test is passed or not"""

    is_passed = True

    # Checking existence of given keys one by one. We'll break out of the loop \
    # if one of the keys does not exist
    for value in response:
        is_passed = True
        for key1, value1 in settings_data.items():
            if key1 not in value.keys():
                is_passed = False
                return "Failed : Unmatched key found"
            if not isinstance(value1[0], type(value[key1])):
                is_passed = False
                return 'Failed : Unmatched data types found'
            if value1[1]:
                if isinstance(value[key1], int):
                    if not value1[1][0] <= value[key1] <= value1[1][1]:
                        is_passed = False
                        return "Failed : value is outside the expected range"
                if isinstance(value[key1], str):
                    if not value1[1][0] <= len(value[key1]) <= value1[1][1]:
                        is_passed = False
                        return "Failed : value length is outside the expected range"

    if is_passed:
        return "Passed"


print(data_check())
