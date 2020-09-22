# Source: https://leetcode.com/problems/add-strings/

# Add Strings

# Given two non-negative integers num1 and num2
# represented as string, return the sum of num1 and num2.

# Note:

# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.


import unittest # unit test framework
from typing import List

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        # OverflowError: int too big to convert
        num1_list = list(num1)
        num2_list = list(num2)

        num1_int = 0
        num2_int = 0

        for num in num1_list:
            num1_int = ord(num) - 48 + num1_int * 10
        for num in num2_list:
            num2_int = ord(num) - 48 + num2_int * 10
        return num1_int + num2_int

        # OverflowError: int too big to convert
        # return int(num1) + int(num2) easiest.

a = Solution
class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(a.addStrings(self, "1", "1"), 2)


    def test_2(self):
        self.assertEqual(a.addStrings(self, "12", "123"), 135)

    def test_3(self):
        self.assertEqual(a.addStrings(self, "401716832807512840963", "167141802233061013023557397451289113296441069"), 167141802233061013023557799168121920809282032)

if __name__ == '__main__':
    unittest.main()
