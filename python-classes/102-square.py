#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size: the size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value: the new size.

        Raises:
            TypeError: if value is not a number.
            ValueError: if value is less than 0.
        """
        if type(value) is not int and type(value) is not float:
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size

    def __eq__(self, other):
        """Check if two squares have equal area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares have different areas."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Check if this square's area is greater than other's."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if this square's area is greater or equal to other's."""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Check if this square's area is less than other's."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if this square's area is less or equal to other's."""
        return self.area() <= other.area()
