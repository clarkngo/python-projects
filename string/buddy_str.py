# Source: https://leetcode.com/problems/buddy-strings/

# Buddy Strings

# Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.



# Example 1:

# Input: A = "ab", B = "ba"
# Output: true
# Example 2:

# Input: A = "ab", B = "ab"
# Output: false
# Example 3:

# Input: A = "aa", B = "aa"
# Output: true
# Example 4:

# Input: A = "aaaaaaabc", B = "aaaaaaacb"
# Output: true
# Example 5:

# Input: A = "", B = "aa"
# Output: false


# Note:

# 0 <= A.length <= 20000
# 0 <= B.length <= 20000
# A and B consist only of lowercase letters.

# Runtime: 20 ms, faster than 76.40% of Python online submissions for Buddy Strings.
# Memory Usage: 12.8 MB, less than 33.33% of Python online submissions for Buddy Strings.

import unittest # unit test framework
from typing import List

# My code can't catch ("abab", "abab"), True

# class Solution(object):
#     def buddyStrings(self, A, B):
#         """
#         :type A: str
#         :type B: str
#         :rtype: bool
#         """
#         if len(A)!= len(B):
#             return False

#         A_list = list(A)
#         B_list = list(B)
#         if A_list == B_list and len(A) > 1:
#             A_list[1], A_list[0] = A_list[0], A_list[1]
#             if A_list == B_list:
#                 return True
#             else:
#                 return False
#         elif len(A) <= 1:
#             return False
#         for i in range(1, len(A)):
#             A_list[i], A_list[i-1] = A_list[i-1], A_list[i]
#             if A_list == B_list:
#                 return True
#             else:
#                 A_list[i], A_list[i-1] = A_list[i-1], A_list[i]
#         return False

# other solution
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        C, A, B = [i for i in range(len(A)) if A[i] != B[i]], list(A), list(B)
        if not C and len(A) == len(B):
            for i in A:
                if A.count(i) > 1: return True
        elif len(C) == 2 and A[C[0]] == B[C[1]] and A[C[1]] == B[C[0]]: return True
        return False
a = Solution
class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(a.buddyStrings(self, "ab", "ba"), True)

    def test2(self):
        self.assertEqual(a.buddyStrings(self, "aa", "aa"), True)

    def test3(self):
        self.assertEqual(a.buddyStrings(self, "aaaaaaabc", "aaaaaaacb"), True)

    def test4(self):
        self.assertEqual(a.buddyStrings(self, "", "aa"), False)

    def test5(self):
        self.assertEqual(a.buddyStrings(self, "ab", "ab"), False)

    def test6(self):
        self.assertEqual(a.buddyStrings(self, "", ""), False)

    def test7(self):
        self.assertEqual(a.buddyStrings(self, "abab", "abab"), True)


if __name__ == '__main__':
    unittest.main()
