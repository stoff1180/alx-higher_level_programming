#!/usr/bin/python3
"""Defines a class and inherited class-check function."""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance or inherited instance of a class.

    Args:
        obj (any): Object to check.
        a_class (type): Class to match the type of obj to.
    Returns:
        If obj is an instance - True, Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
