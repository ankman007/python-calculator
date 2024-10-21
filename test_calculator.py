import unittest
import calculator as calc

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(-44, -99), -143)
        self.assertEqual(calc.add(1, 120), 121)
        self.assertEqual(calc.add(-1, -12), -13)
        
    def test_subtract(self):
        self.assertEqual(calc.subtract(1, 12), -11)
        self.assertEqual(calc.subtract(1, 18), -17)
        self.assertEqual(calc.subtract(101, -9), 110)
        
    def test_mul(self):
        self.assertEqual(calc.multiply(6, 99), 594)
        self.assertEqual(calc.multiply(22, 0), 0)
        self.assertEqual(calc.multiply(-1, -13), 13)
    
    def test_div(self):
        self.assertEqual(calc.divide(9, 6), 1.5)
        self.assertEqual(calc.divide(6, 2), 3)
        self.assertEqual(calc.divide(5, 2), 2.5)

if __name__ == '__main__': 
    unittest.main()
