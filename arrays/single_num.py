# Source: https://leetcode.com/problems/single-number/
# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
# Example 1:
# Input: [2,2,1]
# Output: 1
# Example 2:
# Input: [4,1,2,1,2]
# Output: 4

# Runtime: 1228 ms, faster than 7.06% of Python3 online submissions for Single Number.
# Memory Usage: 16 MB, less than 6.56% of Python3 online submissions for Single Number.

import unittest # unit test framework
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
      no_dup:List = []
      for i in range(len(nums)):
        if nums[i] not in no_dup:
          no_dup.append(nums[i])
        else:
          no_dup.remove(nums[i])
      return no_dup.pop()

a = Solution
class Test(unittest.TestCase):

    def test_uniq_at_end(self):
        self.assertEqual(a.singleNumber(self, [2,2,1]), 1)

    def test_uniq_at_beg(self):
        self.assertEqual(a.singleNumber(self, [4,1,2,1,2]), 4)

    def test_uniq_at_mid(self):
        self.assertEqual(a.singleNumber(self, [1,1,5,6,6]), 5)

    def test_one_element(self):
        self.assertEqual(a.singleNumber(self, [1]), 1)

if __name__ == '__main__':
    unittest.main()
