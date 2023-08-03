"""
This module defines the Square class.

The Square class represents a square and has a private instance attribute `__size`, which stores the size of the square.
The class provides instantiation with an optional size argument. If the size is provided, it must be an integer.
If the size is not provided, the default value is 0.

Attributes:
    __size (int): The size of the square.

Methods:
    __init__(self, size=0):
        Initializes a new Square instance with the given size (default: 0).
        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is less than 0.
    area(self):
        Calculates the area of the square.
        Returns:
            int: The area of the square.
"""


class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0):
            Initializes a new Square instance with the given size (default: 0).
            Raises:
                TypeError: If the provided size is not an integer.
                ValueError: If the provided size is less than 0.
        area(self):
            Calculates the area of the square.
            Returns:
                int: The area of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.
        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size**2


# if __name__ == "__main__":
#     my_square = Square(3)
#     print(type(my_square))
#     print(my_square.__dict__)

#     try:
#         print(my_square.size)
#     except Exception as e:
#         print(e)

#     try:
#         print(my_square.__size)
#     except Exception as e:
#         print(e)
