# Source: https://leetcode.com/problems/number-of-equivalent-domino-pairs/
# Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a==c and b==d), or (a==d and b==c) - that is, one domino can be rotated to be equal to another domino.

# Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

# Example 1:

# Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
# Output: 1


# Constraints:

# 1 <= dominoes.length <= 40000
# 1 <= dominoes[i][j] <= 9

# Runtime: 280 ms, faster than 58.49% of Python3 online submissions for Number of Equivalent Domino Pairs.
# Memory Usage: 22 MB, less than 100.00% of Python3 online submissions for Number of Equivalent Domino Pairs.

from typing import *
class Solution:
	# def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
	# 	count_pairs = 0
	# 	for i in range(len(dominoes) - 1):
	# 		if dominoes[i][0] > dominoes[i][1]:
	# 			dominoes[i][0], dominoes[i][1] = dominoes[i][1], dominoes[i][0]
	# 		if dominoes[i+1][0] > dominoes[i+1][1]:
	# 			dominoes[i+1][0], dominoes[i+1][1] = dominoes[i+1][1], dominoes[i+1][0]
	# 		# print(dominoes[i], dominoes[i+1])
	# 		if dominoes[i] == dominoes[i+1]:
	# 			count_pairs +=1
	# 	return count_pairs

	def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
		dom_dict = {}
		for i in range(len(dominoes)):
			if dominoes[i][0] > dominoes[i][1]:
				dominoes[i][0], dominoes[i][1] = dominoes[i][1], dominoes[i][0]
			if str(dominoes[i]) not in dom_dict:
				dom_dict[str(dominoes[i])] = 1
			else:
				dom_dict[str(dominoes[i])] += 1
		dom_dict = {key:val for key, val in dom_dict.items() if val > 1}
		# print(dom_dict)
		sum = 0
		for key,val in dom_dict.items():
			while val != 1:
				sum += val - 1
				val -= 1
		return sum

	## how about sum of pairs?

import unittest
a = Solution()
class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(a.numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]), 1)
	def test2(self):
		self.assertEqual(a.numEquivDominoPairs([[1,2],[1,2],[1,1],[1,2],[2,2]]), 3)
	def test3(self):
		self.assertEqual(a.numEquivDominoPairs([[1,1],[2,2],[1,1],[1,2],[1,2],[1,1]]), 4)
	def test4(self):
		self.assertEqual(a.numEquivDominoPairs([[2,1],[1,2],[1,2],[1,2],[2,1],[1,1],[1,2],[2,2]]), 15)
	def test5(self):
		self.assertEqual(a.numEquivDominoPairs([[2,1],[1,2],[1,2],[1,2],[2,1],[1,1],[1,2],[2,2],[2,2]]), 16)

if __name__ == '__main__':
    unittest.main()
