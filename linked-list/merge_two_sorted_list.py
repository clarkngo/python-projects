# Source: https://leetcode.com/problems/merge-two-sorted-lists/
# Merge Two Sorted Lists

# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.

# Runtime: 24 ms, faster than 99.82% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Merge Two Sorted Lists.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None: return l2
        if l2 is None: return l1
        if l1 is None and l2 is None: return None

        head = ListNode(-1)
        cur = head

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next

            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1: cur.next = l1
        if l2: cur.next = l2
        return head.next
