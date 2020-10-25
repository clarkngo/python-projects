# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        lst = []
        return self._helper(root, lst)

    def _helper(self, start: TreeNode, traversal: List[int]) -> List[int]:
        if start:
            traversal = self._helper(start.left, traversal)
            traversal.append(start.val)
            traversal = self._helper(start.right, traversal)
        return traversal
