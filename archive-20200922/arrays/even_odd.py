from typing import *

class Solution:
	def even_odd(self, A: List[int]) -> List[int]:
		next_even, next_odd = 0, len(A) - 1
		while next_even < next_odd:
			# move left pointer if even
			if A[next_even] % 2 == 0:
				next_even += 1
			# swap left pointer value with right pointer value
			# move right pointer
			else:
				A[next_even], A[next_odd] = A[next_odd], A[next_even]
				next_odd -= 1
		return A

import unittest

a = Solution()


class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(a.even_odd([1,2,3,4,5,6,7,8,9]), [8,2,6,4,5,7,3,9,1])

if __name__ == '__main__':
	unittest.main()
