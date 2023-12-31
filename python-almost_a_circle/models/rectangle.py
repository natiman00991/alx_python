# # #!/usr/bin/python3
# """
# This module contains the Rectangle class.
# """
# from models.base import Base


# class Rectangle(Base):
#     """
#     The Rectangle class that inherits from Base.
#     """

#     def __init__(self, width, height, x=0, y=0, id=None):
#         """
#         Initializes a new instance of the Rectangle class.

#         Args:
#             width (int): The width of the rectangle.
#             height (int): The height of the rectangle.
#             x (int, optional): The x-coordinate. Defaults to 0.
#             y (int, optional): The y-coordinate. Defaults to 0.
#             id (int, optional): The id of the rectangle. Defaults to None.
#         """
#         super().__init__(id)
#         self.width = width
#         self.height = height
#         self.x = x
#         self.y = y

#     @property
#     def width(self):
#         """Getter for width attribute."""
#         return self.__width

#     @width.setter
#     def width(self, value):
#         """Setter for width attribute."""
#         if not isinstance(value, int):
#             raise TypeError("width must be an integer")
#         if value <= 0:
#             raise ValueError("width must be > 0")
#         self.__width = value

#     @property
#     def height(self):
#         """Getter for height attribute."""
#         return self.__height

#     @height.setter
#     def height(self, value):
#         """Setter for height attribute."""
#         if not isinstance(value, int):
#             raise TypeError("height must be an integer")
#         if value <= 0:
#             raise ValueError("height must be > 0")
#         self.__height = value

#     @property
#     def x(self):
#         """Getter for x attribute."""
#         return self.__x

#     @x.setter
#     def x(self, value):
#         """Setter for x attribute."""
#         if not isinstance(value, int):
#             raise TypeError("x must be an integer")
#         if value < 0:
#             raise ValueError("x must be >= 0")
#         self.__x = value

#     @property
#     def y(self):
#         """Getter for y attribute."""
#         return self.__y

#     @y.setter
#     def y(self, value):
#         """Setter for y attribute."""
#         if not isinstance(value, int):
#             raise TypeError("y must be an integer")
#         if value < 0:
#             raise ValueError("y must be >= 0")
#         self.__y = value


# if __name__ == "__main__":
#     try:
#         Rectangle(10, "2")
#     except Exception as e:
#         print("[{}] {}".format(e.__class__.__name__, e))

#     try:
#         r = Rectangle(10, 2)
#         r.width = -10
#     except Exception as e:
#         print("[{}] {}".format(e.__class__.__name__, e))

#     try:
#         r = Rectangle(10, 2)
#         r.x = {}
#     except Exception as e:
#         print("[{}] {}".format(e.__class__.__name__, e))

#     try:
#         Rectangle(10, 2, 3, -1)
#     except Exception as e:
#         print("[{}] {}".format(e.__class__.__name__, e))

# #!/usr/bin/python3
# """
# This module contains the Rectangle class.
# """
# from models.base import Base


# class Rectangle(Base):
#     """
#     The Rectangle class that inherits from Base.
#     """

#     def __init__(self, width, height, x=0, y=0, id=None):
#         """
#         Initializes a new instance of the Rectangle class.

#         Args:
#             width (int): The width of the rectangle.
#             height (int): The height of the rectangle.
#             x (int, optional): The x-coordinate. Defaults to 0.
#             y (int, optional): The y-coordinate. Defaults to 0.
#             id (int, optional): The id of the rectangle. Defaults to None.
#         """
#         super().__init__(id)
#         self.width = width
#         self.height = height
#         self.x = x
#         self.y = y

#     @property
#     def width(self):
#         """Getter for width attribute."""
#         return self.__width

#     @width.setter
#     def width(self, value):
#         """Setter for width attribute."""
#         if not isinstance(value, int):
#             raise TypeError("width must be an integer")
#         if value <= 0:
#             raise ValueError("width must be > 0")
#         self.__width = value

#     @property
#     def height(self):
#         """Getter for height attribute."""
#         return self.__height

#     @height.setter
#     def height(self, value):
#         """Setter for height attribute."""
#         if not isinstance(value, int):
#             raise TypeError("height must be an integer")
#         if value <= 0:
#             raise ValueError("height must be > 0")
#         self.__height = value

#     @property
#     def x(self):
#         """Getter for x attribute."""
#         return self.__x

