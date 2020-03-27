# Source: https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

# Pairs of Songs With Total Durations Divisible by 60

# In a list of songs, the i-th song has a duration of time[i] seconds.

# Return the number of pairs of songs for which their total duration in seconds is divisible by 60.  Formally, we want the number of indices i < j with (time[i] + time[j]) % 60 == 0.

# Example 1:

# Input: [30,20,150,100,40]
# Output: 3
# Explanation: Three pairs have a total duration divisible by 60:
# (time[0] = 30, time[2] = 150): total duration 180
# (time[1] = 20, time[3] = 100): total duration 120
# (time[1] = 20, time[4] = 40): total duration 60
# Example 2:

# Input: [60,60,60]
# Output: 3
# Explanation: All three pairs have a total duration of 120, which is divisible by 60.


# Note:

# 1 <= time.length <= 60000
# 1 <= time[i] <= 500

from typing import List
import collections
class Solution:
	# Time Limit Exceeded
	# def numPairsDivisibleBy60(self, time: List[int]) -> int:
	# 	count = 0
	# 	for i in range(len(time)):
	# 		for j in range(i+1, len(time)):
	# 			# print(time[i], end=" ")
	# 			# print(time[j])
	# 			if (time[i] + time[j]) % 60 == 0:
	# 				count += 1
	# 	return count
	def numPairsDivisibleBy60(self, time: List[int]) -> int:
		c = collections.Counter()
		res = 0
		for t in time:
			res += c[-t % 60]
			print(c[-t%60])
			c[t % 60] += 1
		return res
	# def numPairsDivisibleBy60(self, time: List[int]) -> int:
	# 	c = collections.Counter()
	# 	res = 0
	# 	for t in time:
	# 		res += c[-t % 60]
	# 		c[t % 60] += 1
	# 	return res

import unittest
a = Solution()
class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(a.numPairsDivisibleBy60([30,20,150,100,40]), 3)

if __name__ == '__main__':
    unittest.main()
