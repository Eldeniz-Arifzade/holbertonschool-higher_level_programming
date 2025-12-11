#!/usr/bin/python3
"""This module will define empty class"""


class BaseGeometry:
    """Define the geometry with one method class"""
    def area(self):
        """Function for calculating area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is bool or not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
