# https://leetcode.com/problems/two-sum/

# Two Sum

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# Runtime: 44 ms, faster than 96.32% of Python3 online submissions for Two Sum.
# Memory Usage: 14 MB, less than 65.81% of Python3 online submissions for Two Sum.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i in range(len(nums)):
            sum_minus_val = target - nums[i]
            if sum_minus_val not in my_dict:
                my_dict[nums[i]] = i
            else:
                return [i,my_dict[sum_minus_val]]
