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

# Checking existence of given keys one by one. We'll break out of the loop \
# if one of the keys does not exist
ISPASSED = False
for i in settings_data:
    ISPASSED = False
    for j in response:
        if i in j.keys():
            ISPASSED = True
    if not ISPASSED:
        break

# if all the keys exist print passed otherwise print failed
if ISPASSED:
    print("Passed")
else:
    print("Failed")
