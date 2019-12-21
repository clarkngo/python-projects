import factorial
import unittest

class Test_Factorial_0_Returns_1(unittest.TestCase):
    def test(self):
      self.assertEqual(factorial.factorial(0),1)
    def test(self):
      self.assertEqual(factorial.factorial(1),1)

class Test_Factorial_Negative1_Returns_1(unittest.TestCase):
    def test(self):
      with self.assertRaises(Exception): factorial.factorial(-1)

class Test_Factorial_FloatNumMoreThan1_Returns_1(unittest.TestCase):
    def test(self):
      with self.assertRaises(Exception): factorial.factorial(1.1)

class Test_Factorial_FloatNum1_Returns_1(unittest.TestCase):
    def test(self):
      self.assertEqual(factorial.factorial(1.0),1)

if __name__ == '__main__':
    unittest.main()