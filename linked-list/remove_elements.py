# Source: https://leetcode.com/problems/remove-linked-list-elements/
# Remove Linked List Elements

# Remove all elements from a linked list of integers that have value val.

# Example:

# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5

# Runtime: 72 ms, faster than 79.43% of Python3 online submissions for Remove Linked List Elements.
# Memory Usage: 15.5 MB, less than 100.00% of Python3 online submissions for Remove Linked List Elements.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	def removeElements(self, head: ListNode, val: int) -> ListNode:
		head, head.next = ListNode(-1), head
		cur = head
		while cur.next:
			if cur.next.val == val:
				cur.next = cur.next.next
			else:
				cur = cur.next
		return head.next

	def printLinkedList(self, head: ListNode) -> None:
		strng = ""
		cur = head
		strng += str(cur.val)
		if (head.next == None):
			print(strng)
			return
		cur = cur.next
		while cur.next != None:
			strng += "->" + str(cur.val)
			cur = cur.next
		strng += "->" + str(cur.val)
		print(strng)

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(6)
node4 = ListNode(3)
node5 = ListNode(4)
node6 = ListNode(5)
node7 = ListNode(6)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
linkedlist1 = node1

node1 = ListNode(6)
node2 = ListNode(6)
node3 = ListNode(6)
node4 = ListNode(6)
node5 = ListNode(6)
node6 = ListNode(6)
node7 = ListNode(6)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
linkedlist2 = node1

node1 = ListNode(1)
node2 = ListNode(6)
node3 = ListNode(6)
node4 = ListNode(6)
node5 = ListNode(6)
node6 = ListNode(6)
node7 = ListNode(6)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
linkedlist3 = node1

a = Solution()
# a.printLinkedList(linkedlist1)
# a.printLinkedList(linkedlist2)
# a.removeElements(linkedlist2, 6)
# a.printLinkedList(linkedlist2)
a.printLinkedList(linkedlist3)
a.removeElements(linkedlist3, 6)
a.printLinkedList(linkedlist3)
