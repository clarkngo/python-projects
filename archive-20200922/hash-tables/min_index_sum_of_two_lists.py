# Source: https://leetcode.com/problems/minimum-index-sum-of-two-lists/
# Minimum Index Sum of Two Lists

# Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

# You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

# Example 1:
# Input:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
# Output: ["Shogun"]
# Explanation: The only restaurant they both like is "Shogun".
# Example 2:
# Input:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["KFC", "Shogun", "Burger King"]
# Output: ["Shogun"]
# Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
# Note:
# The length of both lists will be in the range of [1, 1000].
# The length of strings in both lists will be in the range of [1, 30].
# The index is starting from 0 to the list length minus 1.
# No duplicates in both lists.

# Runtime: 168 ms, faster than 72.06% of Python3 online submissions for Minimum Index Sum of Two Lists.
# Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Minimum Index Sum of Two Lists.

from typing import List
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        if list1 == [] or list2 == []: return []
        common_list = []
        my_dict, filter_dict = {}, {}
        min_sum = len(list1) + len(list2) + 1

        # iterate over the two lists
        for i in range(len(list1)):
            my_dict[list1[i]] = [i]   # store index in list[0] in dict
        for j in range(len(list2)):
            if  list2[j] in my_dict:
                my_dict[list2[j]] += [j]  # store index in list[1] in dict

        # place into new dictionary for common items
        for k, v in my_dict.items():
           if len(v) == 2:
              filter_dict[k] = v[0] + v[1]    # sum the indicies
        min_val = min(filter_dict.values())   # look for minimum sum
        # add to list if value is equal to minmum
        [common_list.append(k) for k, v in filter_dict.items() if v == min_val]
        return common_list


import unittest
a = Solution()
class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
          a.findRestaurant(
            ["Shogun","Tapioca Express","Burger King","KFC"],
            ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]),
            ["Shogun"])

    def test2(self):
        self.assertEqual(
          a.findRestaurant(
            ["Shogun","Tapioca Express","Burger King","KFC"],
            ["KFC","Burger King","Tapioca Express","Shogun"]),
            ["KFC","Burger King","Tapioca Express","Shogun"])

if __name__ == '__main__':
    unittest.main()
