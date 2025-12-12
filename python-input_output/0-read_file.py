#!/usr/bin/python3
"""This module will define a function for reading a text file"""


def read_file(filename=""):
    """Function for reading and printing file content"""
    with open(filename, 'r', encoding='UTF8') as f:
        print(f.read(), end='')
