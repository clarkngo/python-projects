https://leetcode.com/problems/palindrome-linked-list/

Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        cur = head
        lst = []
        while cur:
            lst.append(cur.val)
            cur = cur.next
        for i in range(len(lst)//2):
            if lst.pop(0) != lst.pop(-1):
                return False
        return True
