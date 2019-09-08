# Source: https://leetcode.com/problems/binary-search/

# Binary Search

# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1


# Note:

# You may assume that all elements in nums are unique.
# n will be in the range [1, 10000].
# The value of each element in nums will be in the range [-9999, 9999].

# Runtime: 292 ms, faster than 37.04% of Python3 online submissions for Binary Search.
# Memory Usage: 15 MB, less than 6.45% of Python3 online submissions for Binary Search.

import unittest
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        found = False
        l = 0
        r = len(nums) - 1
        while l <= r and not found:
            mid = (l + r) // 2
            if nums[mid] == target:
                found = True
            else:
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
        if found:
           return mid
        else:
            return - 1

a = Solution
class Test(unittest.TestCase):

    def test_r(self):
        self.assertEqual(a.search(self, [-1,0,3,5,9,12], 9), 4)

    def test_l(self):
        self.assertEqual(a.search(self, [-1,0,3,5,9,12], 0), 1)

    def test_end(self):
        self.assertEqual(a.search(self, [-1,0,3,5,9], 9), 4)

    def test_begin(self):
        self.assertEqual(a.search(self, [-1,0,3,5,9], -1), 0)

    def test_one_elem(self):
        self.assertEqual(a.search(self, [-1], -1), 0)

    def test_two_elem(self):
        self.assertEqual(a.search(self, [-1,1], 1), 1)

    def test_two_elem_2(self):
        self.assertEqual(a.search(self, [-1,1], -1), 0)

    def test_two_elem_2(self):
        self.assertEqual(a.search(self, [-1,0,3,5,9,12], 2), -1)

if __name__ == '__main__':
    unittest.main()
