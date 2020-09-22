class Solution:
    def isPalindrome(self, x: int) -> bool:

        # if negative number
        if x < 0:
            return False

        # length of integer
        num = x
        while num > 0:
            num = num // 10
            length = length + 1
        mid = length // 2
        for i in range(mid):
            True

s = Solution.isPalindrome

