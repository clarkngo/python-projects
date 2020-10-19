# Remove Duplicates from Sorted Array

# Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer_1 = 0
        pointer_2 = 1
        count = 0
        for pointer_2 in range(len(nums)):
            if nums[pointer_1] != nums[pointer_2]:
                pointer_1 += 1
                nums[pointer_1] = nums[pointer_2]
        return pointer_1 + 1
