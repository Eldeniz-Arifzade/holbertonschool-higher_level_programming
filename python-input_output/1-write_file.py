#!/usr/bin/python3
"""Write to a file function"""


def write_file(filename="", text=""):
    """Function will write text to file, and return num of chars written"""
    with open(filename, 'w', encoding='UTF8') as f:
        return(f.write(text))
