# Source: https://leetcode.com/problems/reverse-only-letters/
# Reverse Only Letters

# Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.



# Example 1:

# Input: "ab-cd"
# Output: "dc-ba"
# Example 2:

# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# Example 3:

# Input: "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"


# Note:

# S.length <= 100
# 33 <= S[i].ASCIIcode <= 122
# S doesn't contain \ or "

# Runtime: 24 ms, faster than 98.66% of Python3 online submissions for Reverse Only Letters.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Reverse Only Letters.

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        listAlpha, listOthers = [], []
        for i in range(len(S)):
            if S[i].isalpha():
                listAlpha.append(S[i])
            else:
                listOthers.append([S[i],i])
        listAll = listAlpha[::-1]
        for j in range(len(listOthers)):
            while listOthers:
                listAll.insert(listOthers[0][1], listOthers[0][0])
                listOthers.pop(0)
        return "".join(listAll)

    def reverseOnlyLetters(self, S):
        r = [s for s in S if s.isalpha()]
        return "".join(S[i] if not S[i].isalpha() else r.pop() for i in range(len(S)))

a = Solution
import unittest
class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(a.reverseOnlyLetters(self, "ab-cd"), "dc-ba")

if __name__ == '__main__':
    unittest.main()
