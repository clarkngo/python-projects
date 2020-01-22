# https://leetcode.com/problems/linked-list-cycle/

# Linked List Cycle

# Given a linked list, determine if it has a cycle in it.

# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.



# Example 1:

# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the second node.


# Example 2:

# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the first node.


# Example 3:

# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.




# Follow up:

# Can you solve it using O(1) (i.e. constant) memory?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Runtime: 48 ms, faster than 62.74% of Python3 online submissions for Linked List Cycle.
# Memory Usage: 15.8 MB, less than 100.00% of Python3 online submissions for Linked List Cycle.
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        cur = head
        my_dict = {}
        pos = 0
        while cur:
            if cur in my_dict:
                return True
            my_dict[(cur)] = pos
            pos += 1
            cur = cur.next
        return False

  # Except-ionally fast Python
  def hasCycle(self, head):
      try:
          slow = head
          fast = head.next
          while slow is not fast:
              slow = slow.next
              fast = fast.next.next
          return True
      except:
          return False

  # Here is the same thing but without try/except, using the explicit cases instead:

  def hasCycle(self, head):
      if not head:
          return False
      slow = head
      fast = head.next
      while slow is not fast:
          if slow is None or fast is None or fast.next is None:
              return False
          fast = fast.next.next
          slow = slow.next
      return True