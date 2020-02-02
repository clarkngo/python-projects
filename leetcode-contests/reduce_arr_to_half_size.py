# Reduce Array Size to The Half
# User Accepted:1628
# User Tried:1881
# Total Accepted:1642
# Total Submissions:2218
# Difficulty:Medium
# Given an array arr.  You can choose a set of integers and remove all the occurrences of these integers in the array.

# Return the minimum size of the set so that at least half of the integers of the array are removed.



# Example 1:

# Input: arr = [3,3,3,3,5,5,5,2,2,7]
# Output: 2
# Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
# Possible sets of size 2 are {3,5},{3,2},{5,2}.
# Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has size greater than half of the size of the old array.
# Example 2:

# Input: arr = [7,7,7,7,7,7]
# Output: 1
# Explanation: The only possible set you can choose is {7}. This will make the new array empty.
# Example 3:

# Input: arr = [1,9]
# Output: 1
# Example 4:

# Input: arr = [1000,1000,3,7]
# Output: 1
# Example 5:

# Input: arr = [1,2,3,4,5,6,7,8,9,10]
# Output: 5


# Constraints:

# 1 <= arr.length <= 10^5
# arr.length is even.
# 1 <= arr[i] <= 10^5

# Time Limit Exceeded
# import operator
# class Solution:
#     def minSetSize(self, arr: List[int]) -> int:
#         d = {}
#         half = len(arr) // 2
#         count = 0
#         n_removed = 0
#         for i in range(len(arr)):
#             if arr[i] not in d:
#                 d[arr[i]] = 1
#             else:
#                 d[arr[i]] += 1

#         while count < half:
#             m_key = max(d.items(), key=operator.itemgetter(1))[0]
#             count += d[m_key]
#             d[m_key] = 0
#             n_removed += 1
#         return n_removed

from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        s_freq = [item for items, c in Counter(arr).most_common()
                                      for item in [items] * c]
        d = {}
        half = len(s_freq) // 2
        n_ints = 0
        uniq_ints = 0
        for i in range(len(s_freq)):
            if s_freq[i] not in d:
                d[s_freq[i]] = 1
                n_ints += 1
                uniq_ints += 1
            else:
                d[s_freq[i]] += 1
                n_ints += 1
            if n_ints >= half:
                break
        return uniq_ints
