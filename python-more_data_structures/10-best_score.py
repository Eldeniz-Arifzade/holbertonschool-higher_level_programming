#!/usr/bin/python3
def best_score(a_dictionary):
    sorted_keys = sorted(a_dictionary)
    if len(sorted_keys) == 0:
        return None
    return sorted_keys[-1]
