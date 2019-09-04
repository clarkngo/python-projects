# Maximize Distance to Closest Person
# Source: https://leetcode.com/problems/maximize-distance-to-closest-person/

# In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty.
# There is at least one empty seat, and at least one person sitting.
# Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.
# Return that maximum distance to closest person.

# Example 1:
# Input: [1,0,0,0,1,0,1]
# Output: 2

# Explanation:
# If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
# If Alex sits in any other open seat, the closest person has distance 1.
# Thus, the maximum distance to the closest person is 2.

# Runtime: 168 ms, faster than 33.53% of Python3 online submissions for Maximize Distance to Closest Person.
# Memory Usage: 15.3 MB, less than 8.33% of Python3 online submissions for Maximize Distance to Closest Person.

import unittest # unit test framework
from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        sub_list: list = []
        previous: int = 0
        max_dist: int = 0

        # divide the list to sub sections
        for i in range(len(seats)):
            if seats[i] == 1:
                sub_list.append(seats[previous:i+1])
                previous = i
        sub_list.append(seats[previous:i+1])

        # edge seats from the left
        if sub_list[0][0] == 0 and sub_list[0][-1] == 1:
            if len(sub_list[0]) > max_dist:
                max_dist = len(sub_list[0]) - 1 # don't include the seated
            sub_list.pop(0)

        # edge seats from the right
        if sub_list[-1][0] == 1 and sub_list[-1][-1] == 0:
            if len(sub_list[-1]) > max_dist:
                max_dist = len(sub_list[-1]) - 1 # don't include the seated
            sub_list.pop(-1)

        if len(sub_list) > 1:
            # remove 1 seated edge left
            if sub_list[0][0] == 1 and len(sub_list[0]) == 1:
                sub_list.pop(0)

            # remove 1 seated edge right
            if sub_list[-1][0] == 1 and len(sub_list[-1]) == 1:
                sub_list.pop(-1)

        # iterate over seats in-between
        for j in range(len(sub_list)):
            # even length
            if len(sub_list[j]) % 2 == 0:
                if len(sub_list[j]) // 2 - 1 > max_dist:
                    max_dist = len(sub_list[j]) // 2 - 1
            # odd length
            else:
                if len(sub_list[j]) // 2 > max_dist:
                    max_dist = len(sub_list[j]) // 2

        return max_dist

a = Solution
class Test(unittest.TestCase):

    def test_seat_in_the_middle(self):
        self.assertEqual(a.maxDistToClosest(self, [1,0,0,1]), 1)

    def test_seat_in_the_middle1(self):
        self.assertEqual(a.maxDistToClosest(self, [1,0,0,0,1]), 2)

    def test_seat_in_the_middle2(self):
        self.assertEqual(a.maxDistToClosest(self, [1,0,0,0,1,0,1]), 2)

    def test_seat_in_the_middle3(self):
        self.assertEqual(a.maxDistToClosest(self, [1,0,1,0,0,0,1]), 2)

    def test_seat_in_the_middle4(self):
        self.assertEqual(a.maxDistToClosest(self, [1,0,1,0,0,0,1,0]), 2)

    def test_seat_in_the_middle5(self):
        self.assertEqual(a.maxDistToClosest(self, [0,1,0,0,0,1,0,1]), 2)

    def test_seat_at_the_front1(self):
        self.assertEqual(a.maxDistToClosest(self, [0,0,0,1]), 3)

    def test_seat_at_the_end1(self):
        self.assertEqual(a.maxDistToClosest(self, [1,0,1,0,0,0,0]), 4)

    def test_seat_at_the_end2(self):
        self.assertEqual(a.maxDistToClosest(self, [1,0,0,0]), 3)

    def test_seat_at_the_end3(self):
        self.assertEqual(a.maxDistToClosest(self, [0,1,0,0,0,0]), 4)

if __name__ == '__main__':
    unittest.main()
