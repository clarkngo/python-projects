# https://leetcode.com/problems/reverse-string/

# Reverse String

# Write a function that reverses a string. The input string is given as an array of characters char[].

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# You may assume all the characters consist of printable ascii characters.

# Example 1:

# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

# Runtime: 216 ms, faster than 80.42% of Python3 online submissions for Reverse String.
# Memory Usage: 17.2 MB, less than 98.84% of Python3 online submissions for Reverse String.

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        LENGTH = len(s)
        if LENGTH == 1: return s
        for i in range(len(s)//2):
            s[i], s[LENGTH - 1 - i] =  s[LENGTH - 1 - i], s[i]
        return s
