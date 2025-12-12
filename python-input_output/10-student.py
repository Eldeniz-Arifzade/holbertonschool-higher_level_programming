#!/usr/bin/python3
"""This module will define a Student class"""


class Student:
    """Student class with 3 fields and 1 method"""
    def __init__(self, first_name, last_name, age):
        """Initializa the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of the student instance"""
        dictionary_json = self.__dict__
        if attrs != None and attrs == list(map(str, attrs)):
            for i in attrs:
                if i not in dictionary_json:
                    del dictionary_json[i]
        return dictionary_json
