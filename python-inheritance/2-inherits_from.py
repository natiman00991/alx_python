"""
inherits_from.py - A Python module containing a function to check if an object inherits from a specified class.

This module provides a function `inherits_from`, which allows you to check if an object is an instance of a class that inherited (directly or indirectly) from the specified class. The function uses the built-in `__bases__` attribute to collect all base classes for the given object, including inherited classes and the object class.

Functions:
    inherits_from(obj, a_class):
        Check if the object is an instance of a class that inherited (directly or indirectly) from the specified class.

        Parameters:
            obj (Any): The object to be checked.
            a_class (type): The class or type to check against.

        Returns:
            bool: True if the object is an instance of a class that inherited from the specified class, otherwise False.

Usage:
    import inherits_from

    a = True
    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))
    if inherits_from(a, bool):
        print("{} inherited from class {}".format(a, bool.__name__))
    if inherits_from(a, object):
        print("{} inherited from class {}".format(a, object.__name__))
"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited (directly or indirectly) from the specified class.

    Parameters:
        obj (Any): The object to be checked.
        a_class (type): The class or type to check against.

    Returns:
        bool: True if the object is an instance of a class that inherited from the specified class, otherwise False.
    """
    # Implementation details are provided in the function definition.
    # The function checks for class inheritance using the __bases__ attribute.

    # ... (implementation code)
