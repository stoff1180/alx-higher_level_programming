#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """Returns a list of an object available attributes."""
    return (dir(obj))
