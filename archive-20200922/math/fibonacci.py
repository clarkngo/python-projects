# Source: https://leetcode.com/problems/fibonacci-number/

# Fibonacci Number

# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), for N > 1.
# Given N, calculate F(N).

import unittest # unit test framework
from typing import List

class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 1:
            return N
        return self.fib(N-1) + self.fib(N-2)

a = Solution
class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(a.fib(self, 3), 2)

    def test2(self):
        self.assertEqual(a.fib(self, 4), 3)

if __name__ == '__main__':
    unittest.main()
