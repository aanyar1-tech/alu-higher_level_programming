#!/usr/bin/python3
"""Module that defines an inherits_from function."""


def inherits_from(obj, a_class):
    """Check if obj's class inherited from a_class, directly or indirectly.

    Args:
        obj: the object to check.
        a_class: the class to compare against.

    Returns:
        bool: True if obj is an instance of a class that inherits from
            a_class, but is not exactly a_class itself, False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
