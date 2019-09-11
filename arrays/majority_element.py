# Source: https://leetcode.com/problems/majority-element/

# Majority Element

# Given an array of size n, find the majority element.
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and the majority element
# always exist in the array.

# Example 1:

# Input: [3,2,3]
# Output: 3
# Example 2:

# Input: [2,2,1,1,1,2,2]
# Output: 2

# Runtime: 228 ms, faster than 7.06% of Python3 online submissions for Majority Element.
# Memory Usage: 15.2 MB, less than 7.14% of Python3 online submissions for Majority Element.

import unittest # unit test framework
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        d = {}
        for num in nums:
            if str(num) not in d:
                d[str(num)] = 1
            else:
                d[str(num)] += 1
        return int(max(d, key=d.get))


a = Solution
class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(a.majorityElement(self, [3,2,3]), 3)

    def test2(self):
        self.assertEqual(a.majorityElement(self, [2,2,1,1,1,2,2]), 2)

if __name__ == '__main__':
    unittest.main()
