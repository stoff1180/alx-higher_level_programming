#!/usr/bin/python3
"""Defines a class-check function."""


def is_same_class(obj, a_class):
    """Check if an object is an instance of a given class.

    Args:
        obj (any): Object to check.
        a_class (type): Class to match the type of obj to.
    Returns:
        If obj an instance of class - True, Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
