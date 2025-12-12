#!/usr/bin/python3
"""Module will define a function which will return JSON representations of str"""
import json

def to_json_string(my_obj):
    """Function for finding json representation of my_obj"""
    return json.dumps(my_obj)
