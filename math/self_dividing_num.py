# Source: https://leetcode.com/problems/self-dividing-numbers/

# Self Dividing Numbers

# A self-dividing number is a number that is divisible by every digit it contains.

# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

# Also, a self-dividing number is not allowed to contain the digit zero.

# Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

# Example 1:
# Input:
# left = 1, right = 22
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
# Note:

# The boundaries of each input argument are 1 <= left <= right <= 10000.

# Runtime: 64 ms, faster than 34.55% of Python online submissions for Self Dividing Numbers.
# Memory Usage: 12 MB, less than 30.00% of Python online submissions for Self Dividing Numbers.

import unittest # unit test framework
from typing import List

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        return [number for number in range(left, right+1) if '0' not in str(number) and all((number % int(char) == 0 for char in str(number)))]

a = Solution
class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(a.selfDividingNumbers(self, 1, 22), [1,2,3,4,5,6,7,8,9,11,12,15,22])

if __name__ == '__main__':
    unittest.main()
