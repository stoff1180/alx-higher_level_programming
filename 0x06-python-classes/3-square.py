#!/usr/bin/python3
"""Define a Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        Raises:
            raise TypeError: if size not int
            ValueError: if size less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Area of the square.
        Return: the current area of the square.
        """
        return (self.__size * self.__size)
