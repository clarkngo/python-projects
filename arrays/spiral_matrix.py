# https://leetcode.com/problems/spiral-matrix/

# Spiral Matrix

# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

# Example 1:

# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:

# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# Runtime: 24 ms, faster than 87.55% of Python3 online submissions for Spiral Matrix.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Spiral Matrix.

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        results = []
        while matrix:
            results.extend(matrix.pop(0))            # left to right
            if matrix and matrix[0]:
                for row in matrix:
                    results.append(row.pop())         # top to bottom
            if matrix:
                results.extend(matrix.pop(-1)[::-1]) # right to left
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    results.append(row.pop(0))        # bottom to top
        return results
