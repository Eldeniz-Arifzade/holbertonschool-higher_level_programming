#!/usr/bin/python3
"""Module will define a function which will save object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """Function which will save my_obj to filename"""
    with open(filename, 'a', encoding='UTF8') as file:
        file.write(json.dumps(my_obj))
