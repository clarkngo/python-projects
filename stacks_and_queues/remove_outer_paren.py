# Source: https://leetcode.com/problems/remove-outermost-parentheses/submissions/

# Remove Outermost Parentheses

# A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

# A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

# Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

# Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.



# Example 1:

# Input: "(()())(())"
# Output: "()()()"
# Explanation:
# The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
# After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

# Runtime: 28 ms, faster than 84.97% of Python online submissions for Remove Outermost Parentheses.
# Memory Usage: 12 MB, less than 61.54% of Python online submissions for Remove Outermost Parentheses.

class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        list_s = list(S)
        i, n = 0, len(S)
        stack, outer_start = [], 0
        while i < n:
            if list_s[i] == '(':
                stack.append('(')
            else:
                stack.pop()
            if not stack:
                outer_end = i
                list_s[outer_start], list_s[outer_end] = '', ''
                outer_start = i + 1
            i += 1
        return ''.join(list_s)


a = Solution

import unittest

class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(a.removeOuterParentheses(self, "(())"), "()")

    def test2(self):
        self.assertEqual(a.removeOuterParentheses(self, "(())(())"), "()()")

if __name__ == '__main__':
    unittest.main()