#     @x.setter
#     def x(self, value):
#         """Setter for x attribute."""
#         if not isinstance(value, int):
#             raise TypeError("x must be an integer")
#         if value < 0:
#             raise ValueError("x must be >= 0")
#         self.__x = value

#     @property
#     def y(self):
#         """Getter for y attribute."""
#         return self.__y

#     @y.setter
#     def y(self, value):
#         """Setter for y attribute."""
#         if not isinstance(value, int):
#             raise TypeError("y must be an integer")
#         if value < 0:
#             raise ValueError("y must be >= 0")
#         self.__y = value

#     def area(self):
#         """Calculates and returns the area of the rectangle."""
#         return self.__width * self.__height


# if __name__ == "__main__":
#     r1 = Rectangle(3, 2)
#     print(r1.area())

#     r2 = Rectangle(2, 10)
#     print(r2.area())

#     r3 = Rectangle(8, 7, 0, 0, 12)
#     print(r3.area())

# #!/usr/bin/python3
# """
# This module contains the Rectangle class.
# """
# from models.base import Base


# class Rectangle(Base):
#     """
#     The Rectangle class that inherits from Base.
#     """

#     def __init__(self, width, height, x=0, y=0, id=None):
#         """
#         Initializes a new instance of the Rectangle class.

#         Args:
#             width (int): The width of the rectangle.
#             height (int): The height of the rectangle.
#             x (int, optional): The x-coordinate. Defaults to 0.
#             y (int, optional): The y-coordinate. Defaults to 0.
#             id (int, optional): The id of the rectangle. Defaults to None.
#         """
#         super().__init__(id)
#         self.width = width
#         self.height = height
#         self.x = x
#         self.y = y

#     @property
#     def width(self):
#         """Getter for width attribute."""
#         return self.__width

#     @width.setter
#     def width(self, value):
#         """Setter for width attribute."""
#         if not isinstance(value, int):
#             raise TypeError("width must be an integer")
#         if value <= 0:
#             raise ValueError("width must be > 0")
#         self.__width = value

#     @property
#     def height(self):
#         """Getter for height attribute."""
#         return self.__height

#     @height.setter
#     def height(self, value):
#         """Setter for height attribute."""
#         if not isinstance(value, int):
#             raise TypeError("height must be an integer")
#         if value <= 0:
#             raise ValueError("height must be > 0")
#         self.__height = value

#     @property
#     def x(self):
#         """Getter for x attribute."""
#         return self.__x

#     @x.setter
#     def x(self, value):
#         """Setter for x attribute."""
#         if not isinstance(value, int):
#             raise TypeError("x must be an integer")
#         if value < 0:
#             raise ValueError("x must be >= 0")
#         self.__x = value

#     @property
#     def y(self):
#         """Getter for y attribute."""
#         return self.__y

#     @y.setter
#     def y(self, value):
#         """Setter for y attribute."""
#         if not isinstance(value, int):
#             raise TypeError("y must be an integer")
#         if value < 0:
#             raise ValueError("y must be >= 0")
#         self.__y = value

#     def area(self):
#         """Calculates and returns the area of the rectangle."""
#         return self.__width * self.__height

#     def display(self):
#         """Displays the rectangle using the '#' character."""
#         for _ in range(self.__height):
#             print("#" * self.__width)


# if __name__ == "__main__":
#     r1 = Rectangle(4, 6)
#     r1.display()

#     print("---")

#     r2 = Rectangle(2, 2)
#     r2.display()

# #!/usr/bin/python3
# """
# This module contains the Rectangle class.
# """
# from models.base import Base


# class Rectangle(Base):
#     """
#     The Rectangle class that inherits from Base.
#     """

#     def __init__(self, width, height, x=0, y=0, id=None):
#         """
#         Initializes a new instance of the Rectangle class.

#         Args:
#             width (int): The width of the rectangle.
#             height (int): The height of the rectangle.
#             x (int, optional): The x-coordinate. Defaults to 0.
#             y (int, optional): The y-coordinate. Defaults to 0.
#             id (int, optional): The id of the rectangle. Defaults to None.
#         """
#         super().__init__(id)
#         self.width = width
#         self.height = height
#         self.x = x
#         self.y = y

#     @property
#     def width(self):
#         """Getter for width attribute."""
#         return self.__width

#     @width.setter
#     def width(self, value):
#         """Setter for width attribute."""
#         if not isinstance(value, int):
#             raise TypeError("width must be an integer")
#         if value <= 0:
#             raise ValueError("width must be > 0")
#         self.__width = value

