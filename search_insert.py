# https://leetcode.com/problems/search-insert-position/

# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.

# Example 1:

# Input: [1,3,5,6], 5
# Output: 2
# Example 2:

# Input: [1,3,5,6], 2
# Output: 1
# Example 3:

# Input: [1,3,5,6], 7
# Output: 4
# Example 4:

# Input: [1,3,5,6], 0
# Output: 0

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for index, value in enumerate(nums):
            if value == target or value > target:
                return index
            if index == len(nums) - 1 and value < target:
                return index + 1

# Runtime: 36 ms, faster than 89.98% of Python3 online submissions for Search Insert Position.
# Memory Usage: 13.6 MB, less than 69.77% of Python3 online submissions for Search Insert Position.

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for index, value in enumerate(nums):
            if value == target or value > target:
                return index
        if nums[len(nums) - 1] < target:
            return len(nums)

# Runtime: 32 ms, faster than 96.99% of Python3 online submissions for Search Insert Position.
# Memory Usage: 13.8 MB, less than 13.17% of Python3 online submissions for Search Insert Position.
