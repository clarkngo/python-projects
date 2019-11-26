class Node:
	def __init__(self, val=None):
		self.val = val
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = Node()
		self.length = 0


	def get(self, index: int) -> int:
		if index >= self.length or index < 0:
			return -1
		else: # index < self.length
			cur = self.head
			for i in range(index):
				cur = cur.next
		return cur.val

	def addAtHead(self, val: int) -> int:
		self.length += 1
		if self.head.val == None:
			self.head = Node(val)
		else:
			new_node = Node(val)
			new_node.next = self.head
			self.head = new_node

	def addAtTail(self, val: int) -> int:
		self.length += 1
		cur = self.head
		while cur.next != None:
			cur = cur.next
		cur.next = Node(val)

	def addAtIndex(self, index: int, val: int) -> int:
		new_node = Node(val)
		if index == 0:
			self.addAtHead(new_node)
		if index == self.length:
			self.addAtTail(new_node)

		cur = self.head
		previous = self.head
		for i in range(index):
			new_node.next
			previous.next
		cur = cur.next
		previous.next = new_node
		new_node.next = cur
		self.length +=1

	def deleteAtIndex(self, index: int) -> None:
		cur = self.head
		previous = self.head
		for i in range(index-1):
			cur = cur.next
			previous = previous.next
		cur = cur.next
		previous.next = cur.next
		self.length -= 1

	def printLinkedList(self) -> None:
		"""
		Print linked list node's value
		"""
		if self.head != None:
			cur = self.head
			strng = str(cur.val)
			while cur.next != None:
				cur = cur.next
				strng += ("->" + str(cur.val))
			strng += ("->" + str(cur.next))
			print(strng)

obj = LinkedList()
obj.addAtHead(2)
obj.addAtTail(22)
obj.addAtTail(3)
obj.addAtIndex(1,1000)
obj.deleteAtIndex(1)
obj.printLinkedList()

