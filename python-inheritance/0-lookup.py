#!/usr/bin/python3
"""Module that defines a lookup function."""


def lookup(obj):
    """Return the list of available attributes and methods of an object.

    Args:
        obj: the object to inspect.

    Returns:
        list: the attributes and methods of obj.
    """
    return dir(obj)
