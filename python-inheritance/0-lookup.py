#!/usr/bin/python3
"""This module will define a function which will return attr of objects"""


def lookup(obj):
    return list(obj.__dict__.keys())
