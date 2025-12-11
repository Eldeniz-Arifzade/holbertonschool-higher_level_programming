#!/usr/bin/python3
"""This module will define a class Rectangle that will inherit from BaseGeometry"""


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Initialize the class"""
        self.__width = width
        self.__height = height
        integer_validator(width)
        integer_validator(height)