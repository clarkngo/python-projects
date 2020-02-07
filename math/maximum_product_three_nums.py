# https://leetcode.com/problems/maximum-product-of-three-numbers/submissions/

# Maximum Product of Three Numbers

# Given an integer array, find three numbers whose product is maximum and output the maximum product.

# Example 1:

# Input: [1,2,3]
# Output: 6


# Example 2:

# Input: [1,2,3,4]
# Output: 24


# Note:

# The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
# Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.

# Runtime: 276 ms, faster than 74.98% of Python3 online submissions for Maximum Product of Three Numbers.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Maximum Product of Three Numbers.

# Explanation:

# Given = [1,2,3,4,5]
# Once you have a sorted list,
# you can grab the last 3 numbers in the sorted list

# Given = [-5,-4,-3,1,2,5]
# However if we have negatives, we need to compare
# the last 3 numbers in the sorted list and
# the first 2 numbers and the last number in the sorted list
# Why? Negative multiplied by negative is positive

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        s_nums = sorted(nums)
        return max(s_nums[-1] * s_nums[-2] * s_nums[-3], s_nums[-1] * s_nums[0] * s_nums[1])

