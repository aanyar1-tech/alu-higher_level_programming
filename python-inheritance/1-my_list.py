#!/usr/bin/python3
"""Module that defines a MyList class."""


class MyList(list):
    """Represents a list that can print itself sorted."""

    def print_sorted(self):
        """Print the list, sorted in ascending order."""
        print(sorted(self))
