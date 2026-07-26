#!/usr/bin/python3
"""Defines the BaseGeometry class."""


class BaseGeometry:
    """Base class for geometry objects."""

    def area(self):
        """Raise an Exception since area() is not implemented here."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name="name", value=None):
        """Validate that value is an integer greater than 0.

        Args:
            name (str): the name of the attribute being validated.
            value: the value to validate.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
