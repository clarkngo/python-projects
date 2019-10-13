# Source: https://leetcode.com/problems/di-string-match/

# DI String Match

# Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

# Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

# If S[i] == "I", then A[i] < A[i+1]
# If S[i] == "D", then A[i] > A[i+1]


# Example 1:

# Input: "IDID"
# Output: [0,4,1,3,2]
# Example 2:

# Input: "III"
# Output: [0,1,2,3]
# Example 3:

# Input: "DDI"
# Output: [3,2,0,1]

import unittest # unit test framework
from typing import List


# Totally wrong solution

# class Solution(object):
#     def diStringMatch(self, S):
#         """
#         :type S: str
#         :rtype: List[int]
#         """
#         if len(S) <= 1:
#             return ""
#         curr: int = S[0]
#         my_list: list = []
#         for i in range(1, len(S)):
#             if S[i] > S[i-1]:
#                 my_list.append("I")
#             else:
#                 my_list.append("D")
#         return "".join(my_list)

# Runtime: 52 ms, faster than 82.71% of Python online submissions for DI String Match.
# Memory Usage: 13.1 MB, less than 33.33% of Python online submissions for DI String Match.

class Solution(object):
    def diStringMatch(self, S):
        lo, hi = 0, len(S)
        ans = []
        for x in S:
            if x == 'I':
                ans.append(lo)
                lo += 1
            else:
                ans.append(hi)
                hi -= 1

        return ans + [lo]




a = Solution
class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(a.diStringMatch(self, "IDID"), [0,4,1,3,2])

    def test2(self):
        self.assertEqual(a.diStringMatch(self, "III", [0,1,2,3]))

    def test3(self):
        self.assertEqual(a.diStringMatch(self, "DDI"), [3,2,0,1])


if __name__ == '__main__':
    unittest.main()
