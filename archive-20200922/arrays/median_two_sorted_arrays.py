# https://leetcode.com/problems/median-of-two-sorted-arrays/

# Median of Two Sorted Arrays

# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# You may assume nums1 and nums2 cannot be both empty.

# Example 1:

# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0
# Example 2:

# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5

# Brute force
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)

        if len(nums) % 2 == 1:
            return nums[len(nums)//2]
        else:
            return (nums[len(nums)//2] + nums[len(nums)//2-1])/2

# O(log(min(m,n)))
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)

        left_size = (m + n + 1) // 2
        start = 0
        end = m
        is_even = ((m + n) % 2) == 0
        while start <= end:
            a_part = (start + end) // 2
            b_part = left_size - a_part

            aleftmax = float("-inf") if a_part == 0 else nums1[a_part - 1]
            arightmin = float("inf") if a_part == m else nums1[a_part]
            bleftmax = float("-inf") if b_part == 0 else nums2[b_part - 1]
            brightmin = float("inf") if b_part == n else nums2[b_part]

            if aleftmax <= brightmin and bleftmax <= arightmin:
                if not is_even:
                    return max(aleftmax, bleftmax)
                else:
                    return (max(aleftmax, bleftmax) + min(arightmin, brightmin))/ 2
            elif aleftmax > brightmin:
                end = a_part - 1
            elif bleftmax > arightmin:
                start = a_part + 1

# O(log(min(m,n))) with code explaination
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        # positioning "nums1" to be smaller than "nums2"
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)

        # the + 1 plays well for both even and odd number of elements
        # in the combined array
        left_size = (m + n + 1) // 2
        start = 0
        end = m

        is_even = ((m + n) % 2) == 0

        while start <= end:
            a_part = (start + end) // 2
            b_part = left_size - a_part

            aleftmax = float("-inf") if a_part == 0 else nums1[a_part - 1]
            arightmin = float("inf") if a_part == m else nums1[a_part]
            bleftmax = float("-inf") if b_part == 0 else nums2[b_part - 1]
            brightmin = float("inf") if b_part == n else nums2[b_part]

            if aleftmax <= brightmin and bleftmax <= arightmin:
                if not is_even:
                    return max(aleftmax, bleftmax)
                else:
                    return (max(aleftmax, bleftmax) + min(arightmin, brightmin))/ 2
            elif aleftmax > brightmin:
                end = a_part - 1
            elif bleftmax > arightmin:
                start = a_part + 1