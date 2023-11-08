#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    doubled_dict = {}
    for key, val in a_dictionary.items():
        doubled_dict[key] = val * 2
    return doubled_dict
