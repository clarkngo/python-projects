# Source: https://leetcode.com/problems/house-robber/

# House Robber

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

# Example 1:

# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.
# Example 2:

# Input: [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
#              Total amount you can rob = 2 + 9 + 1 = 12.

import unittest # unit test framework
from typing import List

class Solution:
    # this only accounts for skipping one element at a time
    # def rob(self, nums: List[int]) -> int:
    #     length = len(nums)
    #     if (length % 2 == 0):   # even length
    #         start1, end1 = 0, length - 1
    #         start2, end2 = 1, length
    #     else:                   # odd length
    #         start1, end1 = 0, length
    #         start2, end2 = 1, length - 1
    #     sum1, sum2 = 0, 0
    #     for i in range(start1, end1, 2):
    #         sum1 += nums[i]
    #     for j in range(start2, end2, 2):
    #         sum2 += nums[j]
    #     if sum1 > sum2:
    #         return sum1
    #     else:
    #         return sum2
    def rob(self, nums: List[int]) -> int:
        skip = 1
        sumList = []
        sum = 0
        for i in range(1):
          sum += nums[0]
          for j in range(i+2,len(nums)-skip, skip):
            sum += nums[j]
        return sum


a = Solution
class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(a.rob(self, [1, 2, 3, 1]), 4)
    def test2(self):
        self.assertEqual(a.rob(self, [1, 2, 3, 1, 2, 1]), 7)
    def test3(self):
        self.assertEqual(a.rob(self, [2,1,1,2]), 4)

if __name__ == '__main__':
    unittest.main()
