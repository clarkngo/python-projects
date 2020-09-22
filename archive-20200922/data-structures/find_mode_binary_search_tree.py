# https://leetcode.com/problems/find-mode-in-binary-search-tree/

# Find Mode in Binary Search Tree

# Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.


# For example:
# Given BST [1,null,2,2],

#    1
#     \
#      2
#     /
#    2


# return [2].

# Note: If a tree has more than one mode, you can return them in any order.

# Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).

# Runtime: 5572 ms, faster than 5.03% of Python3 online submissions for Find Mode in Binary Search Tree.
# Memory Usage: 17.1 MB, less than 100.00% of Python3 online submissions for Find Mode in Binary Search Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        A = self.preorderTraversal(root)
        from collections import Counter

        data = Counter(A)
        get_mode = dict(data)
        mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
        return mode

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        lst = []
        return self._helper(root, lst)

    def _helper(self, start: TreeNode, traversal: List[int]) -> List[int]:
        if start:
            traversal.append(start.val)
            traversal = self._helper(start.left, traversal)
            traversal = self._helper(start.right, traversal)
        return traversal
