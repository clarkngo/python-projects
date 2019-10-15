# Source: https://leetcode.com/problems/intersection-of-two-arrays-ii/

# Fizz Buzz

# Write a program that outputs the string representation of numbers
# from 1 to n. But for multiples of three it should output “Fizz”
# instead of the number and for the multiples of five output “Buzz”.
# For numbers which are multiples of both three and five output “FizzBuzz”.

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
