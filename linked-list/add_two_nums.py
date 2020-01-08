# https://leetcode.com/problems/add-two-numbers/

# Add Two Numbers

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Runtime: 60 ms, faster than 92.82% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Add Two Numbers.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        prev = result = ListNode(None)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            prev.next = ListNode(carry % 10)
            prev = prev.next
            carry //= 10
        return result.next


    # solve for recursion
    # def add(node0, node1, carry = 0):
    #     if not node0 and not node1 and not carry:
    #         return None

    #     node0_val = node0.data if node0 else 0
    #     node1_val = node1.data if node1 else 0
    #     total = node0_val +node1_val + carry

    #     node0_next = node0.next if node0 else None
    #     node1_next = node1,next if node1 else None
    #     carry_next = 1 if total >= 10 else 0

    #     return Node(total % 10, add(node0_next, node1_next, carry_next))
