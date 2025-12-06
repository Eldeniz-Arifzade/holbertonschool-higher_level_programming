#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    return {key: a_dictionary[key] for key in a_dictionary.keys().sort()}
