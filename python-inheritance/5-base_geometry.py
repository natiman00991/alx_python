"""
5-base_geometry.py - A Python module defining the BaseGeometry class with validation methods.

This module defines the `BaseGeometry` class, which serves as a base class with methods for validating integer values and an abstract `area()` method. It allows other classes to inherit from it and provides a foundation for building more complex classes.

Classes:
    BaseGeometry:
        A base class with methods to validate integer values and an abstract area method.

Methods:
    area(self):
        Raise an Exception with the message "area() is not implemented".
    integer_validator(self, name, value):
        Validate an integer value.

Usage:
    import 5-base_geometry

    class DerivedClass(5-base_geometry.BaseGeometry):
        def area(self):
            # Custom implementation of the area method for DerivedClass

    obj = DerivedClass()
    obj.integer_validator("my_int", 12)
    obj.integer_validator("width", 89)

    try:
        obj.integer_validator("name", "John")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))  # Output: [TypeError] name must be an integer

    try:
        obj.integer_validator("age", 0)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))  # Output: [ValueError] age must be greater than 0

    try:
        obj.integer_validator("distance", -4)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))  # Output: [ValueError] distance must be greater than 0

Note:
    - This module does not require any external module imports.
    - The `BaseGeometry` class is designed to be a simple base class with integer validation methods and an abstract area method.
    - It can be subclassed to create more complex classes that build upon its foundation.
    - The `area()` method raises an exception with the message "area() is not implemented".
    - The `integer_validator()` method validates integer values and raises TypeError or ValueError if conditions are not met.
"""


class BaseGeometry:
    """
    A base class with methods to validate integer values and an abstract area method.
    """

    def area(self):
        """
        Public instance method: area()

        Raises:
            Exception: Always raises an exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method: integer_validator(name, value)

        Parameters:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
