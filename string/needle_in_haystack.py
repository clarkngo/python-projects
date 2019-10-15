# Source: https://leetcode.com/problems/fizz-buzz/

# Fizz Buzz

# Write a program that outputs the string representation of numbers
# from 1 to n. But for multiples of three it should output “Fizz”
# instead of the number and for the multiples of five output “Buzz”.
# For numbers which are multiples of both three and five output “FizzBuzz”.

import unittest # unit test framework
from typing import List

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        match_count = 0
        index = 0
        j = 0
        for i in range(len(haystack)):
          while haystack[i] == needle[j]:
            index = i
            match_count += 1
            j += 1
        if match_count == len(needle):
            index
        return -1

a = Solution
class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(a.strStr(self, "hello", "ll"), [2])

if __name__ == '__main__':
    unittest.main()
