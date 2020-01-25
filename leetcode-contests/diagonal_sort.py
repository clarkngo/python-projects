# Sort the Matrix Diagonally
# User Accepted:1012
# User Tried:1103
# Total Accepted:1020
# Total Submissions:1432
# Difficulty:Medium
# Given a m * n matrix mat of integers, sort it diagonally in ascending order from the top-left to the bottom-right then return the sorted array.



# Example 1:


# Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
# Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]


# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# 1 <= mat[i][j] <= 100

class Solution(object):
    def diagonalSort(self, A):
        R, C = len(A), len(A[0])
        vals = collections.defaultdict(list)
        for r, row in enumerate(A):
            for c,v  in enumerate(row):
                vals[r-c].append(v)
        for row in vals.values():
            row.sort(reverse=True)
        for r, row in enumerate(A):
            for c,v  in enumerate(row):
                A[r][c] = vals[r-c].pop()
        return A
