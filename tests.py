import unittest
from main import *

class TestCalculatr(unittest.TestCase):
    
    def test_addition(self):
        self.assertEqual(addition(1, 1), 2)
        self.assertEqual(addition(1, -1), 0)
        self.assertEqual(addition(1000, 1000), 2000)
    
    def test_subtraction(self):
        self.assertEqual(subtraction(1, 1), 0)
        self.assertEqual(subtraction(1, -1), 2)
        self.assertEqual(subtraction(1000, 1000), 0)

    def test_multiplication(self):
        self.assertEqual(multiplication(1, 1), 1)
        self.assertEqual(multiplication(1, -1), -1)
        self.assertEqual(multiplication(1000, 1000), 1_000_000)
    
    def test_division(self):
        self.assertEqual(division(1, 1), 1)
        self.assertEqual(division(1, -1), -1)
        self.assertEqual(division(1000, 1000), 1)


    def test_raises(self):
        self.assertRaises(ValueError, division, 2, 0)
    
    def test_types(self):
        self.assertRaises(TypeError, addition, '2 + i', '3')
        self.assertRaises(TypeError, subtraction, '2 + i', '3')
        self.assertRaises(TypeError, multiplication, '2 + i', '3')
        self.assertRaises(TypeError, division, '2 + i', '3')
        