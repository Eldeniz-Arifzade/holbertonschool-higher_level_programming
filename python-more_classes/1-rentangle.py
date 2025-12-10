#!/usr/bin/python3
"""This module will contain a class names Rectangle"""


class Rectangle:
    """This class will define a Rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize class with width and height attr"""
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """retrieve width"""
        return self.__width

    @width.setter
    def width(self, new_val):
        """set width"""
        if not isinstance(new_val, int):
            raise TypeError('width must be an integer')
        elif new_val < 0:
            raise ValueError('width must be >= 0')

    @property
    def height(self):
        """retrieve height"""
        return self.__height

    @height.setter
    def height(self, new_val):
        """set height"""
        if not isinstance(new_val, int):
            raise TypeError('height must be an integer')
        elif new_val < 0:
            raise ValueError('height must be >= 0')
