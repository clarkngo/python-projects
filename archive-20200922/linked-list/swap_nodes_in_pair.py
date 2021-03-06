# https://leetcode.com/problems/swap-nodes-in-pairs/

# Swap Nodes in Pairs

# Given a linked list, swap every two adjacent nodes and return its head.

# You may not modify the values in the list's nodes, only nodes itself may be changed.

# Example:

# Given 1->2->3->4, you should return the list as 2->1->4->3.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Dummy node acts as the prevNode for the head node
        # of the list and hence stores pointer to the head node.
        dummy = ListNode(-1)
        dummy.next = head

        prev_node = dummy

        while head and head.next:

            # Nodes to be swapped
            first_node = head;
            second_node = head.next;

            # Swapping
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            # Reinitializing the head and prev_node for next swap
            prev_node = first_node
            head = first_node.next

        # Return the new head node.
        return dummy.next

"""
Explanation:

The following variables I would use:
dummy_node = to store pointer of head node
prev_node = node to point to the 1st node of the next pair
first_node = 1st node of the current pair
second_node = 2nd node of the current pair

Initialization:
dummy_node points to head node
prev_node stores dummy_node

LOOP while my pair of nodes is not None:

Prepare first_node and second_node

Swapping part:
Let prev_node point to second_node
Let first_node point to second_node.next (which is the next pair's 1st node)
Let second_node point to first_node

Reinitialization:
prev_node stores the first_node
head stores the first_node.next (which is the next pair's 1st node)

END LOOP

return dummy's pointer, which is head.
"""
