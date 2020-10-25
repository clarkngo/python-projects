# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        """
        Given singly linked list, group all odd nodes together followed by
        even nodes.
        
        O(1) Space
        O(n) Time
        """
        # edge case for length of linked list 0 to 2
        if not head or head.next == None or head.next.next == None:
            return head
        odd_head, even_head = head, head.next
        # connect linked list of odds
        # connect linked list of evens
        cur_odd, cur_even = odd_head, even_head
        while cur_odd and cur_odd.next and cur_even and cur_even.next:
            cur_odd.next, cur_even.next = cur_odd.next.next, cur_even.next.next
            cur_odd, cur_even = cur_odd.next, cur_even.next
        # combine two linked lists
        cur_odd.next = even_head
        return odd_head
