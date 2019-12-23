# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Given a binary tree, return the postorder traversal of its nodes' values.

# Example:

# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# Output: [3,2,1]
# Follow up: Recursive solution is trivial, could you do it iteratively?

# Runtime: 20 ms, faster than 98.66% of Python3 online submissions for Binary Tree Postorder Traversal.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Binary Tree Postorder Traversal.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        lst = []
        return self._helper(root, lst)

    def _helper(self, start: TreeNode, traversal: List[int]) -> List[int]:
        if start:
            traversal = self._helper(start.left, traversal)
            traversal = self._helper(start.right, traversal)
            traversal.append(start.val)
        return traversal
