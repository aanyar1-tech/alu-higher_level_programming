#!/usr/bin/python3
"""Module that defines a MyInt class."""


class MyInt(int):
    """Represents an integer with inverted == and != operators."""

    def __eq__(self, value):
        """Return the inverted result of the equality comparison."""
        return int(self) != value

    def __ne__(self, value):
        """Return the inverted result of the inequality comparison."""
        return int(self) == value
