# Source: https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Remove Duplicates from Sorted List

# Given a sorted linked list, delete all duplicates such that each element appear only once.

# Example 1:

# Input: 1->1->2
# Output: 1->2
# Example 2:

# Input: 1->1->2->3->3
# Output: 1->2->3

# Runtime: 40 ms, faster than 91.17% of Python3 online submissions for Remove Duplicates from Sorted List.
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Remove Duplicates from Sorted List.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None: return None
        cur = head
        while cur.next != None:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

    def deleteDuplicates2(self, head):
            if head and head.next:
                head.next = self.deleteDuplicates2(head.next)
                return head.next if head.next.val == head.val else head
            return head
