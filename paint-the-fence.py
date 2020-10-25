class Solution:
    def numWays(self, pickets: int, colors: int) -> int:
        """
        There is a fence with n posts, each post can be painted with one of the k colors.

        You have to paint all the posts such that no more than two adjacent fence posts have the same color.

        Return the total number of ways you can paint the fence.

        Note:
        n and k are non-negative integers.
        """
        # edge case
        # 0 picket means no colors can be painted
        if pickets == 0:
            return 0
        # 1 picket means num of ways == colors
        if pickets == 1:
            return colors
        
        # total num of ways = same num of ways + diff num of ways
        same = colors 
        diff = colors * (colors - 1)
        
        if pickets == 2:
            return same + diff
        
        prev_same, prev_diff = same, diff
        for _ in range(3, pickets + 1):
            same = prev_diff
            diff = (prev_same + prev_diff) * (colors - 1)
            prev_same, prev_diff = same, diff
        return same + diff
            