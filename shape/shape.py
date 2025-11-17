"""This module defines the Shape class."""

__author__ = "Gunkar singh"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

class Shape(ABC):
    """An abstract base class for all shapes.
    This class provides a common interface and shared functionality
    for different shape types.
        """

    def __init__(self, color: str) -> None:
        """
            Set up the shape with a color.
            Args:
                color (str): The color of the shape.
            Raises:
                ValueError: If color is blank
            
        """
        if not color.strip():
            raise ValueError("Color cannot be blank.")
        self._color = color.strip()

    def __str__(self) -> str:
        """
        Show the color of the shape.
        Returns:
            str: A description of the shape's color.
           The shape color is {self._color}.
        """
        return f"The shape color is {self._color}."

    @abstractmethod
    def calculate_area(self) -> float:
        """ 
        Calculate the area of the shape.
        Returns:
            float: The area of the shape,area() = base * height / 2
        """
        pass

    @abstractmethod
    def calculate_perimeter(self) -> float:
        """ Calculate the perimeter of the shape.
        Returns:
            float: The perimeter of the shape.
            the perimeter() = sum of all sides
        """
        pass
