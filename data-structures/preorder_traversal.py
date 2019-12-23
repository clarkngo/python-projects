# https://leetcode.com/problems/binary-tree-preorder-traversal/

# Binary Tree Preorder Traversal

# Given a binary tree, return the preorder traversal of its nodes' values.

# Example:

# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# Output: [1,2,3]
# Follow up: Recursive solution is trivial, could you do it iteratively?

# Runtime: 32 ms, faster than 60.54% of Python3 online submissions for Binary Tree Preorder Traversal.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Binary Tree Preorder Traversal.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        lst = []
        return self._helper(root, lst)

    def _helper(self, start: TreeNode, traversal: List[int]) -> List[int]:
        if start:
            traversal.append(start.val)
            traversal = self._helper(start.left, traversal)
            traversal = self._helper(start.right, traversal)
        return traversal
