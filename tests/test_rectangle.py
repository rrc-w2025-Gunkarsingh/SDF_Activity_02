"""This module defines the TestRectangle class.

Usage: 
    To execute all tests in the terminal execute the following command:

    $ python -m unittest tests/test_rectangle.py
"""

__author__ = "Gunkar singh"
__version__ = "1.0.0"

import unittest
from shape.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.rectangle = Rectangle("Blue", 5, 6)

    def test_valid_rectangle_creation(self):
        self.assertIsInstance(self.rectangle, Rectangle)

    def test_blank_color(self):
        with self.assertRaises(ValueError) as context:
            Rectangle("   ", 5, 6)
        self.assertEqual(str(context.exception), "Color cannot be blank.")

    def test_invalid_length_type(self):
        with self.assertRaises(ValueError) as context:
            Rectangle("Red", "five", 6)
        self.assertEqual(str(context.exception), "Length must be numeric.")

    def test_invalid_width_type(self):
        with self.assertRaises(ValueError) as context:
            Rectangle("Red", 5, "six")
        self.assertEqual(str(context.exception), "Width must be numeric.")

    def test_str_method(self):
        expected_output = (
            "The shape color is Blue.\n"
            "This rectangle has four sides with the lengths of 5, 6, 5 and 6 centimeters."
        )
        self.assertEqual(str(self.rectangle), expected_output)

    def test_calculate_area(self):
        self.assertEqual(self.rectangle.calculate_area(), 30)

    def test_calculate_perimeter(self):
        self.assertEqual(self.rectangle.calculate_perimeter(), 22)


if __name__ == "__main__":
    unittest.main()

