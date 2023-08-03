"""
6-rectangle.py - A Python module defining the Rectangle class, which inherits from BaseGeometry.

This module defines the `Rectangle` class, which inherits from the `BaseGeometry` class. It represents a rectangle with private attributes `__width` and `__height`, and it provides an implementation of the `area()` method to calculate the area of the rectangle. The `Rectangle` class validates the width and height as positive integers using the `integer_validator` method inherited from the `BaseGeometry` class.

Classes:
    BaseGeometry:
        A base class with methods to validate integer values and an abstract area method.

    Rectangle(BaseGeometry):
        A class representing a rectangle with private attributes for width and height.

Methods:
    __init__(self, width, height):
        Constructor method to initialize the Rectangle object with width and height.
    __str__(self):
        String representation of the Rectangle object.
    area(self):
        Calculate the area of the rectangle.

Usage:
    import 6-rectangle

    r = 6-rectangle.Rectangle(3, 5)
    print(r)  # Output: [Rectangle] 3/5

    try:
        print("Rectangle: {} - {}".format(r.width, r.height))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))  # Output: [AttributeError] 'Rectangle' object has no attribute 'width'

    try:
        r2 = 6-rectangle.Rectangle(4, True)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))  # Output: [TypeError] height must be an integer

Note:
    - This module does not require any external module imports.
    - The `Rectangle` class is designed to inherit from the `BaseGeometry` class, providing additional functionality for rectangles.
    - The `__init__` method initializes the `Rectangle` object with private attributes for width and height, and it validates these attributes using the `integer_validator` method.
    - The `area()` method calculates the area of the rectangle and is inherited from the `BaseGeometry` class.
    - The `Rectangle` class restricts direct access to its width and height attributes, making them private.
    - The width and height attributes are validated to ensure they are positive integers, as required for a rectangle.
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


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle with private attributes for width and height.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Constructor method to initialize the Rectangle object with width and height.

        Parameters:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def __str__(self):
        """
        String representation of the Rectangle object.

        Returns:
            str: A formatted string representing the Rectangle object in the format [Rectangle] <width>/<height>.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height
