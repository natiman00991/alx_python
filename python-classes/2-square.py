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
