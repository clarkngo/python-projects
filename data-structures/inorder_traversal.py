# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Binary Tree Inorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Given a binary tree, return the inorder traversal of its nodes' values.

# Example:

# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# Output: [1,3,2]
# Follow up: Recursive solution is trivial, could you do it iteratively?

# Runtime: 28 ms, faster than 83.36% of Python3 online submissions for Binary Tree Inorder Traversal.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Binary Tree Inorder Traversal.

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        lst = []
        return self._helper(root, lst)

    def _helper(self, start: TreeNode, traversal: List[int]):
        if start:
            traversal = self._helper(start.left, traversal)
            traversal.append(start.val)
            traversal = self._helper(start.right, traversal)
        return traversal
