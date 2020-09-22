# Source: https://leetcode.com/problems/sliding-window-maximum/

# Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

# Example:

# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7]
# Explanation:

# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Note:
# You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

# Follow up:
# Could you solve it in linear time?

# Runtime: 684 ms, faster than 24.18% of Python3 online submissions for Sliding Window Maximum.
# Memory Usage: 19.4 MB, less than 88.46% of Python3 online submissions for Sliding Window Maximum.

from typing import List
import sys
INT_MIN = -sys.maxsize - 1
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        max_num = INT_MIN
        result = []
        for i in range(len(nums)):
            if i >= k-1:
                max_num=max(nums[i-k+1:i+1])
                result.append(max_num)
        return result

import unittest
A = Solution()
class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(A.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3), [3,3,5,5,6,7])
    def test2(self):
        self.assertEqual(A.maxSlidingWindow([1,-1], 1), [1,-1])
    def test3(self):
        self.assertEqual(A.maxSlidingWindow([7,2,4], 2), [7,4])

if __name__ == '__main__':
	  unittest.main()
