"""This module defines the Triangle class."""

__author__ = "Gunkar singh"
__version__ = "1.0.0"

from math import sqrt
from shape.shape import Shape


class Triangle(Shape):
    """Represents a triangle shape with three sides."""

    def __init__(self, color: str, side_1: int, side_2: int, side_3: int) -> None:
        """
        Initialize the triangle with a color and three sides.
         
        Args:
            color (str): The color you'd like the triangle to be.
            side_1 (int): The length of the first side in centimeters.
            side_2 (int): The length of the second side in centimeters.
            side_3 (int): The length of the third side in centimeters.

        Raises:
            ValueError: If any of the side lengths are not integers.
            ValueError: If the side lengths do not satisfy the Triangle
                Inequality Theorem.
        """
        # Validate color using the superclass
        super().__init__(color)

        # Validate all sides are integers
        if not isinstance(side_1, int):
            raise ValueError("Side 1 must be numeric.")
        if not isinstance(side_2, int):
            raise ValueError("Side 2 must be numeric.")
        if not isinstance(side_3, int):
            raise ValueError("Side 3 must be numeric.")

        # Validate Triangle Inequality Theorem (broken into readable lines)
        if not (
            side_1 + side_2 > side_3
            and side_1 + side_3 > side_2
            and side_2 + side_3 > side_1
        ):
            raise ValueError(
                "The sides do not satisfy the Triangle Inequality Theorem."
            )

        # Assign attributes
        self.__side_1 = side_1
        self.__side_2 = side_2
        self.__side_3 = side_3

    def __str__(self) -> str:
        """
        Return a string that describes the triangle.

        Returns:
            str: A message that describes the triangle’s color and
            the lengths of its three sides.
        """
        return (
            super().__str__() +
            f"\nThis triangle has three sides with lengths of "
            f"{self.__side_1}, {self.__side_2} and {self.__side_3} centimeters."
        )

    def calculate_area(self) -> float:
        """
        Find the area of the triangle using Heron's formula.

        Returns:
            float: The total area of the triangle.
        """
        semi_perimeter = (
            self.__side_1 + self.__side_2 + self.__side_3
        ) / 2

        return sqrt(
            semi_perimeter *
            (semi_perimeter - self.__side_1) *
            (semi_perimeter - self.__side_2) *
            (semi_perimeter - self.__side_3)
        )

    def calculate_perimeter(self) -> float:
        """
        Find the perimeter of the triangle.

        Returns:
            float: The total perimeter of the triangle.
        """
        return self.__side_1 + self.__side_2 + self.__side_3

    @property
    def side_1(self) -> int:
        """int: Length of the first side in centimeters."""
        return self.__side_1

    @property
    def side_2(self) -> int:
        """int: Length of the second side in centimeters."""
        return self.__side_2

    @property
    def side_3(self) -> int:
        """int: Length of the third side in centimeters."""
        return self.__side_3
