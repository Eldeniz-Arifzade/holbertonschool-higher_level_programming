#!/usr/bin/python3
"""This module will define a function which will return attr of objects"""


def lookup(obj):
    """will return list of available attributes of obj"""
    return dir(obj)
