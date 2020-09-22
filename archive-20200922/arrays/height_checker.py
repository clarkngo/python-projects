# Souce: https://leetcode.com/problems/height-checker/
# Students are asked to stand in non-decreasing order of heights for an annual photo.
# Return the minimum number of students not standing in the right positions.
# (This is the number of students that must move in order for all students to be
# standing in non-decreasing order of height.)

# Example 1:

# Input: [1,1,4,2,1,3]
# Output: 3
# Explanation:
# Students with heights 4, 3 and the last 1 are not standing in the right positions.

# Runtime: 40 ms, faster than 84.64% of Python3 online submissions for Height Checker.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Height Checker.


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        orignal_heights = []
        orignal_heights.extend(heights)     # copy a list
        heights.sort()
        count = 0
        for i in range(len(heights)):
                if orignal_heights[i] != heights[i]:
                    count += 1
        return count