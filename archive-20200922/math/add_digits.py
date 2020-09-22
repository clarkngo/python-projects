# Source: https://leetcode.com/problems/add-digits/

# Add Digits

# Write a program that outputs the string representation of numbers
# from 1 to n. But for multiples of three it should output “Fizz”
# instead of the number and for the multiples of five output “Buzz”.
# For numbers which are multiples of both three and five output “FizzBuzz”.

import unittest # unit test framework
from typing import List

class Solution:
    def addDigits(self, num: int) -> int:
        while num % 10 == 0:
            num //= 10
        sum = 0
        while True:
            while num % 10 != 0:
                sum += num % 10
                num //= 10
                print(sum)
            if sum <= 10:
                break
            num = sum
            sum = 0
        if sum % 10 == 0:
            return sum // 10
        return sum

a = Solution
class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(a.addDigits(self, 38), 2)

    def test2(self):
        self.assertEqual(a.addDigits(self, 49), 4)

    def test3(self):
        self.assertEqual(a.addDigits(self, 10), 1)

    def test4(self):
        self.assertEqual(a.addDigits(self, 11), 2)
    def test5(self):
        self.assertEqual(a.addDigits(self, 19), 1)

    def test6(self):
        self.assertEqual(a.addDigits(self, 20), 2)


    def test7(self):
        self.assertEqual(a.addDigits(self, 100), 1)

if __name__ == '__main__':
    unittest.main()
