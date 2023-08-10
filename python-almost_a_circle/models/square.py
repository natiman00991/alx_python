#!/usr/bin/python3
# """
# This module contains the Square class.
# """
# from models.rectangle import Rectangle


# class Square(Rectangle):
#     """
#     The Square class that inherits from Rectangle.
#     """

#     def __init__(self, size, x=0, y=0, id=None):
#         """
#         Initializes a new instance of the Square class.

#         Args:
#             size (int): The size of the square.
#             x (int, optional): The x-coordinate. Defaults to 0.
#             y (int, optional): The y-coordinate. Defaults to 0.
#             id (int, optional): The id of the square. Defaults to None.
#         """
#         super().__init__(size, size, x, y, id)

#     def __str__(self):
#         """Returns the string representation of the square."""
#         return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)


# if __name__ == "__main__":
#     s1 = Square(5)
#     print(s1)
#     print(s1.area())
#     s1.display()

#     print("---")

#     s2 = Square(2, 2)
#     print(s2)
#     print(s2.area())
#     s2.display()

#     print("---")

#     s3 = Square(3, 1, 3)
#     print(s3)
#     print(s3.area())
#     s3.display()

#!/usr/bin/python3
"""
This module contains the Square class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    The Square class that inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate. Defaults to 0.
            y (int, optional): The y-coordinate. Defaults to 0.
            id (int, optional): The id of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size attribute."""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns the string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)


# if __name__ == "__main__":
#     s1 = Square(5)
#     print(s1)
#     print(s1.size)
#     s1.size = 10
#     print(s1)

#     try:
#         s1.size = "9"
#     except Exception as e:
#         print("[{}] {}".format(e.__class__.__name__, e))
