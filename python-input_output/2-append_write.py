#!/usr/bin/python3
"""This module will define a function which will append to a file"""


def write_file(filename="", text=""):
    """Function will append text to file, and return num of chars written"""
    with open(filename, 'a', encoding='UTF8') as f:
        return f.write(text)
