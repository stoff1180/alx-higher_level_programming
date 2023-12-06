#!/usr/bin/python3
"""Defines class Student."""


class Student:
    """Define a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student.

        Args:
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Getting dictionary representation of a Student.

        If attrs is a list of strings, defines only those attributes
        in the list.

        Args:
            attrs (list): (Optional) Attributes to define.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
