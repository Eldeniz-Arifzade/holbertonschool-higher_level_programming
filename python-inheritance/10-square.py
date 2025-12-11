#!/usr/bin/python3
"""This module will define class Square inherited from Rectangle"""
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """Square class inherited from Rectangle"""
    def __init__(self, size):
        """Initialize the class"""
        self.integer_validator("size", size)
        self.__size = size

    def area():
        """Implement area for Square class"""
        return self.__size ** 2
