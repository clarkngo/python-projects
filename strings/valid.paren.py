# Code below will fail in test case: "()[]{}"
# Suggestion, use a stack.
#
# class Solution:
#     def isValid(self, s: str) -> bool:
#         if len(s) <= 1 or len(s) % 2 != 0:
#             return False
#         j = len(s) - 1
#         for i in range(len(s) // 2):
#             if s[i] == '(':
#                 if s[j] == ')':
#                     j -= 1
#                     continue
#             elif s[i] == '[':
#                 if s[j] == ']':
#                     j -= 1
#                     continue
#                 else:
#                     return False
#             elif s[i] == '{':
#                 if s[j] == '}':
#                     j -= 1
#                     continue
#             else:
#                 return False
#         return True

# Source: https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(s: str) -> bool:
        stack = []
        if len(s) == 1 or len(s) % 2 == 1:
            return False
        elif len(s) == 0:
            return True
        else:
            if s[0] == ')' or s[0] == '}' or s[0] == ']':
                return False
            else:
                for i in range(len(s)):
                    if s[i] == '(' or s[i] == '{' or s[i] == '[':
                        stack.append(s[i])
                    elif (stack[-1] == '(' and s[i] == ')') or (stack[-1] == '{' and s[i] == '}') or (stack[-1] == '[' and s[i] == ']'):
                        stack.pop()
                        continue
                    else:
                        return False
        if stack:
            return False
        return True

a = Solution
print("Passed" if a.isValid('') == True else "Failed")
print("Passed" if a.isValid('()') == True else "Failed")
print("Passed" if a.isValid('()[]') == True else "Failed")
print("Passed" if a.isValid('{()}') == True else "Failed")
print("Passed" if a.isValid('{') == False else "Failed")
print("Passed" if a.isValid('}') == False else "Failed")
print("Passed" if a.isValid('(})') == False else "Failed")
print("Passed" if a.isValid('[]}') == False else "Failed")
print("Passed" if a.isValid('((') == False else "Failed")
