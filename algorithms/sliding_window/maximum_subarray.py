# https://leetcode.com/problems/maximum-subarray/

# Maximum Subarray

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:

# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

# Runtime: 60 ms, faster than 98.32% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 13.5 MB, less than 78.86% of Python3 online submissions for Maximum Subarray.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        cur_sum, max_sum = nums[0], nums[0]
        for i in range(1, len(nums)):
            cur_sum += nums[i]
            if nums[i] > cur_sum:
                cur_sum = nums[i]
            if cur_sum > max_sum:
                max_sum = cur_sum
        return max_sum
