from simple_calc import SimpleCalc
import unittest
import pytest


class Calctests(unittest.TestCase):

    calc = SimpleCalc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 4), 6)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5, 1), 5)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 2), 3)
