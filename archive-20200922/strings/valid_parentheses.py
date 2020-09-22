# Source: https://leetcode.com/problems/valid-parentheses/
# Valid Parentheses

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:

# Input: "()"
# Output: true
# Example 2:

# Input: "()[]{}"
# Output: true
# Example 3:

# Input: "(]"
# Output: false
# Example 4:

# Input: "([)]"
# Output: false
# Example 5:

# Input: "{[]}"
# Output: true

class Solution:
    # def isValid(self, s: str) -> bool:
    #     if s == "": return True
    #     my_dict = {"{":"}","[":"]","(":")"}
    #     # list out keys and values separately
    #     key_list = list(my_dict.keys())
    #     val_list = list(my_dict.values())

    #     stack = []
    #     for i in range(len(s)):
    #         if s[i] in my_dict:
    #             stack.append(s[i])
    #         else:
    #             key = list(my_dict.keys())[list(my_dict.values()).index(s[i])]
    #             if key == stack[-1]:
    #                 stack.pop()
    #             else:
    #                 return False
    #     return True

    def isValid(self, s: str) -> bool:
        if s == "": return True
        stack = []
        for i in range(len(s)):
            if s[i]=="(" or s[i]=="{" or s[i]=="[":
                stack.append(s[i])
            elif stack[-1] == "(" and s[i]==")":
                stack.pop()
            elif stack[-1] == "[" and s[i]=="]":
                stack.pop()
            elif stack[-1] == "{" and s[i]=="}":
                stack.pop()
            else:
                return False
        return True

a = Solution
import unittest
class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(a.isValid(self, "()"), True)
    def test2(self):
        self.assertEqual(a.isValid(self, "()[]{}"), True)
    def test3(self):
        self.assertEqual(a.isValid(self, "(]"), False)
    def test4(self):
        self.assertEqual(a.isValid(self, "([)]"), False)
    def test5(self):
        self.assertEqual(a.isValid(self, "{[]}"), True)

if __name__ == '__main__':
    unittest.main()

