# Reverse Subarray To Maximize Array Value
# User Accepted:63
# User Tried:495
# Total Accepted:72
# Total Submissions:1170
# Difficulty:Hard
# You are given an integer array nums. The value of this array is defined as the sum of |nums[i]-nums[i+1]| for all 0 <= i < nums.length-1.

# You are allowed to select any subarray of the given array and reverse it. You can perform this operation only once.

# Find maximum possible value of the final array.

# Example 1:

# Input: nums = [2,3,1,5,4]
# Output: 10
# Explanation: By reversing the subarray [3,1,5] the array becomes [2,5,1,3,4] whose value is 10.
# Example 2:

# Input: nums = [2,4,9,24,2,1,10]
# Output: 68


# Constraints:

# 1 <= nums.length <= 3*10^4
# -10^5 <= nums[i] <= 10^5

class Solution(object):

    def maxValueAfterReverse(self, A):
        n = len(A)
        total = res = sum(abs(a - b) for a, b in zip(A, A[1:]))
        max2, min2 = sorted(A[:2])
        # print total
        for a, b in zip(A, A[1:]):
            # print 'meet', a, b
            # print "min2", min2, "max2", max2
            # print total - abs(a - b) + abs(A[0] - b)
            res = max(res, total - abs(a - b) + abs(A[0] - b))
            # print total - abs(a - b) + abs(A[-1] - a)
            res = max(res, total - abs(a - b) + abs(A[-1] - a))
            # print total + (min(a, b) - min2) * 2
            res = max(res, total + (min(a, b) - min2) * 2)
            # print total + (max2 - max(a, b)) * 2
            res = max(res, total + (max2 - max(a, b)) * 2)

            min2 = min(min2, max(a, b))
            max2 = max(max2, min(a, b))
        return res
