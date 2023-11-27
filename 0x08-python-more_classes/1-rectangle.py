#!/usr/bin/python3
"""Represents a Rectangle class."""


class Rectangle:
    """Defines a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): Width of the new rectangle.
            height (int): Height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the private instance attribute width."""
        return self.__width

    @width.setter
    def width(self, value):
        """set the private instance attribute width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter the private instance attribute height."""
        return self.__height

    @height.setter
    def height(self, value):
        """setter the private instance attribute height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
