# Source: https://leetcode.com/problems/rotate-string/

# Rotate String

# We are given two strings, A and B.

# A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

# Example 1:
# Input: A = 'abcde', B = 'cdeab'
# Output: true

# Example 2:
# Input: A = 'abcde', B = 'abced'
# Output: false

# Runtime: 40 ms, faster than 30.02% of Python3 online submissions for Rotate String.
# Memory Usage: 13.9 MB, less than 5.26% of Python3 online submissions for Rotate String.

import unittest # unit test framework
from typing import List

class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if len(A) == 0:
            return True
        if len(A) == 1:
            if A[0] == B[0]:
                return True
            else:
                return False
        rotate = ''
        for i in range(len(A)):
            print(rotate)
            rotate = B[i:] + B[:i]
            if A == rotate:
                return True
        return False


a = Solution
class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(a.rotateString(self, "abcde", "cdeab"), True)

    def test2(self):
        self.assertEqual(a.rotateString(self, "abcde", "abced"), False)

if __name__ == '__main__':
    unittest.main()
