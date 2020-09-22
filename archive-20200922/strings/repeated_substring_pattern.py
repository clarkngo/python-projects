# https://leetcode.com/problems/repeated-substring-pattern/

# Repeated Substring Pattern

# Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.



# Example 1:

# Input: "abab"
# Output: True
# Explanation: It's the substring "ab" twice.
# Example 2:

# Input: "aba"
# Output: False
# Example 3:

# Input: "abcabcabcabc"
# Output: True
# Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

# Runtime: 24 ms, faster than 98.21% of Python3 online submissions for Repeated Substring Pattern.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Repeated Substring Pattern.

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # s1: create a string with the double of the input string (s + s)
        # s2: remove the first character and last character of s1
        # find if input string exists in s2
        s1 = s + s
        s2 = s1[1:-1]
        return s2.find(s) != -1

def repeatedSubstringPattern(self, str):
    return str in (2 * str)[1:-1]
