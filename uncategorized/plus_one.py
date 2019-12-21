# source: https://leetcode.com/problems/plus-one/submissions/

# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Example 1:

# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.

def plusOne(self, digits: List[int]) -> List[int]:
    digits[-1] += 1
    n = len(digits)
    if digits[n-1] > 9:
        for i in range(n, 1, -1):
            digits[n-1] = 0
            digits[n-2] += 1
            n -= 1
            if digits[n-1] < 10:
                break
        if digits[0] == 10:
            digits[0] = 0
            digits.insert(0,1)
    return digits


# Runtime: 44 ms, faster than 18.29% of Python3 online submissions for Plus One.
# Memory Usage: 13.4 MB, less than 5.49% of Python3 online submissions for Plus One.