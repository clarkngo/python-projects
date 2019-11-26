class MyLinkedList:
	def __init__(self):
		self.size = 0
		self.head = ListNode(0) # sentinel node as pseudo-head

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None
