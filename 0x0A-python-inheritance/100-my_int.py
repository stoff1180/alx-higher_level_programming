#!/usr/bin/python3
"""Defines class MyInt that inherits from int."""


class MyInt(int):
    """Inverts integer operators == and !=."""

    def __eq__(self, value):
        """That overrides == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """That overrides != operator with == behavior."""
        return self.real == value
