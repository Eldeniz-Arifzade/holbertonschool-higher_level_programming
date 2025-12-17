#!/usr/bin/python3
import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}\nIs Student: {self.is_student}")

    def serialize(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.__dict__.copy(), file)

    @classmethod
    def deserialize(cls, filename):
        with open(filename, 'rb') as file:
            try:
                data = pickle.load(file)
                obj = cls.__new__(cls)
                obj.__dict__.update(data)
                return obj
            except Exception:
                return None
