

# Source: https://www.freecodecamp.org/news/python-interview-question-guide-how-to-code-a-linked-list-fd77cbbd367d/
class linkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

# create individual nodes
node1 = linkedListNode("3")
node2 = linkedListNode("7")
node3 = linkedListNode("10")

# connect the nodes
node1.nextNode = node2
node2.nextNode = node3

node1.value                     # 3
node1.nextNode.value            # 7
node1.nextNode.nextNode.value   # 10

# If you’re doing a programming interview, and you get asked a Linked List question, you’re not going to be given all the nodes.

# All you’ll get is the head node.

# class Solution(object):
#     def linkedListSolution(self, head):

# currentNode = head

currentNode = node1
# Traverse linked list
def traverse(currentNode):
    while currentNode is not None:
        # reassigning ‘currentNode’ to our current node’s neighbor
        print (currentNode.value)
        currentNode = currentNode.nextNode

# Inserting elements
node4 = linkedListNode("4")
node3.nextNode = node4

# if given only head node, insert a node at the tail
def insertNode(head, valueToInsert):
    currentNode = head
    while currentNode is not None:
      if currentNode.nextNode is None:
          currentNode.nextNode = linkedListNode(valueToInsert)
          return head
      currentNode = currentNode.nextNode

def deleteNode(head, valueToDelete):
    currentNode = head
    previousNode = None
    while currentNode is not None:
        if currentNode.value == valueToDelete:
            if previousNode is None:
                newHead = currentNode.nextNode
                currentNode.nextNode = None
                return newHead  # Deleted the head
            previousNode.nextNode = currentNode.nextNode
            return head
            previousNode = currentNode
            currentNode = currentNode.nextNode
            return head # Value to delete was not found.


node5 = linkedListNode("5")
insertNode(node1, "5")
traverse(node1)
deleteNode(node1, "10")
traverse(node1)

