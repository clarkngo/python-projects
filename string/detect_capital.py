# Source: https://leetcode.com/problems/detect-capital/

# Detect Capital
# Given a word, you need to judge whether the usage of capitals in it is right or not.

# We define the usage of capitals in a word to be right when one of the following cases holds:

# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Otherwise, we define that this word doesn't use capitals in a right way.


# Example 1:

# Input: "USA"
# Output: True


# Example 2:

# Input: "FlaG"
# Output: False

# Runtime: 28 ms, faster than 99.36% of Python3 online submissions for Detect Capital.
# Memory Usage: 13.8 MB, less than 6.67% of Python3 online submissions for Detect Capital.

import unittest # unit test framework
from typing import List

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) <= 1:
            return True
        # Uppercase first letter
        if ord(word[0]) >= 65 and ord(word[0]) <= 90:
            # if second letter is uppercase
            if ord(word[1]) >= 65 and ord(word[1]) <= 90:
                # start from 3rd letter onwards
                for i in range(2, len(word)):
                    # if 3rd letter and onwards is not uppercase
                    if not ord(word[i]) >= 65 or not ord(word[i]) <= 90:
                        return False
                    else:
                        continue
                return True
            # if second letter is lowercase
            elif not ord(word[1]) >= 65 or not ord(word[1]) <= 90:
                # start from 3rd letter onwards
                for i in range(2, len(word)):
                    # if 3rd letter and onwards is uppercase
                    if ord(word[i]) >= 65 and ord(word[i]) <= 90:
                        return False
                    else:
                        continue

            return True

        # Lowercase first letter
        elif ord(word[0]) >= 97 and ord(word[0]) <= 122:
            for i in range(1, len(word)):
                # if uppercase afterwards
                if not ord(word[i]) >= 97 or not ord(word[i]) <= 122:
                    return False
            return True

a = Solution
class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(a.detectCapitalUse(self, "USA"), True)
    def test2(self):
        self.assertEqual(a.detectCapitalUse(self, "leetcode"), True)
    def test3(self):
        self.assertEqual(a.detectCapitalUse(self, "lEetcode"), False)
    def test4(self):
        self.assertEqual(a.detectCapitalUse(self, "Google"), True)
    def test5(self):
        self.assertEqual(a.detectCapitalUse(self, "FlAG"), False)
    def test6(self):
        self.assertEqual(a.detectCapitalUse(self, "FlaG"), False)
    def test7(self):
        self.assertEqual(a.detectCapitalUse(self, "flaG"), False)
    def test8(self):
        self.assertEqual(a.detectCapitalUse(self, "f"), True)
    def test9(self):
        self.assertEqual(a.detectCapitalUse(self, "F"), True)
    def test10(self):
        self.assertEqual(a.detectCapitalUse(self, "FFFFFFFFFFFf"), False)
if __name__ == '__main__':
    unittest.main()

