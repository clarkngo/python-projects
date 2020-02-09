# Rank Transform of an Array

# Given an array of integers arr, replace each element with its rank.

# The rank represents how large the element is. The rank has the following rules:

# Rank is an integer starting from 1.
# The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
# Rank should be as small as possible.

# Example 1:

# Input: arr = [40,10,20,30]
# Output: [4,1,2,3]
# Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.
# Example 2:

# Input: arr = [100,100,100]
# Output: [1,1,1]
# Explanation: Same elements share the same rank.
# Example 3:

# Input: arr = [37,12,28,9,100,56,80,5,12]
# Output: [5,3,4,2,8,6,7,1,3]


# Constraints:

# 0 <= arr.length <= 105
# -109 <= arr[i] <= 109

class Solution:

    # Submission Result: Time Limit Exceeded
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        my_dict = {}
        ranked_lst = arr
        prev = None
        for i in range(len(arr)):
            my_dict[i] = arr[i]

        rank_plus = 1
        for i in range(len(arr)):
            cur = min(my_dict, key=my_dict.get)
            if prev == my_dict[cur]:
                rank_plus -= 1
            ranked_lst[cur] = i + rank_plus
            prev = my_dict[cur]
            del my_dict[cur]

        return ranked_lst
