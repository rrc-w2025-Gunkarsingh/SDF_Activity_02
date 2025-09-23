"""This module defines the Rectangle class."""

__author__ = "Gunkar Singh"
__version__ = "1.0.0"

from shape.shape import Shape

class Rectangle(Shape):
    def __init__(self, color: str, length: int, width: int) -> None:
        super().__init__(color)

        if not isinstance(length, int):
            raise ValueError("Length must be numeric.")
        if not isinstance(width, int):
            raise ValueError("Width must be numeric.")

        self._length = length
        self._width = width

    def __str__(self) -> str:
        return (
            super().__str__() +
            f"\nThis rectangle has four sides with the lengths of "
            f"{self._length}, {self._width}, {self._length} and {self._width} centimeters."
        )

    def calculate_area(self) -> float:
        return self._length * self._width

    def calculate_perimeter(self) -> float:
        return 2 * self._length + 2 * self._width

