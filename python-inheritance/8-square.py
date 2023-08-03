"""
8-square.py - A Python module defining the Square class, which inherits from Rectangle.

This module defines the `Square` class, which inherits from the `Rectangle` class. It represents a square with a private attribute `__size`, and it provides an implementation of the `area()` method to calculate the area of the square. The `Square` class validates the size as a positive integer using the `integer_validator` method inherited from the `BaseGeometry` class.

Classes:
    BaseGeometry:
        A base class with methods to validate integer values and an abstract area method.

    Rectangle(BaseGeometry):
        A class representing a rectangle with private attributes for width and height.

    Square(Rectangle):
        A class representing a square with a private attribute for size.

Methods:
    __init__(self, size):
        Constructor method to initialize the Square object with size.
    __str__(self):
        String representation of the Square object.
    area(self):
        Calculate the area of the square.

Usage:
    import 8-square

    s = 8-square.Square(13)
    print(s)  # Output: [Square] 13/13
    print(s.area())  # Output: 169

Note:
    - This module does not require any external module imports.
    - The `Square` class is designed to inherit from the `Rectangle` class, representing a special case where width and height are the same (equal to size).
    - The `__init__` method initializes the `Square` object with a private attribute for size and validates it using the `integer_validator` method.
    - The `Square` class restricts direct access to its size attribute, making it private.
    - The size attribute is validated to ensure it is a positive integer, as required for a square.
    - The `area()` method calculates the area of the square and is inherited from the `Rectangle` class.
    - The `print()` function and `str()` method display the square description in the format [Square] <size>/<size>.
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


class Square(Rectangle):
    """
    A class representing a square with a private attribute for size.

    Attributes:
        __size (int): The size of the square (equal to width and height).
    """

    def __init__(self, size):
        """
        Constructor method to initialize the Square object with size.

        Parameters:
            size (int): The size of the square (equal to width and height).
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        String representation of the Square object.

        Returns:
            str: A formatted string representing the Square object in the format [Square] <size>/<size>.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
