#!/usr/bin/python3
"""Module that defines a LockedClass."""


class LockedClass:
    """Represents a class that only allows a first_name attribute."""
    __slots__ = ["first_name"]
