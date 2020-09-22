# Source: https://leetcode.com/problems/add-binary/submissions/

# Given two binary strings, return their sum (also a binary string).

# The input strings are both non-empty and contains only characters 1 or 0.

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

# Runtime: 48 ms, faster than 17.72% of Python3 online submissions for Add Binary.
# Memory Usage: 14 MB, less than 5.41% of Python3 online submissions for Add Binary.

class Solution:
    def addBinary(self, x: str, y: str) -> str:
        max_len = max(len(x), len(y))

        x = x.zfill(max_len)
        y = y.zfill(max_len)

        result = ''
        carry = 0

        for i in range(max_len-1, -1, -1):
            r = carry
            r += 1 if x[i] == '1' else 0
            r += 1 if y[i] == '1' else 0
            result = ('1' if r % 2 == 1 else '0') + result
            carry = 0 if r < 2 else 1

        if carry !=0 : result = '1' + result

        return result.zfill(max_len)
