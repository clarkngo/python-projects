# https://leetcode.com/problems/maximum-product-subarray/

# Maximum Product Subarray

# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

# Example 1:

# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

class Solution:
    # Given: [2, 3, -2, 4]
    def maxProduct(self, A):
        B = A[::-1]   # reversed list [4, -2, 3, 2]
        for i in range(1, len(A)):
            A[i] *= A[i-1] or 1   # calculate prefix product in A
            B[i] *= B[i-1] or 1   # calculate suffix product in B

        # list A [2, 6, -12, -48]
        # list B [4, -8, -24, -48]
        return max(A+B)   # Output: 6
