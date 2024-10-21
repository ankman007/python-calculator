import unittest
from calculator import add, subtract, divide, multiply

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(-44, -99), -143)
        self.assertEqual(add(1, 120), 121)
        self.assertEqual(add(-1, -12), -13)
        
    def test_subtract(self):
        self.assertEqual(subtract(1, 12), -11)
        self.assertEqual(subtract(1, 18), -17)
        self.assertEqual(subtract(101, -9), 110)
        
    def test_mul(self):
        self.assertEqual(multiply(6, 99), 594)
        self.assertEqual(multiply(22, 0), 0)
        self.assertEqual(multiply(-1, -13), 13)
    
    def test_div(self):
        self.assertEqual(divide(9, 6), 1.5)
        self.assertEqual(divide(6, 2), 3)
        self.assertEqual(divide(5, 2), 2.5)

if __name__ == '__main__': 
    unittest.main()
