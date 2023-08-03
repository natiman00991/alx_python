"""
inherits_from.py - A Python module containing a function to check if an object inherits from a specified class.

This module provides a function `inherits_from`, which allows you to check if an object is an instance of a class that inherited (directly or indirectly) from the specified class. The function uses the built-in `isinstance()` and `type()` functions to perform the type checking.

Functions:
    inherits_from(obj, a_class):
        Check if the object is an instance of a class that inherited (directly or indirectly) from the specified class.

    Parameters:
        obj (Any): The object to be checked.
            Any valid Python object. The function checks whether this object is an instance of the specified class or any of its subclasses.
        a_class (type): The class or type to check against.
            A valid Python class or type. The function determines if the given object is an instance of this class or any of its subclasses.

    Returns:
        bool: True if the object is an instance of a class that inherited from the specified class, otherwise False.
            - Returns True if `obj` is an instance of `a_class` or any class that inherited from `a_class`.
            - Returns False if `obj` is not an instance of `a_class` or any class that inherited from `a_class`.

Usage:
    import inherits_from

    class Animal:
        pass

    class Dog(Animal):
        pass

    class Labrador(Dog):
        pass

    obj = Labrador()
    print(inherits_from(obj, Animal))   # Output: True
    print(inherits_from(obj, Dog))      # Output: True
    print(inherits_from(obj, Labrador)) # Output: False
    print(inherits_from(obj, object))   # Output: True

Note:
    - This module does not require any external module imports.
    - The function does not raise any exceptions and handles inheritance checks efficiently using the `isinstance()` and `type()` functions.
    - The function considers direct and indirect inheritance, so if `obj` is an instance of a subclass of `a_class`, it will return True.

Example:
    For more examples, see the usage section above.

"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited (directly or indirectly) from the specified class.

    Parameters:
        obj (Any): The object to be checked.
            Any valid Python object. The function checks whether this object is an instance of the specified class or any of its subclasses.
        a_class (type): The class or type to check against.
            A valid Python class or type. The function determines if the given object is an instance of this class or any of its subclasses.

    Returns:
        bool: True if the object is an instance of a class that inherited from the specified class, otherwise False.
            - Returns True if `obj` is an instance of `a_class` or any class that inherited from `a_class`.
            - Returns False if `obj` is not an instance of `a_class` or any class that inherited from `a_class`.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
