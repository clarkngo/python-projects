# Source: https://leetcode.com/problems/missing-number/
# Missing Number

# Given an array containing n distinct numbers taken from
# 0, 1, 2, ..., n, find the one that is missing from the array.

# Example 1:

# Input: [3,0,1]
# Output: 2

# Runtime: 172 ms, faster than 20.84% of Python3 online submissions for Missing Number.
# Memory Usage: 15 MB, less than 6.45% of Python3 online submissions for Missing Number.

import unittest # unit test framework
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
      nums.sort()
      for i in range(len(nums)):
        if nums[i] != i:
          return nums[i] - 1
      return nums[i] + 1

a = Solution
class Test(unittest.TestCase):

    def test_missing_number_in_the_middle(self):
        self.assertEqual(a.missingNumber(self, [3, 0, 1]), 2)

    def test_list_with_one_element(self):
        self.assertEqual(a.missingNumber(self, [0]), 1)

if __name__ == '__main__':
    unittest.main()
