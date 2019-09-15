# Source: https://leetcode.com/problems/sqrtx/

# Sqrt(x)

# Implement int sqrt(int x).

# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

# Example 1:

# Input: 4
# Output: 2
# Example 2:

# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since
#              the decimal part is truncated, 2 is returned.

import unittest # unit test framework
from typing import List

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        l, r = 1, x
        while l <= r:
            mid = l + (r- l) // 2
            sqrt = x // mid
            if sqrt == mid:
                return mid
            elif mid > sqrt:
                r = mid - 1
            else:
                l = mid + 1
        return r


a = Solution
class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(a.mySqrt(self, 4), 2)

    def test2(self):
        self.assertEqual(a.mySqrt(self, 8), 2)


if __name__ == '__main__':
    unittest.main()
