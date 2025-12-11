#!/usr/bin/python3
"""This module will define a function for adding attribute too object"""


def add_attribute(obj, name, value):
    """Function for adding attribute"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
