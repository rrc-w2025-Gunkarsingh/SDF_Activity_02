"""This module defines the Shape class."""

__author__ = "Gunkar singh"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

class Shape(ABC):
    """An abstract base class for all shapes."""

    def __init__(self, color: str) -> None:
        """
            Set up the shape with a color.
        """
        if not color.strip():
            raise ValueError("Color cannot be blank.")
        self._color = color.strip()

    def __str__(self) -> str:
        """
        Show the color of the shape.
        """
        return f"The shape color is {self._color}."

    @abstractmethod
    def calculate_area(self) -> float:
        """ 
        Calculate the area of the shape.
        """
        pass

    @abstractmethod
    def calculate_perimeter(self) -> float:
        """ Calculate the perimeter of the shape.
        """
        pass
