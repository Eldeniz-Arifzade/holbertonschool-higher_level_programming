#!/usr/bin/python3
def best_score(a_dictionary):
    keys, values = a_dictionary.items()
    if len(keys) == 0:
        return None
    return key[values.index(max(values))]
