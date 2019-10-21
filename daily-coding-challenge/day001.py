# Good morning.

# This is your coding interview problem for today.

# This problem was recently asked by Google.

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?

from typing import List

class Solution:
    # nested for loop
    # O(n^2)
    def hasTwoSums_1(self, arr: List, target: int) -> bool:
        if len(arr) <= 1:
            return False
        for i in range(len(arr)):
            for j in range(len(arr) - i):
                if arr[i] + arr[j] == target:
                    return True
        return False

    # hash table
    # O(n)
    def hasTwoSums_2(self, arr: List, target: int) -> bool:
        if len(arr) <= 1:
            return False
        my_dict = {}
        my_dict["0"] = arr[0]
        for i in range(1, len(arr)):
            if target - arr[i] in my_dict.values():
                return True
        return False

import unittest
a = Solution()

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(a.hasTwoSums_1([10, 15, 3, 7], 13), True)
        self.assertEqual(a.hasTwoSums_1([2, 7, 11, 15], 9), True)
        self.assertEqual(a.hasTwoSums_1([2, 11, 15], 9), False)
        self.assertEqual(a.hasTwoSums_1([2], 9), False)
        self.assertEqual(a.hasTwoSums_1([], 9), False)

    def test2(self):
        self.assertEqual(a.hasTwoSums_2([10, 15, 3, 7], 13), True)
        self.assertEqual(a.hasTwoSums_2([2, 7, 11, 15], 9), True)
        self.assertEqual(a.hasTwoSums_2([2], 9), False)
        self.assertEqual(a.hasTwoSums_2([], 9), False)

if __name__ == '__main__':
    unittest.main()


# Answer Key

# This problem can be solved in several different ways.

# Brute force way would involve a nested iteration to check for every pair of numbers:

def two_sum(lst, k):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j and lst[i] + lst[j] == k:
                return True
    return False

# This would take O(N2). Another way is to use a set to remember the numbers we've seen so far.
# Then for a given number, we can check if there is another number that, if added, would sum to k.
# This would be O(N) since lookups of sets are O(1) each.

def two_sum(lst, k):
    seen = set()
    for num in lst:
        if k - num in seen:
            return True
        seen.add(num)
    return False

# Yet another solution involves sorting the list.
# We can then iterate through the list and run a binary search on K - lst[i].
# Since we run binary search on N elements, this would take O(N log N) with O(1) space.

from bisect import bisect_left


def two_sum(lst, K):
    lst.sort()

    for i in range(len(lst)):
        target = K - lst[i]
        j = binary_search(lst, target)

        # Check that binary search found the target and that it's not in the same index
        # as i. If it is in the same index, we can check lst[i + 1] and lst[i - 1] to see
        #  if there's another number that's the same value as lst[i].
        if j == -1:
            continue
        elif j != i:
            return True
        elif j + 1 < len(lst) and lst[j + 1] == target:
            return True
        elif j - 1 >= 0 and lst[j - 1] == target:
            return True
    return False

def binary_search(lst, target):
    lo = 0
    hi = len(lst)
    ind = bisect_left(lst, target, lo, hi)

    if 0 <= ind < hi and lst[ind] == target:
        return ind
    return -1