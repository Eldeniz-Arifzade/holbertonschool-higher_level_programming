#!/usr/bin/python3
"""This module will define a function from json to str"""
import json


def from_json_string(my_str):
    """Function that converts json to str and returns it"""
    return json.loads(my_str)
