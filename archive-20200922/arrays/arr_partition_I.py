# Source: https://leetcode.com/problems/array-partition-i/

# Array Partition I

# Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

# Example 1:
# Input: [1,4,3,2]

# Output: 4
# Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
# Note:
# n is a positive integer, which is in the range of [1, 10000].
# All the integers in the array will be in the range of [-10000, 10000].

# Runtime: 340 ms, faster than 40.77% of Python3 online submissions for Array Partition I.
# Memory Usage: 16.2 MB, less than 6.06% of Python3 online submissions for Array Partition I.

import unittest # unit test framework
from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        nums.sort()
        for i in range(1, len(nums), 2):
            if nums[i] < nums [i-1]:
                sum += nums[i]
            else:
                sum += nums[i-1]
        return sum


a = Solution
class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(a.arrayPairSum(self, [1,4,3,2]), 4)

    def test2(self):
        self.assertEqual(a.arrayPairSum(self, [1,4]), 1)

if __name__ == '__main__':
    unittest.main()
