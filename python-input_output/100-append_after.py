#!/usr/bin/python3
"""This module will define a function for update and searching files"""


def append_after(filename="", search_string="", new_string=""):
    """Function that inserts new_string after search_string"""
    with open(filename, 'a', encoding='UTF8') as file:
        for line in file:
            if search_string in line:
                file.write(new_string)
