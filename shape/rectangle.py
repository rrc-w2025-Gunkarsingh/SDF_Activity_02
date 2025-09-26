"""This module defines the Rectangle class."""

__author__ = "Gunkar Singh"
__version__ = "1.0.0"

from shape.shape import Shape

class Rectangle(Shape):
    """A simple class to represent a rectangle shape."""

    def __init__(self, color: str, length: int, width: int) -> None:
        """
        Create a new rectangle.

        Args:
            color (str): The color of the rectangle.
            length (int): The length of the rectangle.
            width (int): The width of the rectangle.

        Raises:
            ValueError: If length or width is not an integer.
        """
        super().__init__(color)

        super().__init__(color)
        if not isinstance(length, int):
            raise ValueError("Length must be numeric.")
        if not isinstance(width, int):
            raise ValueError("Width must be numeric.")
        
        self._length = length
        self._width = width

    def __str__(self) -> str:
        """
        Show a simple description of the rectangle.
        """
        return (
            f"The shape color is {self._color}.\n"
            f"This rectangle has four sides with the lengths of "
            f"{self._length}, {self._width}, {self._length} and {self._width} centimeters."
        )

    def calculate_area(self) -> float:
        """
        Find the area of the rectangle.
        """
        return self._length * self._width

    def calculate_perimeter(self) -> float:
        """ Find the perimeter of the rectangle.
        """
        return 2 * self._length + 2 * self._width

