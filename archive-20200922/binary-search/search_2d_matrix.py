# https://leetcode.com/problems/search-a-2d-matrix/

# Search a 2D Matrix

# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# Example 1:

# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# Output: true
# Example 2:

# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# Output: false

# Runtime: 64 ms, faster than 79.73% of Python3 online submissions for Search a 2D Matrix.
# Memory Usage: 14.9 MB, less than 5.88% of Python3 online submissions for Search a 2D Matrix.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        if len(matrix) == 1 and len(matrix[0]) == 0:
            return False
        l, m = 0, 0
        r = len(matrix) - 1
        target_arr = []
        while l <= r:
            m = l + (r - l) // 2
            if target < matrix[m][0]:
                print(r)

                r = m - 1
            elif target > matrix[m][-1]:
                l = m + 1
            else:
                break
        left, mid = 0, 0
        right = len(matrix[m]) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if matrix[m][mid] == target:
                return True
            elif target < matrix[m][mid]:
                right = mid - 1
                print("here")
            else:
                left = mid + 1

        return False
