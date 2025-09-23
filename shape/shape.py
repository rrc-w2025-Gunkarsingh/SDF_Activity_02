"""This module defines the Shape class."""

__author__ = "Gunkar singh"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

class Shape(ABC):
   def __init__(self, color: str) -> None:
    """Initialize the shape with a color."""
    if not color.strip():
        raise ValueError("Color cannot be blank.")
    self._color = color.strip()


    def __str__(self) -> str:
        return f"The shape color is {self._color}."

    @abstractmethod
    def calculate_area(self) -> float:
        pass

    @abstractmethod
    def calculate_perimeter(self) -> float:
        pass
