#!/usr/bin/python3
"""Module that defines a to_json_string function."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of an object (string).

    Args:
        my_obj: the object to serialize.

    Returns:
        str: the JSON string representation of my_obj.
    """
    return json.dumps(my_obj)
