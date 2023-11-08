#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        new_dict = {k: v for k, v in a_dictionary.items() if k != key}
        return new_dict.copy()
    return a_dictionary.copy()