#     @property
#     def height(self):
#         """Getter for height attribute."""
#         return self.__height

#     @height.setter
#     def height(self, value):
#         """Setter for height attribute."""
#         if not isinstance(value, int):
#             raise TypeError("height must be an integer")
#         if value <= 0:
#             raise ValueError("height must be > 0")
#         self.__height = value

#     @property
#     def x(self):
#         """Getter for x attribute."""
#         return self.__x

#     @x.setter
#     def x(self, value):
#         """Setter for x attribute."""
#         if not isinstance(value, int):
#             raise TypeError("x must be an integer")
#         if value < 0:
#             raise ValueError("x must be >= 0")
#         self.__x = value

#     @property
#     def y(self):
#         """Getter for y attribute."""
#         return self.__y

#     @y.setter
#     def y(self, value):
#         """Setter for y attribute."""
#         if not isinstance(value, int):
#             raise TypeError("y must be an integer")
#         if value < 0:
#             raise ValueError("y must be >= 0")
#         self.__y = value

#     def area(self):
#         """Calculates and returns the area of the rectangle."""
#         return self.__width * self.__height

#     def display(self):
#         """Displays the rectangle using the '#' character."""
#         for _ in range(self.__height):
#             print("#" * self.__width)

#     def __str__(self):
#         """Returns the string representation of the rectangle."""
#         return "[Rectangle] ({}) {}/{} - {}/{}".format(
#             self.id, self.__x, self.__y, self.__width, self.__height
#         )


# if __name__ == "__main__":
#     r1 = Rectangle(4, 6, 2, 1, 12)
#     print(r1)

#     r2 = Rectangle(5, 5, 1)
#     print(r2)

# #!/usr/bin/python3
# """
# This module contains the Rectangle class.
# """
# from models.base import Base


# class Rectangle(Base):
#     """
#     The Rectangle class that inherits from Base.
#     """

#     def __init__(self, width, height, x=0, y=0, id=None):
#         """
#         Initializes a new instance of the Rectangle class.

#         Args:
#             width (int): The width of the rectangle.
#             height (int): The height of the rectangle.
#             x (int, optional): The x-coordinate. Defaults to 0.
#             y (int, optional): The y-coordinate. Defaults to 0.
#             id (int, optional): The id of the rectangle. Defaults to None.
#         """
#         super().__init__(id)
#         self.width = width
#         self.height = height
#         self.x = x
#         self.y = y

#     @property
#     def width(self):
#         """Getter for width attribute."""
#         return self.__width

#     @width.setter
#     def width(self, value):
#         """Setter for width attribute."""
#         if not isinstance(value, int):
#             raise TypeError("width must be an integer")
#         if value <= 0:
#             raise ValueError("width must be > 0")
#         self.__width = value

#     @property
#     def height(self):
#         """Getter for height attribute."""
#         return self.__height

#     @height.setter
#     def height(self, value):
#         """Setter for height attribute."""
#         if not isinstance(value, int):
#             raise TypeError("height must be an integer")
#         if value <= 0:
#             raise ValueError("height must be > 0")
#         self.__height = value

#     @property
#     def x(self):
#         """Getter for x attribute."""
#         return self.__x

#     @x.setter
#     def x(self, value):
#         """Setter for x attribute."""
#         if not isinstance(value, int):
#             raise TypeError("x must be an integer")
#         if value < 0:
#             raise ValueError("x must be >= 0")
#         self.__x = value

#     @property
#     def y(self):
#         """Getter for y attribute."""
#         return self.__y

#     @y.setter
#     def y(self, value):
#         """Setter for y attribute."""
#         if not isinstance(value, int):
#             raise TypeError("y must be an integer")
#         if value < 0:
#             raise ValueError("y must be >= 0")
#         self.__y = value

#     def area(self):
#         """Calculates and returns the area of the rectangle."""
#         return self.__width * self.__height

#     def display(self):
#         """Displays the rectangle using the '#' character."""
#         for _ in range(self.__y):
#             print()
#         for _ in range(self.__height):
#             print(" " * self.__x + "#" * self.__width)

#     def __str__(self):
#         """Returns the string representation of the rectangle."""
#         return "[Rectangle] ({}) {}/{} - {}/{}".format(
#             self.id, self.__x, self.__y, self.__width, self.__height
#         )


# if __name__ == "__main__":
#     r1 = Rectangle(2, 3, 2, 2)
#     r1.display()

