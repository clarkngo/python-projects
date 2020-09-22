"""Solution for factorial"""
class Solution:
    """Solution"""
    @staticmethod
    def factorial(num):
        """Factorial recursive approach"""
        if num == 1:
            return 1
        return num * Solution.factorial(num-1)

    @staticmethod
    def fac_iterative(num):
        """Factorial iterative approach"""
        result = 1
        stack = []
        stack.append(num)
        while result == 1:
            num = stack[-1]       # get the last element
            if stack[-1] == 1:  # base case: check if last element is 1
                for item in stack:
                    result *= item      #
            else:
                stack.append(num-1)
            print(stack)
        return result

S = Solution()
A = S.factorial(5)
B = S.fac_iterative(5)
print(A)
print(B)
