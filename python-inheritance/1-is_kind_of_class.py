"""
my_module.py - A Python module containing utility functions for type checking.

This module provides a single function, `is_kind_of_class`, which allows you to check if an object is an instance of a specified class or any of its subclasses. The function uses the built-in `isinstance()` function to perform the type check.

Functions:
    is_kind_of_class(obj, a_class):
        Check if the object is an instance of, or if the object is an instance of a class that inherited from,
        the specified class.

        Parameters:
            obj (Any): The object to be checked.
            a_class (type): The class or type to check against.

        Returns:
            bool: True if the object is an instance of the specified class or any of its subclasses, otherwise False.

Usage:
    import my_module

    result = my_module.is_kind_of_class(42, int)
    print(result)  # Output: True

    result = my_module.is_kind_of_class(3.14, int)
    print(result)  # Output: False
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or if the object is an instance of a class that inherited from,
    the specified class.

    Parameters:
        obj (Any): The object to be checked.
        a_class (type): The class or type to check against.

    Returns:
        bool: True if the object is an instance of the specified class or any of its subclasses, otherwise False.
    """
    return isinstance(obj, a_class)
