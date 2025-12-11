#!/usr/bin/python3
"""This module fill define MyInt class inherited fron int"""


class MyInt(int):
    """Rebel class"""
    def __init__(self, value):
        """Initialize class"""
        self.value = value

    def __eq__(self, other):
        """Replace with !="""
        return self.value != other

    def __ne__(self, other):
        """Replace with =="""
        return self.value == other
