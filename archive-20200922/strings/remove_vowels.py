# Source: https://leetcode.com/problems/remove-vowels-from-a-string/
# Remove Vowels from a String

# Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.



# Example 1:

# Input: "leetcodeisacommunityforcoders"
# Output: "ltcdscmmntyfrcdrs"
# Example 2:

# Input: "aeiou"
# Output: ""


# Note:

# S consists of lowercase English letters only.
# 1 <= S.length <= 1000

# Runtime: 24 ms, faster than 96.95% of Python3 online submissions for Remove Vowels from a String.
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Remove Vowels from a String.

class Solution:
    def removeVowels(self, S: str) -> str:
        lst = []
        for s in S:
            if s != 'a' and s != 'e' and s != 'i' and s != 'o' and s != 'u':
                lst.append(s)

        return "".join(lst)

# Runtime: 24 ms, faster than 96.95% of Python3 online submissions for Remove Vowels from a String.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Remove Vowels from a String.

    def removeVowels2(self, S: str) -> str:
        s = set('aeiou')
        ret = ""
        for ch in S:
            if ch not in s:
                ret += ch
        return ret
