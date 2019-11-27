# Source: https://leetcode.com/problems/3sum/
# 3Sum
# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.

# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums == [] or len(nums) < 3:
            return []
        if all(i >= 0 for i in nums) or all(i < 0 for i in nums):
            if all(i == 0 for i in nums):
                return [[0,0,0]]
            else:
                return []
        nums.sort()
        positives = []
        negatives = []
        zeroes = []
        triplets = []
        for i in range(len(nums)):
            if nums[i] > 0:
                positives.append(nums[i])
            elif nums[i] < 0:
                negatives.append(nums[i])
            else:
                zeroes.append(nums[i])

        # two positives 1 negative
        if len(positives) >= 2:
            for i in range(len(negatives)):
                for j in range(len(positives)):
                    for k in range(j+1, len(positives)):
                        if positives[j] + positives[k] == abs(negatives[i]):
                            triplets.append(negatives[i])
                            triplets.append(positives[j])
                            triplets.append(positives[k])

        # two negatives 1 positive
        if len(negatives) >= 2:
            for i in range(len(positives)):
                for j in range(len(negatives)):
                    for k in range(j+1, len(negatives)):
                        if abs(negatives[j]) + abs(negatives[k]) == positives[i]:
                            triplets.append(positives[i])
                            triplets.append(negatives[j])
                            triplets.append(negatives[k])

        # 1 zero, 1 positive, 1 negative
        if len(zeroes) >= 1:
            for i in range(len(positives)):
                for j in range(len(negatives)):
                    if positives[i] + negatives[j] == 0:
                        triplets.append(positives[i])
                        triplets.append(negatives[j])
                        triplets.append(zeroes[0])

        unique_triplets = []
        for i in range(0, len(triplets),3):
            if triplets[i:i+3] not in unique_triplets:
                unique_triplets.append(triplets[i:i+3])
        for trplt in unique_triplets:
            trplt = trplt.sort()
        zero_set = []
        for num in nums:
            if num == 0:
                zero_set.append(0)
        if len(zero_set) >= 3:
            unique_triplets.insert(len(unique_triplets),[0,0,0])
        unique_triplets.sort()
        return unique_triplets

a = Solution
import unittest
class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(a.threeSum(self, [-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])
    def test2(self):
        self.assertEqual(a.threeSum(self, [0,0,0]), [[0,0,0]])
    def test3(self):
        self.assertEqual(a.threeSum(self, [-2,0,1,1,2]), [[-2,0,2],[-2,1,1]])
    def test4(self):
        self.assertEqual(a.threeSum(self, [0]), [])
    def test5(self):
        self.assertEqual(a.threeSum(self, []), [])
    def test6(self):
        self.assertEqual(a.threeSum(self, [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]), [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]])
    def test7(self):
        self.assertEqual(a.threeSum(self, [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]), [[-5,1,4],[-4,0,4],[-4,1,3],[-2,-2,4],[-2,1,1],[0,0,0]])
    def test8(self):
        self.assertEqual(a.threeSum(self, [4,4,3,-5,0,0,0,-2,3,-5,-5,0]), [[0,0,0]])

    # Time Limit Exceeded
    def test9(self):
        self.assertEqual(a.threeSum(self,[82597,-9243,62390,83030,-97960,-26521,-61011,83390,-38677,12333,75987,46091,83794,19355,-71037,-6242,-28801,324,1202,-90885,-2989,-95597,-34333,35528,5680,89093,-90606,50360,-29393,-27012,53313,65213,99818,-82405,-41661,-3333,-51952,72135,-1523,26377,74685,96992,92263,15929,5467,-99555,-43348,-41689,-60383,-3990,32165,65265,-72973,-58372,12741,-48568,-46596,72419,-1859,34153,62937,81310,-61823,-96770,-54944,8845,-91184,24208,-29078,31495,65258,14198,85395,70506,-40908,56740,-12228,-40072,32429,93001,68445,-73927,25731,-91859,-24150,10093,-60271,-81683,-18126,51055,48189,-6468,25057,81194,-58628,74042,66158,-14452,-49851,-43667,11092,39189,-17025,-79173,13606,83172,92647,-59741,19343,-26644,-57607,82908,-20655,1637,80060,98994,39331,-31274,-61523,91225,-72953,13211,-75116,-98421,-41571,-69074,99587,39345,42151,-2460,98236,15690,-52507,-95803,-48935,-46492,-45606,-79254,-99851,52533,73486,39948,-7240,71815,-585,-96252,90990,-93815,93340,-71848,58733,-14859,-83082,-75794,-82082,-24871,-1
        ]), [[]])


if __name__ == '__main__':
    unittest.main()


# This is the answer from @caikehe and all the comments below

# The main idea is to iterate every number in nums.
# We use the number as a target to find two other numbers which make total zero.
# For those two other numbers, we move pointers, l and r, to try them.

# l start from left to right.
# r start from right to left.

# First, we sort the array, so we can easily move i around and know how to adjust l and r.
# If the number is the same as the number before, we have used it as target already, continue. [1]
# We always start the left pointer from i+1 because the combination of 0~i has already been tried. [2]

# Now we calculate the total:
# If the total is less than zero, we need it to be larger, so we move the left pointer. [3]
# If the total is greater than zero, we need it to be smaller, so we move the right pointer. [4]
# If the total is zero, bingo! [5]
# We need to move the left and right pointers to the next different numbers, so we do not get repeating result. [6]

# We do not need to consider i after nums[i]>0, since sum of 3 positive will be always greater than zero. [7]
# We do not need to try the last two, since there are no rooms for l and r pointers.
# You can think of it as The last two have been tried by all others. [8]

# For time complexity
# Sorting takes O(NlogN)
# Now, we need to think as if the nums is really really big
# We iterate through the nums once, and each time we iterate the whole array again by a while loop
# So it is O(NlogN+N^2)~=O(N^2)

# For space complexity
# We didn't use extra space except the res
# So it is O(1).

# Code
class Solution(object):
	def threeSum(self, nums):
		res = []
		nums.sort()
		length = len(nums)
		for i in xrange(length-2): #[8]
			if nums[i]>0: break #[7]
			if i>0 and nums[i]==nums[i-1]: continue #[1]

			l, r = i+1, length-1 #[2]
			while l<r:
				total = nums[i]+nums[l]+nums[r]

				if total<0: #[3]
					l+=1
				elif total>0: #[4]
					r-=1
				else: #[5]
					res.append([nums[i], nums[l], nums[r]])
					while l<r and nums[l]==nums[l+1]: #[6]
						l+=1
					while l<r and nums[r]==nums[r-1]: #[6]
						r-=1
					l+=1
					r-=1
		return res
# More Resource
# I really take time tried to make the best solution or explaination.
# Because I wanted to help others like me.
# If you like my answer, a star on GitHub means a lot to me.
# https://github.com/wuduhren/leetcode-python