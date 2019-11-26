# 707. Design Linked List
# Easy

# 313

# 282

# Favorite

# Share
# Design your implementation of the linked list.
# You can choose to use the singly linked list or the doubly linked list.
# A node in a singly linked list should have two attributes: val and next.
# val is the value of the current node, and next is a pointer/reference to the next node.
# If you want to use the doubly linked list, you will need one more attribute previous to indicate the previous node in the linked list.
# Assume all nodes in the linked list are 0-indexed.

# Implement these functions in your linked list class:

# get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
# addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
# addAtTail(val) : Append a node of value val to the last element of the linked list.
# addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
# deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.
# Example:

# MyLinkedList linkedList = new MyLinkedList();
# linkedList.addAtHead(1);
# linkedList.addAtTail(3);
# linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
# linkedList.get(1);            // returns 2
# linkedList.deleteAtIndex(1);  // now the linked list is 1->3
# linkedList.get(1);            // returns 3
# Note:

# All values will be in the range of [1, 1000].
# The number of operations will be in the range of [1, 1000].
# Please do not use the built-in LinkedList library.


# Runtime: 136 ms, faster than 87.40% of Python online submissions for Design Linked List.
# Memory Usage: 14 MB, less than 33.33% of Python online submissions for Design Linked List.

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        init_node = Node()      # a new empty node is create whenever you create a new linked list
        self.head = init_node
        self.tail = init_node
        self.length = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """

        if index >= self.length:
            return -1       # invalid index
        if index < self.length // 2:
            cur = self.head
            for i in range(index):
                cur = cur.next
        else:   # index >= self.length // 2
            cur = self.tail
            for i in range(self.length - index - 1):
                cur = cur.prev
        return cur.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        """
        self.length += 1
        new_node = Node(val)
        # if no new node is inserted yet
        # overwrite the head as head starts with val=None and next=None
        if self.head.val is None:
            self.head = new_node
            self.tail = new_node
        # there's at least 1 node with value
        else:
            new_node.next = self.head       # let the new node point to the head node
            self.head.prev = new_node   # let existing head point to new node
            self.head = new_node            # move head pointer to new node

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.length += 1
        new_node = Node(val)
        if self.tail.val is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node       # let the tail pointer point to new node
            new_node.prev = self.tail   # let new node point back to tail pointer
            self.tail = new_node            # move tail pointer to new node


    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        """
        new_node = Node(val)

        if index == 0:
            self.addAtHead(val)
            return
        if index == self.length:
            self.addAtTail(val)
            return
        if index > self.length:
            return

        if index < self.length // 2:
            cur = self.head
            for i in range(index - 1):
                cur = cur.next
        else:
            cur = self.tail
            for i in range(self.length - index):
                cur = cur.prev
        new_node.next = cur.next        # new node point to current node next | new node connect to next node
        cur.next = new_node             # new node becomes current node next | cur connects to new node
        new_node.prev = cur             # new node point back to cur node | new node connect to previous node
        new_node.next.prev = new_node   # have the next node point back to new node

        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.length:
            return
        if index == 0:
            self.head = self.head.next      # move head pointer to the next node
            if self.head is not None:
                self.head.prev = None       # set pointer pointing to previous node to None
            self.length -= 1
            return

        if index < self.length // 2:
            cur = self.head
            for i in range(index - 1):
                cur = cur.next

        else: # index >= self.length // 2
            cur = self.tail
            for i in range(self.length - index):
                cur = cur.prev

        if cur.next == self.tail:
            self.tail = cur             # move tail pointer to previous node

        cur.next = cur.next.next        # let current node point to the next, next node. this deletes the cur.next

        if cur.next is not None:
            cur.next.prev = cur         # let the next next node previous pointer to the current node
        self.length -= 1

    def printLinkedList(self) -> None:
        """
        Print linked list node's value
        """
        print("head to tail: ", end= "")
        if self.head != None:
            cur = self.head
            strng = str(cur.val)
            while cur.next != None:
                cur = cur.next
                strng += ("->" + str(cur.val))
            strng += ("->" + str(cur.next))
            print(strng)
        print("tail to head: ", end= "")
        if self.tail != None:
            cur = self.tail
            strng2 = str(cur.val)
            while cur.prev != None:
                cur = cur.prev
                strng2 += ("->" + str(cur.val))
            strng2 += ("->" + str(cur.prev))
            print(strng2)




obj = MyLinkedList()
obj.addAtHead(1)
obj.deleteAtIndex(0)
obj.printLinkedList()
