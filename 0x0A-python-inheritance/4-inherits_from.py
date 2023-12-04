#!/usr/bin/python3
"""Defines an inherited class-check function."""


def inherits_from(obj, a_class):
    """Check if an object is inherited instance of a class.

    Args:
        obj (any): Object to check.
        a_class (type): Class to match the type of obj to.
    Returns:
        If obj is an inherited - True, Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
