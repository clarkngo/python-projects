class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class Tree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def add(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._add(value, self.root)

    def _add(self, value, node):
        if value < node.value:
            if node.left != None:
                self._add(value, node.left)
            else:
                node.left = Node(value)
        else:
            if node.right != None:
                self._add(value, node.right)
            else:
                node.right = Node(value)

    def find(self, value):
        if self.root != None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, node):
        if value == node.value:
            return node
        elif value < node.value and node.left != None:
            self._find(value, node.left)
        elif value > node.value and node.right != None:
            self._find(value, node.right)

bt = Tree()
bt.add(2)
bt.add(1)
bt.add(4)
bt.add(5)
bt.add(3)

#     2
#   /    \
#  1     4
#       /  \
#      3    5

print(bt)
print(bt.root.value)
print(bt.root.left.value)
print(bt.root.right.value)
print(bt.root.right.right.value)
print(bt.root.right.left.value)
