# https://leetcode.com/problems/maximum-average-subarray-i/

# Maximum Average Subarray I

# Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

# Example 1:

# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75
# Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75

# Note:

# 1 <= k <= n <= 30,000.
# Elements of the given array will be in the range [-10,000, 10,000].

# Runtime: 964 ms, faster than 67.71% of Python3 online submissions for Maximum Average Subarray I.
# Memory Usage: 16.1 MB, less than 12.50% of Python3 online submissions for Maximum Average Subarray I.

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) < k: return 0.00
        current_total = 0
        max_sum = float("-inf")
        for i in range(len(nums)):
            current_total += nums[i]
            if i >= k - 1:
                if current_total > max_sum:
                    max_sum = current_total
                current_total -= nums[i-(k-1)]
        return max_sum / k

import unittest
A = Solution()
class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(A.findMaxAverage([1,12,-5,-6,50,3], 4), 12.75000)
    def test2(self):
        self.assertEqual(A.findMaxAverage([3,3,4,3,0], 3), 3.33333)


if __name__ == '__main__':
	  unittest.main()