# Source: https://leetcode.com/problems/middle-of-the-linked-list/
# Middle of the Linked list

# Given a non-empty, singly linked list with head node head, return a middle node of linked list.

# If there are two middle nodes, return the second middle node.



# Example 1:

# Input: [1,2,3,4,5]
# Output: Node 3 from this list (Serialization: [3,4,5])
# The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
# Note that we returned a ListNode object ans, such that:
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
# Example 2:

# Input: [1,2,3,4,5,6]
# Output: Node 4 from this list (Serialization: [4,5,6])
# Since the list has two middle nodes with values 3 and 4, we return the second one.


# Note:

# The number of nodes in the given list will be between 1 and 100.

# Runtime: 24 ms, faster than 97.36% of Python3 online submissions for Middle of the Linked List.
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Middle of the Linked List.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        print(fast)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.val

one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)
one.next = two
two.next = three
three.next = four
four.next = five
# six = ListNode(6)
# five.next = six

a = Solution()
print(a.middleNode(one))
