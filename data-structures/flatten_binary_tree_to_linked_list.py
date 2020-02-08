"""
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

Flatten Binary Tree to Linked List

Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

Runtime: 36 ms, faster than 63.55% of Python3 online submissions for Flatten Binary Tree to Linked List.
Memory Usage: 13.6 MB, less than 8.70% of Python3 online submissions for Flatten Binary Tree to Linked List.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        cur = root
        lst = self.preorder(root)
        root = TreeNode(lst[0])
        for i in range(1, len(lst)):
            cur.left = None
            cur.right = TreeNode(lst[i])
            cur = cur.right

    def preorder(self, root: TreeNode) -> List[int]:
        lst = []
        return self._helper(root, lst)

    def _helper(self, start: TreeNode, traversal: List[int]) -> List[int]:
        if start:
            traversal.append(start.val)
            traversal = self._helper(start.left, traversal)
            traversal = self._helper(start.right, traversal)
        return traversal
