# Source: https://leetcode.com/problems/maximum-subarray/

# Maximum Subarray
# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:

# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

# Time Limit Exceed O(n^2)
# class Solution(object):
#     def maxSubArray(self, nums) -> int:
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         sum = nums[0]           # for negative num
#         max = nums[0]           # for negative num
#         for i in range(len(nums)):
#             for j in range(i, len(nums)):
#                 if i == 0 and j == 0:       # fence post
#                     continue
#                 sum += nums[j]
#                 if sum > max:
#                     max = sum
#             sum = 0
#         return max
class Solution(object):
    def maxSubArray(self, A) -> int:
        max_ending_here = max_so_far = A[0]
        for x in A[1:]:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

import unittest
a = Solution()

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]),6)

    def test2(self):
        self.assertEqual(a.maxSubArray([-1]),-1)

    def test3(self):
        self.assertEqual(a.maxSubArray([-1, -2]),-1)

    def test4(self):
        self.assertEqual(a.maxSubArray([1]),1)

if __name__ == '__main__':
    unittest.main()
