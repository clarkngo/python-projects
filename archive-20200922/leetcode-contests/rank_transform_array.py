# Rank Transform of an Array
# User Accepted:1498
# User Tried:1741
# Total Accepted:1523
# Total Submissions:2954
# Difficulty:Easy
# Given an array of integers arr, replace each element with its rank.

# The rank represents how large the element is. The rank has the following rules:

# Rank is an integer starting from 1.
# The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
# Rank should be as small as possible.


# Example 1:

# Input: arr = [40,10,20,30]
# Output: [4,1,2,3]
# Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.
# Example 2:

# Input: arr = [100,100,100]
# Output: [1,1,1]
# Explanation: Same elements share the same rank.
# Example 3:

# Input: arr = [37,12,28,9,100,56,80,5,12]
# Output: [5,3,4,2,8,6,7,1,3]


# Constraints:

# 0 <= arr.length <= 105
# -109 <= arr[i] <= 109

# class Solution(object):
#     def arrayRankTransform(self, A):
#         rank = {}
#         for i,a in enumerate(sorted(A)):
#             if a not in rank:
#                 rank[a] = len(rank) + 1
#         return [rank[a] for a in A]

# class Solution(object):
#     def arrayRankTransform(self, A):
#         vals = sorted(set(A))
#         m = {}
#         for i, v in enumerate(vals):
#             m[v] = i + 1
#         return [m[x] for x in A]

# My Solution
class Solution:
    def arrayRankTransform(self, arr):
        s_arr = sorted(arr)
        d = {}
        rank = 1
        for i in range(len(s_arr)):
            if s_arr[i] not in d:
                d[s_arr[i]] = rank
                rank += 1
        for i in range(len(arr)):
            arr[i] = d[arr[i]]
        return arr

s = Solution()
ans = s.arrayRankTransform([37,12,28,9,100,56,80,5,12])
print(ans)
