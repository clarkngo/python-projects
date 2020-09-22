# Maximum Product of Splitted Binary Tree
# User Accepted:1534
# User Tried:2306
# Total Accepted:1572
# Total Submissions:5681
# Difficulty:Medium
# Given a binary tree root. Split the binary tree into two subtrees by removing 1 edge such that the product of the sums of the subtrees are maximized.

# Since the answer may be too large, return it modulo 10^9 + 7.



# Example 1:



# Input: root = [1,2,3,4,5,6]
# Output: 110
# Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)
# Example 2:



# Input: root = [1,null,2,3,4,null,null,5,6]
# Output: 90
# Explanation:  Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
# Example 3:

# Input: root = [2,3,9,10,7,8,6,5,4,11,1]
# Output: 1025
# Example 4:

# Input: root = [1,1]
# Output: 1


# Constraints:

# Each tree has at most 50000 nodes and at least 2 nodes.
# Each node's value is between [1, 10000].

# LeetCode
# Explore
# Problems
# Mock
# Contest
# Articles
# Discuss
#  Store
# New Playground
# clarkngo
# 5330. Maximum Product of Splitted Binary Tree
# User Accepted:1534
# User Tried:2306
# Total Accepted:1572
# Total Submissions:5681
# Difficulty:Medium
# Given a binary tree root. Split the binary tree into two subtrees by removing 1 edge such that the product of the sums of the subtrees are maximized.

# Since the answer may be too large, return it modulo 10^9 + 7.



# Example 1:



# Input: root = [1,2,3,4,5,6]
# Output: 110
# Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)
# Example 2:



# Input: root = [1,null,2,3,4,null,null,5,6]
# Output: 90
# Explanation:  Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
# Example 3:

# Input: root = [2,3,9,10,7,8,6,5,4,11,1]
# Output: 1025
# Example 4:

# Input: root = [1,1]
# Output: 1


# Constraints:

# Each tree has at most 50000 nodes and at least 2 nodes.
# Each node's value is between [1, 10000].
# Python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# UNSOLVED
class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        import functools
        cur = root
        val = root.val
        while cur:
            if cur.left and cur.right:
                break
            elif cur.left:
                cur = cur.left
            elif cur.right:
                cur = cur.right
            val += cur.val

        root1 = cur.right
        root2 = cur.left
        if root1.left and root1.right:
            root2.val += val
        elif root2.left and root2.right:
            root1.val += val
        lst1 = self.preorderTraversal(root1)
        lst2 = self.preorderTraversal(root2)
        a = functools.reduce(lambda a,b : a+b,lst1)
        b = functools.reduce(lambda a,b : a+b,lst2)
        return a * b

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        lst = []
        return self._helper(root, lst)

    def _helper(self, start: TreeNode, traversal: List[int]) -> List[int]:
        if start:
            traversal.append(start.val)
            traversal = self._helper(start.left, traversal)
            traversal = self._helper(start.right, traversal)
        return traversal
