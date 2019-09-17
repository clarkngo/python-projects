# Source: https://leetcode.com/problems/last-stone-weight/

# Last Stone Weight

# We have a collection of rocks, each rock has a positive integer weight.

# Each turn, we choose the two heaviest rocks and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

# If x == y, both stones are totally destroyed;
# If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
# At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)



# Example 1:

# Input: [2,7,4,1,8,1]
# Output: 1
# Explanation:
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.


# Note:

# 1 <= stones.length <= 30
# 1 <= stones[i] <= 1000

# Runtime: 16 ms, faster than 84.50% of Python online submissions for Last Stone Weight.
# Memory Usage: 11.8 MB, less than 100.00% of Python online submissions for Last Stone Weight.

import unittest # unit test framework
from typing import List

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        new_stone = 0
        stones.sort(reverse = True)
        print(stones)
        while len(stones) > 1:
            if stones[0] > stones[1]:
                new_stone = stones[0] - stones[1]
            elif stones[0] < stones[1]:
                new_stone = stones[1] - stones[0]

            stones.pop(0)
            stones.pop(0)
            if new_stone > 0:
                stones.insert(0,new_stone)
            stones.sort(reverse = True)
            new_stone = 0
        if stones == []:
            return 0
        return stones[0]




a = Solution
class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(a.lastStoneWeight(self,[2,7,4,1,8,1]), 1)

    def test2(self):
        self.assertEqual(a.lastStoneWeight(self,[3,1]), 2)

    def test3(self):
        self.assertEqual(a.lastStoneWeight(self,[2,2]), 2)
if __name__ == '__main__':
    unittest.main()

