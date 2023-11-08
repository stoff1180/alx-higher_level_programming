#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max val = 0
    max key = None
    for k, v in a_dictionary.items():
        if v > max val:
            max val = v
            max key = k
        return max key
