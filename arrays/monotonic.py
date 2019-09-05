# Source: https://leetcode.com/problems/monotonic-array/

# Monotonic Array

# An array A is monotone increasing if for all i <= j, A[i] <= A[j].
# An array A is monotone decreasing if for all i <= j, A[i] >= A[j].
# Return true if and only if the given array A is monotonic.

# Example 1:
# Input: [1,2,2,3]
# Output: true

# Example 2:
# Input: [6,5,4,4]
# Output: true

# Example 3:
# Input: [1,3,2]
# Output: false

# Runtime: 576 ms, faster than 36.61% of Python3 online submissions for Monotonic Array.
# Memory Usage: 19.7 MB, less than 5.26% of Python3 online submissions for Monotonic Array.


import unittest # unit test framework
from typing import List

class Solution:
    def isMonotonic(self, A: int) -> bool:
      increasing = A.copy()
      increasing.sort()
      decreasing = A.copy()
      decreasing.sort(reverse=True)
      if increasing == A or decreasing == A:
        return True
      else:
        return False

a = Solution
class Test(unittest.TestCase):

    def test_increasing(self):
        self.assertEqual(a.isMonotonic(self, [1,2,2,3]), True)

    def test_decreasing(self):
        self.assertEqual(a.isMonotonic(self, [6,5,4,4]), True)

    def test_one_element(self):
        self.assertEqual(a.isMonotonic(self, [0]), True)

    def test_empty_list(self):
        self.assertEqual(a.isMonotonic(self, []), True)

    def test_no_order(self):
        self.assertEqual(a.isMonotonic(self, [1,3,2]), False)

    def test_no_order(self):
        self.assertEqual(a.isMonotonic(self, [2,3,1]), False)

if __name__ == '__main__':
    unittest.main()
