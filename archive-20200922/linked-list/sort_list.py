https://leetcode.com/problems/sort-list/

Sort List

Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Runtime: 76 ms, faster than 99.61% of Python3 online submissions for Sort List.
# Memory Usage: 20.2 MB, less than 100.00% of Python3 online submissions for Sort List.

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        lst = []
        cur = head

        while cur:
            lst.append(cur.val)
            cur = cur.next
        lst.sort()
        cur = head
        for i in range(len(lst)):
            cur.val = lst[i]
            cur = cur.next
        return head
