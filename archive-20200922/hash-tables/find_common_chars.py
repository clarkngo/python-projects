# Source: https://leetcode.com/problems/find-common-characters/

# Find Common Characters

# Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

# You may return the answer in any order.



# Example 1:

# Input: ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:

# Input: ["cool","lock","cook"]
# Output: ["c","o"]

import unittest # unit test framework
from typing import List

class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        dict = {}
        common_chars = []
        for i in range(len(A)):
            for j in range(len(A[i])):
              if A[i][j] not in dict:
                  dict[A[i][j]] = 1
              else:
                  dict[A[i][j]] += 1
        for key, value in dict.items():
            if value % len(A) == 0 or value // len(A) == 1:
                for i in range(value // len(A)):
                    common_chars.append(key)
        return common_chars



a = Solution
class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(a.commonChars(self, ["bella","label","roller"]), ["e","l","l"])

    def test2(self):
        self.assertEqual(a.commonChars(self, ["cool","lock","cook"]), ["c","o"])

    def test3(self):
        self.assertEqual(a.commonChars(self, ["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"]), [])



if __name__ == '__main__':
    unittest.main()
