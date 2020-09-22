# https://leetcode.com/problems/move-zeroes/submissions/

# Given an array nums, write a function to move all 0's
# to the end of it while maintaining the relative order of the non-zero elements.

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

## Solution is Time Limit Exceeded

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n):
            for j in range(0, n-i-1):
                if nums[j] == 0:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
