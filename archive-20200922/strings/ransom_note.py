# Source: https://leetcode.com/problems/ransom-note/

# Ransom Note

# Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

# Each letter in the magazine string can only be used once in your ransom note.

# Note:
# You may assume that both strings contain only lowercase letters.

# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true

import unittest # unit test framework
from typing import List

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_list = list(ransomNote)
        count = 0
        magazine_list = list(magazine)
        for i in range(len(ransom_list)):
            for j in range(len(magazine_list)):
                if ransom_list[i] == magazine_list[j]:
                    count += 1
                    magazine_list[j] = None
        if len(ransom_list) == count:
            return True
        else:
            return False

a = Solution
class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(a.canConstruct(self, "a", "b"), False)
    def test2(self):
        self.assertEqual(a.canConstruct(self, "aa", "ab"), False)
    def test3(self):
        self.assertEqual(a.canConstruct(self, "aa", "abb"), False)
    def test4(self):
        self.assertEqual(a.canConstruct(self, "aa", "aab"), True)
    def test5(self):
        self.assertEqual(a.canConstruct(self, "bg", "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"), True)

if __name__ == '__main__':
    unittest.main()
