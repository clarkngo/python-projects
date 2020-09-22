# https://leetcode.com/problems/valid-perfect-square/

# Valid Perfect Square

# Given a positive integer num, write a function which returns True if num is a perfect square else False.

# Note: Do not use any built-in library function such as sqrt.

# Runtime: 28 ms, faster than 83.51% of Python3 online submissions for Valid Perfect Square.
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Valid Perfect Square.


class Solution:
    # Linear Search
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        # I can generate squared values
        # while squared values is < to num
        squared_number = 0
        base_number = 0
        while squared_number < num:
            base_number += 1
            squared_number = base_number * base_number
        if squared_number == num:
            return True
        return False

    # Binary Search
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num
        while left <= right:
            mid = left + (right-left) // 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                right = mid - 1
            else:
                left = mid + 1
        return False

    def BitwiseTrick(self, num):
       root = 0
       bit = 1 << 15

       while bit > 0 :
           root |= bit
           if root > num // root:
               root ^= bit
           bit >>= 1
       return root * root == num
