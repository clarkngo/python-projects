
def returnLength(nums) -> int:
    if len(nums) == 0:
        return 0
    # i slow runner
    # j fast runner
    i = 0
    for j in range(1,len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1

# Source: https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/
# Runtime: 56 ms, faster than 92.79% of Python3 online submissions for Remove Duplicates from Sorted Array.
# Memory Usage: 14.9 MB, less than 32.66% of Python3 online submissions for Remove Duplicates from Sorted Array.
