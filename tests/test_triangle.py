"""This module defines the TestTriangle class.

Usage: 
    To execute all tests in the terminal execute the following command:

    $ python -m unittest tests/test_triangle.py
"""

__author__ = "Gunkar singh"
__version__ = "1.0.0"

import unittest
from shape.triangle import Triangle


class TestTriangle(unittest.TestCase):
    """Unit tests for the Triangle class."""

    def setUp(self):
        """Common setup for valid triangle tests."""
        self.triangle = Triangle("Blue", 6, 8, 10)

    def test_valid_triangle_creation(self):
        """Test creating a valid triangle."""
        self.assertIsInstance(self.triangle, Triangle)

    def test_blank_color(self):
        """Test that a blank color raises a ValueError."""
        with self.assertRaises(ValueError) as context:
            Triangle("   ", 6, 8, 10)
        self.assertEqual(str(context.exception), "Color cannot be blank.")

    def test_invalid_side_1_type(self):
        """Test that side_1 must be an integer."""
        with self.assertRaises(ValueError) as context:
            Triangle("Green", "six", 8, 10)
        self.assertEqual(str(context.exception), "Side 1 must be numeric.")

    def test_invalid_side_2_type(self):
        """Test that side_2 must be an integer."""
        with self.assertRaises(ValueError) as context:
            Triangle("Green", 6, "eight", 10)
        self.assertEqual(str(context.exception), "Side 2 must be numeric.")

    def test_invalid_side_3_type(self):
        """Test that side_3 must be an integer."""
        with self.assertRaises(ValueError) as context:
            Triangle("Green", 6, 8, "ten")
        self.assertEqual(str(context.exception), "Side 3 must be numeric.")

    def test_triangle_inequality(self):
        """Test triangle inequality validation."""
        with self.assertRaises(ValueError) as context:
            Triangle("Purple", 2, 3, 5)
        self.assertEqual(
            str(context.exception),
            "The sides do not satisfy the Triangle Inequality Theorem."
        )

    def test_str_method(self):
        """Test the __str__ method output."""
        expected_output = (
            "The shape color is Blue.\n"
            "This triangle has three sides with lengths of 6, 8 and 10 centimeters."
        )
        self.assertEqual(str(self.triangle), expected_output)

    def test_calculate_area(self):
        """Test the area calculation of a valid triangle."""
        # Heron's formula: s = 12, area = √(12 * (12-6) * (12-8) * (12-10)) = √576 = 24
        self.assertEqual(self.triangle.calculate_area(), 24.0)

    def test_calculate_perimeter(self):
        """Test the perimeter calculation of a valid triangle."""
        self.assertEqual(self.triangle.calculate_perimeter(), 24)


if __name__ == "__main__":
    unittest.main()
