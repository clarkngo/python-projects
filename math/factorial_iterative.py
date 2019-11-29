class Solution:
  def factorial(self, n):
    if n == 1:
      return 1
    else:
      return n * self.factorial(n-1)

  def facIterative(self, n):
    sum = 1
    stack = []
    stack.append(n)
    while sum == 1:
      n = stack[-1]       # get the last element
      if stack[-1] == 1:  # base case: check if last element is 1
        for num in stack:
          sum *= num      #
      else:
        stack.append(n-1)
      print(stack)
    return sum

s = Solution()
a = s.factorial(5)
b = s.facIterative(5)
print(a)
print(b)
