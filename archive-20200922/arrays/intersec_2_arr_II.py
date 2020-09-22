# Source: https://leetcode.com/problems/intersection-of-two-arrays-ii/

import unittest # unit test framework
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersect = []
        for i in range(nums1):
            if num1 in nums2:
                intersect.append(num1)

        return intersect

a = Solution
class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(a.intersect(self, [1,2,2,1], [2,2]), [2,2])

    def test2(self):
        self.assertEqual(a.intersect(self, [4,9,5], [9,4,9,8,4]), [4,9])


if __name__ == '__main__':
    unittest.main()
