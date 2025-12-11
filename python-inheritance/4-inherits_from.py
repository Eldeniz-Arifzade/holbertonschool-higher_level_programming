#!/usr/bin/python3
"""Check if class is inherited from some class"""


def inherits_from(obj, a_class):
    """Function for checking classes"""
    return isinstance(obj, a_class) and type(obj) is not a_class
