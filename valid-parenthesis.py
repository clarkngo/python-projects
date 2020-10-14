class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1: return False
        my_dict = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for i in range(len(s)):
            if len(stack) > 0 and my_dict[stack[-1]] == s[i]:
                stack.pop()
            elif s[i] in my_dict:
                stack.append(s[i])
            else:
                return False
        return False if len(stack) > 0 else True