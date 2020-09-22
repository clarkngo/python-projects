# Source: https://leetcode.com/problems/unique-number-of-occurrences/

# Unique Number of Occurrences

# Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.



# Example 1:

# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
# Example 2:

# Input: arr = [1,2]
# Output: false
# Example 3:

# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true


# Constraints:

# 1 <= arr.length <= 1000
# -1000 <= arr[i] <= 1000

from typing import *

class Solution(object):
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        my_dict = {}
        frequency = []
        for x in arr:
            if str(x) not in my_dict:
                my_dict[str(x)] = 1
            else:
                my_dict[str(x)] += 1

        flag: bool
        # len() + set()
        # converts the list to set and then tests with original list if contains similar no. of elements.
        # Source: https://www.geeksforgeeks.org/python-check-if-list-contains-all-unique-elements/
        flag = len(set(my_dict.values())) == len(my_dict.values())

        return flag

a = Solution()

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(a.uniqueOccurrences([1,2,2,1,1,3]), True)

    def test2(self):
        self.assertEqual(a.uniqueOccurrences([1,2]), False)

    def test3(self):
        self.assertEqual(a.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]), True)

if __name__ == '__main__':
    unittest.main()
