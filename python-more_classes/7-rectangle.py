#!/usr/bin/python3
"""This module will contain a class names Rectangle"""


class Rectangle:
    """This class will define a Rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize class with width and height attr"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        self.__width = new_val

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
        self.__height = new_val

    def __str__(self):
        """method for printing rectangle"""
        rect_print = ''
        if self.__width == 0 or self.__height == 0:
            return rect_print
        for i in range(self.__height):
            if i != self.__height - 1:
                rect_print += Rectangle.print_symbol * self.__width + '\n'
            else:
                rect_print += Rectangle.print_symbol * self.__width
        return rect_print

    def __repr__(self):
        """return string representation that looks like py code"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """delete rectangle object"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    def area(self):
        """Calc the area based on width and height"""
        return self.__width * self.__height

    def perimeter(self):
        """Calc the perimeter based on width and height"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
