"""This module defines the Triangle class."""

__author__ = "Gunkar singh"
__version__ = "1.0.0"

from math import sqrt
from shape import Shape

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
            ValueError: Raised if any of the side lengths aren't integers—
                        because a triangle needs real, measurable sides.
            ValueError: Raised if the side lengths don't follow the Triangle
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

        # Validate Triangle Inequality Theorem
        if not (side_1 + side_2 > side_3 and side_1 + side_3 > side_2 and side_2 + side_3 > side_1):
            raise ValueError("The sides do not satisfy the Triangle Inequality Theorem.")

        # Assign attributes
        self.__side_1 = side_1
        self.__side_2 = side_2
        self.__side_3 = side_3

    def __str__(self) -> str:
        """
        Return a string that describes the triangle.

        Returns:
            str: A message that describes the triangle’s color and the lengths of its three sides.
        """
       
        return (super().__str__() +
                f"\nThis triangle has three sides with lengths of "
                f"{self.__side_1}, {self.__side_2} and {self.__side_3} centimeters.")

    def calculate_area(self) -> float:
        """
        Finds the area of the triangle using Heron's formula.

        Returns:
              float: The total area of the triangle.
        """
        sp = (self.__side_1 + self.__side_2 + self.__side_3) / 2
        return sqrt(sp * (sp - self.__side_1) * (sp - self.__side_2) * (sp - self.__side_3))

    def calculate_perimeter(self) -> float:
        """
        Finds the perimeter of the triangle.
        Returns:
              float: The total perimeter of the triangle.
        """
        return self.__side_1 + self.__side_2 + self.__side_3