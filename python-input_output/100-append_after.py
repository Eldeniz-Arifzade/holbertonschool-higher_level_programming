#!/usr/bin/python3
"""This module will define a function for update and searching files"""


def append_after(filename="", search_string="", new_string=""):
    """Function that inserts new_string after search_string"""
    with open(filename, 'r+', encoding='UTF8') as file:
        list_of_lines = file.readlines()
        new_list_of_lines = []
        for line in list_of_lines:
            new_list_of_lines.append(line)
            if search_string in line:
                new_list_of_lines.append(new_string)
        file.seek(0)
        file.write(''.join(new_list_of_lines))
