#!/usr/bin/python3
"""Defines square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes new Square.

        Args:
            size (int): Size of the new Square.
            x (int): Coordinate x for the new Square.
            y (int): Coordinate y for the new Square.
            id (int): Identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter the square size."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the Square.

        Args:
            *args (ints): New attribute values.
                - 1st argument defines id attribute
                - 2nd argument defines size attribute
                - 3rd argument defines x attribute
                - 4th argument defines y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Returns a dictionary represents of a Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Returns a print() and str() represent of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
