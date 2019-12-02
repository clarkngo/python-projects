# https://leetcode.com/problems/length-of-last-word/submissions/

# Length of Last Word

# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

# If the last word does not exist, return 0.

# Note: A word is defined as a character sequence consists of non-space characters only.

# Example:

# Input: "Hello World"
# Output: 5

# Runtime: 20 ms, faster than 99.19% of Python3 online submissions for Length of Last Word.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Length of Last Word.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0: return 0
        trimmed = s.rstrip()
        if len(trimmed) == 1:
          if trimmed[0] != ' ':
            return 1
          else:
            return 0
        last_word = ''
        hasSpaces = False
        for i in range(len(trimmed)-1, -1, -1):
            if (trimmed[i] == ' '):
                last_word = trimmed[i+1:len(trimmed)]
                hasSpaces = True
                break
        if hasSpaces:
          return len(last_word)
        return len(trimmed)

# other solution
def lengthOfLastWord(self, s):
    return len(s.rstrip(' ').split(' ')[-1])

import unittest
a = Solution()
class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(a.lengthOfLastWord("Hello World "), 5)
    def test2(self):
        self.assertEqual(a.lengthOfLastWord("Hello My World"), 5)
    def test3(self):
        self.assertEqual(a.lengthOfLastWord("       "), 0)
    def test4(self):
        self.assertEqual(a.lengthOfLastWord(" "), 0)
    def test4(self):
        self.assertEqual(a.lengthOfLastWord("a"), 1)
    def test5(self):
        self.assertEqual(a.lengthOfLastWord(" a"), 1)
    def test6(self):
        self.assertEqual(a.lengthOfLastWord("a "), 1)
    def test7(self):
        self.assertEqual(a.lengthOfLastWord("day"), 3)
    def test8(self):
        self.assertEqual(a.lengthOfLastWord(" day"), 3)
if __name__ == '__main__':
    unittest.main()
