"""
https://leetcode.com/problems/intersection-of-two-arrays-ii/

Intersection of Two Arrays II

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?


Runtime: 72 ms, faster than 12.85% of Python3 online submissions for Intersection of Two Arrays II.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Intersection of Two Arrays II.
"""
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        if nums1 and nums2:
            for i in range(len(nums1)):
                if nums1[i] in nums2:
                    res.append(nums1[i])
                    nums2.remove(nums1[i])
        return res

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        num1Dict = {}

        for n in nums1:
            num1Dict[n] = num1Dict[n] + 1 if n in num1Dict else 1

        for n in nums2:
            if n in num1Dict and num1Dict[n] > 0:
                intersection.append(n)
                num1Dict[n] = num1Dict[n] - 1

        return intersection
