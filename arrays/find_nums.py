# Source: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

# Find All Numbers Disappeared in an Array

# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

# Find all the elements of [1, n] inclusive that do not appear in this array.

# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

# Example:

# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [5,6]

import unittest # unit test framework
from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        missing_num: list = []
        no_dupl: list = Solution.remove_duplicate(nums)
        no_dupl.sort()
        print(no_dupl)

    def remove_duplicate(duplicate):
        final_list = []
        for num in duplicate:
            if num not in final_list:
                final_list.append(num)
        return final_list

a = Solution
class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(a.findDisappearedNumbers(self, [4,3,2,7,8,2,3,1]), [5,6])



if __name__ == '__main__':
    unittest.main()
