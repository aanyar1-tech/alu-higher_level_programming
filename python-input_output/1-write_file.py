#!/usr/bin/python3
"""Module that defines a write_file function."""


def write_file(filename="", text=""):
    """Write a string to a text file (UTF8), creating or overwriting it.

    Args:
        filename (str): the path of the file to write to.
        text (str): the string to write.

    Returns:
        int: the number of characters written.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
