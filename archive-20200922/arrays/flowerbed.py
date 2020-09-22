# Source: https://leetcode.com/problems/can-place-flowers/
# Can Place Flowers

# Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

# Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: True
# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: False
# Note:
# The input array won't violate no-adjacent-flowers rule.
# The input array size is in the range of [1, 20000].
# n is a non-negative integer which won't exceed the input array size.

# Runtime: 188 ms, faster than 76.49% of Python3 online submissions for Can Place Flowers.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Can Place Flowers.

from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0: return True
        flowersToBePlanted = n
        before, after = 0, 2
        if len(flowerbed) == 1 and flowerbed[0] == 0 and n >= 1:
            return True
        if flowerbed[0] == 0 and flowerbed[1] == 0:
          flowerbed[0] = 1
          flowersToBePlanted -= 1
        if flowerbed[len(flowerbed)-2] == 0 and flowerbed[len(flowerbed)-1] == 0 and n >= 1:
          flowerbed[len(flowerbed)-1] = 1
          flowersToBePlanted -= 1
        if flowersToBePlanted <= 0:
            return True
        for current in range(1, len(flowerbed)-1):
            if flowerbed[before] == 0 and flowerbed[after] == 0:
                if flowerbed[current] == 0:
                  flowerbed[current] = 1
                  flowersToBePlanted -= 1
            if flowersToBePlanted == 0:
                return True
            before += 1
            after += 1
        return False

import unittest
a = Solution()
class Test(unittest.TestCase):
	# def test(self):
	# 	self.assertEqual(a.canPlaceFlowers([1,0,0,0,1],1), True)
	# def test2(self):
	# 	self.assertEqual(a.canPlaceFlowers([1,0,0,0,0,1],2), False)
	# def test3(self):
	# 	self.assertEqual(a.canPlaceFlowers([1,0,1,0,1,0,1],1), False)
	# def test4(self):
	# 	self.assertEqual(a.canPlaceFlowers([0,0,1,0,1],1), True)
	# def test5(self):
	# 	self.assertEqual(a.canPlaceFlowers([1,0,1,0,0],1), True)
	# def test6(self):
	# 	self.assertEqual(a.canPlaceFlowers([0],1), True)
	# def test7(self):
	# 	self.assertEqual(a.canPlaceFlowers([1,0,0],1), True)
	def test8(self):
		self.assertEqual(a.canPlaceFlowers([0,0,1,0,0],1), True)

if __name__ == '__main__':
    unittest.main()

