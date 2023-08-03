"""
0-is_same_class

This module contains a single function 'is_same_class' that checks if an object is exactly an instance of the specified class.

Functions:
    is_same_class(obj, a_class): Returns True if the object is exactly an instance of the specified class; otherwise, False.

"""


def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    Args:
        obj (object): The object to be checked.
        a_class (type): The specified class to compare against.

    Returns:
        bool: True if the object is exactly an instance of the specified class; otherwise, False.
    """
    return obj.__class__ is a_class
