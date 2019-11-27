# Source: https://leetcode.com/problems/reverse-only-letters/

# Reverse Only Letters

# Given a string S, return the "reversed" string where all
# characters that are not a letter stay in the same place,
# and all letters reverse their positions.


# Example 1:

# Input: "ab-cd"
# Output: "dc-ba"
# Example 2:

# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# Example 3:

# Input: "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"

import unittest # unit test framework
from typing import List

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        S_list = list(S)
        new_list = []
        index = 0
        for i in range(len(S_list)):
            if ord(S_list[i]) >= 65 and ord(S_list[i]) <= 90:
                new_list.insert(index, S_list[i])
            elif ord(S_list[i]) >= 97 and ord(S_list[i]) <= 122:
                new_list.insert(index, S_list[i])
            else:
                new_list.append(S_list[i])
                index = i+1
        print("".join(new_list))
        return "".join(new_list)

a = Solution
class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(a.reverseOnlyLetters(self, "ab-cd"), "dc-ba")

    # def test2(self):
    #     self.assertEqual(a.reverseOnlyLetters(self, "a-bC-dEf-ghIj"), "j-Ih-gfE-dCba")

    # def test3(self):
    #     self.assertEqual(a.reverseOnlyLetters(self, "Test1ng-Leet=code-Q!"), "Qedo1ct-eeLg=ntse-T!")

if __name__ == '__main__':
    unittest.main()
