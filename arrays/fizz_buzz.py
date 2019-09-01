# Source: https://leetcode.com/problems/fizz-buzz/

# Fizz Buzz

# Write a program that outputs the string representation of numbers
# from 1 to n. But for multiples of three it should output “Fizz”
# instead of the number and for the multiples of five output “Buzz”.
# For numbers which are multiples of both three and five output “FizzBuzz”.

import unittest # unit test framework
from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr: List = []
        while n != 0:
            if n % 3 == 0 and n % 5 == 0:
                arr.insert(0,"FizzBuzz")
            elif n % 3 == 0:
                arr.insert(0,"Fizz")
            elif n % 5 == 0:
                arr.insert(0,"Buzz")
            else:
                arr.insert(0, str(n))
            n -= 1
        return arr

a = Solution
class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(a.fizzBuzz(self, 1), ["1"])
    def test_fizz(self):
        self.assertEqual(a.fizzBuzz(self, 3), ["1", "2", "Fizz"])
    def test_buzz(self):
        self.assertEqual(a.fizzBuzz(self, 5), ["1", "2", "Fizz", "4", 'Buzz'])
    def test_fizz_buzz(self):
        self.assertEqual(a.fizzBuzz(self, 15),
                                              [
                                                  "1",
                                                  "2",
                                                  "Fizz",
                                                  "4",
                                                  "Buzz",
                                                  "Fizz",
                                                  "7",
                                                  "8",
                                                  "Fizz",
                                                  "Buzz",
                                                  "11",
                                                  "Fizz",
                                                  "13",
                                                  "14",
                                                  "FizzBuzz"
                                              ])


if __name__ == '__main__':
    unittest.main()
