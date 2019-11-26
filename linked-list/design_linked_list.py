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
# If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list.
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


# Runtime: 2524 ms, faster than 5.00% of Python online submissions for Design Linked List.
# Memory Usage: 12.5 MB, less than 33.33% of Python online submissions for Design Linked List.

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node()  # a new empty node is create whenever you create a new linked list

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """

        cur = self.head     # current node starts at the head
        pointer = 0         # pointer to know which node/index we are currently at

        if index == 0:
            return cur.val
        elif index > self.getLength():
            return -1       # invalid index
        else:
            while cur.next != None:
                pointer += 1            # move the pointer
                if index == pointer:
                    return cur.next.val # return value of node if pointer reached the index
                cur = cur.next

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        """

        # if no new node is inserted yet
        # overwrite the head as head starts with val=None and next=None
        if self.head.val == None:
            self.head = Node(val)
        # there's at least 1 node with value
        else:
            new_node = Node(val)
            new_node.next = self.head   # let the new node point to the head node
            self.head = new_node        # let new node be the new head node

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        cur = self.head
        # iterate until you reach the tail
        while cur.next != None:
            cur = cur.next
        cur.next = Node(val)


    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        """
        new_node = Node(val)
        cur = self.head
        previous = self.head
        pointer = 0

        if index == 0:
            new_node.next = cur
            self.head = new_node


        elif index <= self.getLength():
            pointer += 1
            while pointer < index:
                cur = cur.next
                previous = previous.next
                pointer += 1
            cur = cur.next
            previous.next = new_node
            new_node.next = cur


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        cur = self.head
        previous = self.head
        pointer = 0
        if index == 0:
            self.head = cur.next
        elif index < self.getLength():
            pointer += 1
            while pointer < index:
                cur = cur.next
                previous = previous.next
                pointer += 1
            cur = cur.next
            previous.next = cur.next


    def getLength(self) -> int:
        length = 0
        # if no node exist
        if self.head.val == None:
            return length

        cur = self.head
        length = 1  # start with head node
        # iterate until tail
        while cur.next != None:
            cur = cur.next
            length += 1

        return length


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



# obj = MyLinkedList()
# obj.addAtHead(6)
# obj.addAtHead(5)
# obj.addAtTail(2)
# obj.addAtIndex(5,1)
# obj.addAtIndex(0,22)
# obj.addAtIndex(1,15)
# obj.deleteAtIndex(0)
# obj.printLinkedList()
# obj.deleteAtIndex(2)
# obj.printLinkedList()

obj = MyLinkedList()
# print(obj.getLength())
print(obj.get(22))
obj.addAtHead(2)
obj.deleteAtIndex(1)
obj.addAtTail(22)
# print(obj.getLength())
obj.printLinkedList()
