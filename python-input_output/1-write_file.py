#!/usr/bin/python3
"""Module that defines a write_file function."""


def write_file(filename="", text=""):
<<<<<<< HEAD
    """Write a string to a text file (UTF8), creating or overwriting it.

    Args:
        filename (str): the path of the file to write to.
        text (str): the string to write.
=======
    """Write a string to a text file (UTF8) and return the number
    of characters written.

    Args:
        filename (str): the path of the file to write to.
        text (str): the string to write to the file.
>>>>>>> Add write_file function

    Returns:
        int: the number of characters written.
    """
<<<<<<< HEAD
    with open(filename, mode="w", encoding="utf-8") as f:
=======
    with open(filename, "w", encoding="utf-8") as f:
>>>>>>> Add write_file function
        return f.write(text)
