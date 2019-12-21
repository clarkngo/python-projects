# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

# Convert Binary Number in a Linked List to Integer

# Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

# Return the decimal value of the number in the linked list.

# Runtime: 32 ms, faster than 27.33% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.

# Example 1:


# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10
# Example 2:

# Input: head = [0]
# Output: 0
# Example 3:

# Input: head = [1]
# Output: 1
# Example 4:

# Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
# Output: 18880
# Example 5:

# Input: head = [0,0]
# Output: 0


# Constraints:

# The Linked List is not empty.
# Number of nodes will not exceed 30.
# Each node's value is either 0 or 1.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        cur = head
        binary_nums = []
        decimal_val = 0
        while cur != None:
            binary_nums.append(cur.val)
            cur = cur.next
        j = 0
        for i in range(len(binary_nums)-1,-1,-1):
            decimal_val += binary_nums[i] * 2 ** j
            j += 1
        return decimal_val

# Implementation:

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans = 0
        while head:
            ans = 2*ans + head.val
            head = head.next
        return ans
# Analysis:
# Time complexity O(N)
# Space complexity O(1)
