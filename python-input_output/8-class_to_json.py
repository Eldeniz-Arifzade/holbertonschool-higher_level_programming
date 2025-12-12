#!/usr/bin/python3
"""Class to JSON"""


def class_to_json(obj):
    """Function that will convert class to JSON"""
    return obj.__dict__