#     print("---")

#     r2 = Rectangle(3, 2, 1, 0)
#     r2.display()

# #!/usr/bin/python3
# """
# This module contains the Rectangle class.
# """
# from models.base import Base


# class Rectangle(Base):
#     """
#     The Rectangle class that inherits from Base.
#     """

#     def __init__(self, width, height, x=0, y=0, id=None):
#         """
#         Initializes a new instance of the Rectangle class.

#         Args:
#             width (int): The width of the rectangle.
#             height (int): The height of the rectangle.
#             x (int, optional): The x-coordinate. Defaults to 0.
#             y (int, optional): The y-coordinate. Defaults to 0.
#             id (int, optional): The id of the rectangle. Defaults to None.
#         """
#         super().__init__(id)
#         self.width = width
#         self.height = height
#         self.x = x
#         self.y = y

#     @property
#     def width(self):
#         """Getter for width attribute."""
#         return self.__width

#     @width.setter
#     def width(self, value):
#         """Setter for width attribute."""
#         if not isinstance(value, int):
#             raise TypeError("width must be an integer")
#         if value <= 0:
#             raise ValueError("width must be > 0")
#         self.__width = value

#     @property
#     def height(self):
#         """Getter for height attribute."""
#         return self.__height

#     @height.setter
#     def height(self, value):
#         """Setter for height attribute."""
#         if not isinstance(value, int):
#             raise TypeError("height must be an integer")
#         if value <= 0:
#             raise ValueError("height must be > 0")
#         self.__height = value

#     @property
#     def x(self):
#         """Getter for x attribute."""
#         return self.__x

#     @x.setter
#     def x(self, value):
#         """Setter for x attribute."""
#         if not isinstance(value, int):
#             raise TypeError("x must be an integer")
#         if value < 0:
#             raise ValueError("x must be >= 0")
#         self.__x = value

#     @property
#     def y(self):
#         """Getter for y attribute."""
#         return self.__y

#     @y.setter
#     def y(self, value):
#         """Setter for y attribute."""
#         if not isinstance(value, int):
#             raise TypeError("y must be an integer")
#         if value < 0:
#             raise ValueError("y must be >= 0")
#         self.__y = value

#     def area(self):
#         """Calculates and returns the area of the rectangle."""
#         return self.__width * self.__height

#     def display(self):
#         """Displays the rectangle using the '#' character."""
#         for _ in range(self.__y):
#             print()
#         for _ in range(self.__height):
#             print(" " * self.__x + "#" * self.__width)

#     def __str__(self):
#         """Returns the string representation of the rectangle."""
#         return "[Rectangle] ({}) {}/{} - {}/{}".format(
#             self.id, self.__x, self.__y, self.__width, self.__height
#         )

#     def update(self, *args):
#         """
#         Updates the attributes of the rectangle.

#         Args:
#             *args: List of arguments in the order: id, width, height, x, y.
#         """
#         attributes = ["id", "width", "height", "x", "y"]
#         for i, arg in enumerate(args):
#             setattr(self, attributes[i], arg)


# if __name__ == "__main__":
#     r1 = Rectangle(10, 10, 10, 10)
#     print(r1)

#     r1.update(89)
#     print(r1)

#     r1.update(89, 2)
#     print(r1)

#     r1.update(89, 2, 3)
#     print(r1)

#     r1.update(89, 2, 3, 4)
#     print(r1)

#     r1.update(89, 2, 3, 4, 5)
#     print(r1)

#!/usr/bin/python3
"""
This module contains the Rectangle class.
"""
from models.base import Base


class Rectangle(Base):
    """
    The Rectangle class that inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate. Defaults to 0.
            y (int, optional): The y-coordinate. Defaults to 0.
            id (int, optional): The id of the rectangle. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width attribute."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height attribute."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x attribute."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y attribute."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Displays the rectangle using the '#' character."""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Returns the string representation of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the rectangle.

        Args:
            *args: List of arguments in the order: id, width, height, x, y.
            **kwargs: Key-value arguments representing attributes.
        """
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)


# if __name__ == "__main__":
#     r1 = Rectangle(10, 10, 10, 10)
#     print(r1)

#     r1.update(height=1)
#     print(r1)

#     r1.update(width=1, x=2)
#     print(r1)

#     r1.update(y=1, width=2, x=3, id=89)
#     print(r1)

#     r1.update(x=1, height=2, y=3, width=4)
#     print(r1)
