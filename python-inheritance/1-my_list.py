#!/usr/bin/python3
"""This module will define a class MyList which will inherit list"""


class MyList(list):
    """This class will inherit from list and define one public method"""

    def print_sorted(self):
        """print list in ascended order"""
        return sorted(self)
