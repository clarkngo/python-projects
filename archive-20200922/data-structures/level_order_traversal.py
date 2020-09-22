# Recursive Python program for level order traversal of Binary Tree

# A node structure
class Node:

	# A utility function to create a new node
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None


# Function to print level order traversal of tree
def printLevelOrder(root):
	h = height(root)
	for i in range(1, h+1):
		printGivenLevel(root, i)


# Print nodes at a given level
def printGivenLevel(root , level):
	if root is None:
		return
	if level == 1:
		print(root.data)
	elif level > 1 :
		printGivenLevel(root.left , level-1)
		printGivenLevel(root.right , level-1)


""" Compute the height of a tree--the number of nodes
	along the longest path from the root node down to
	the farthest leaf node
"""
def height(node):
	if node is None:
		return 0
	else :
		# Compute the height of each subtree
		lheight = height(node.left)
		rheight = height(node.right)

		#Use the larger one
		if lheight > rheight :
			return lheight+1
		else:
			return rheight+1

# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right.left = Node(10)
root.left.right.right = Node(11)
root.right.left.left = Node(12)
root.right.left.right = Node(13)
root.right.right.left = Node(14)
root.right.right.right = Node(15)

print("Level order traversal of binary tree is -")
printLevelOrder(root)

#This code is contributed by Nikhil Kumar Singh(nickzuck_007)
