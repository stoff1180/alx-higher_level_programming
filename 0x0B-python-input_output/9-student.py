#!/usr/bin/python3
"""Defines class Student."""


class Student:
    """Defines a student."""

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

    def to_json(self):
        """Getting dictionary representation of a Student."""
        return self.__dict__
