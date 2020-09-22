# Break a Palindrome
# User Accepted:1201
# User Tried:1478
# Total Accepted:1224
# Total Submissions:4001
# Difficulty:Medium
# Given a palindromic string palindrome, replace exactly one character by any lowercase English letter so that the string becomes the lexicographically smallest possible string that isn't a palindrome.

# After doing so, return the final string.  If there is no way to do so, return the empty string.



# Example 1:

# Input: palindrome = "abccba"
# Output: "aaccba"
# Example 2:

# Input: palindrome = "a"
# Output: ""


# Constraints:

# 1 <= palindrome.length <= 1000
# palindrome consists of only lowercase English letters.

class Solution(object):
    def breakPalindrome(self, s):
        n = len(s)
        A = list(s)
        if n == 1: return ""

        for i in range(n):
            if A[i] != 'a':
                old = A[i]
                A[i] = 'a'
                if A != A[::-1]:
                    return "".join(A)
                A[i] = old

            if A[i] != 'b' and A[i] > 'b':
                old = A[i]
                A[i] = 'b'
                if A != A[::-1]:
                    return "".join(A)
                A[i] = old

        ans = "".join(A) if A != A[::-1] else None
        for i in range(n-1, -1,-1):
            if A[i] != 'b':
                old = A[i]
                A[i] = 'b'
                if A != A[::-1]:
                    cand = "".join(A)
                    if ans is None:
                        ans = cand
                    elif cand < ans:
                        ans = cand

                A[i] = old

        return ans if ans is not None else ""
