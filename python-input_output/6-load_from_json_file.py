#!/usr/bin/python3
"""Module will define a function which will create object from a json file"""
import json


def load_from_json_file(filename):
    """Create object from a json file"""
    with open(filename, encoding='UTF8') as file:
        return json.loads(file.read())
