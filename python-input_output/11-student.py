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
        dictionary_json = self.__dict__.copy()
        if attrs is not None and attrs == list(map(str, attrs)):
            for i in dictionary_json.copy():
                if i not in attrs:
                    del dictionary_json[i]
        return dictionary_json

    def reload_from_json(self, json):
        """Replace all attributes of Student instance"""
        self.__dict__ = self.to_json(json)
