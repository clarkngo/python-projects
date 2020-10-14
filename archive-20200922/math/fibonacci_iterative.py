class Solution():
  def fib(self, n):
    if n == 0:
      return 0
    if n == 1:
      return 1
    return self.fib(n-1) + self.fib(n-2)

  def fibIterative(self, n):
    stack = []
    stack.append(n)
    sum = 0
    while(len(stack) > 0):
      n = stack.pop()
      if n == 0:
        sum += 0
      elif n == 1:
        sum += 1
      else:
        stack.append(n-1)
        stack.append(n-2)
      # print(stack)
    return sum

s = Solution()
# ans = s.fib(10)
# print(ans)
ans = s.fibIterative(10)
print(ans)

## Input of 10
## Stack inside the while loop
# [9, 8]
# [9, 7, 6]
# [9, 7, 5, 4]
# [9, 7, 5, 3, 2]
# [9, 7, 5, 3, 1, 0]
# [9, 7, 5, 3, 1]
# [9, 7, 5, 3]
# [9, 7, 5, 2, 1]
# [9, 7, 5, 2]
# [9, 7, 5, 1, 0]
# [9, 7, 5, 1]
# [9, 7, 5]
# [9, 7, 4, 3]
# [9, 7, 4, 2, 1]
# [9, 7, 4, 2]
# [9, 7, 4, 1, 0]
# [9, 7, 4, 1]
# [9, 7, 4]
# [9, 7, 3, 2]
# [9, 7, 3, 1, 0]
# [9, 7, 3, 1]
# [9, 7, 3]
# [9, 7, 2, 1]
# [9, 7, 2]
# [9, 7, 1, 0]
# [9, 7, 1]
# [9, 7]
# [9, 6, 5]
# [9, 6, 4, 3]
# [9, 6, 4, 2, 1]
# [9, 6, 4, 2]
# [9, 6, 4, 1, 0]
# [9, 6, 4, 1]
# [9, 6, 4]
# [9, 6, 3, 2]
# [9, 6, 3, 1, 0]
# [9, 6, 3, 1]
# [9, 6, 3]
# [9, 6, 2, 1]
# [9, 6, 2]
# [9, 6, 1, 0]
# [9, 6, 1]
# [9, 6]
# [9, 5, 4]
# [9, 5, 3, 2]
# [9, 5, 3, 1, 0]
# [9, 5, 3, 1]
# [9, 5, 3]
# [9, 5, 2, 1]
# [9, 5, 2]
# [9, 5, 1, 0]
# [9, 5, 1]
# [9, 5]
# [9, 4, 3]
# [9, 4, 2, 1]
# [9, 4, 2]
# [9, 4, 1, 0]
# [9, 4, 1]
# [9, 4]
# [9, 3, 2]
# [9, 3, 1, 0]
# [9, 3, 1]
# [9, 3]
# [9, 2, 1]
# [9, 2]
# [9, 1, 0]
# [9, 1]
# [9]
# [8, 7]
# [8, 6, 5]
# [8, 6, 4, 3]
# [8, 6, 4, 2, 1]
# [8, 6, 4, 2]
# [8, 6, 4, 1, 0]
# [8, 6, 4, 1]
# [8, 6, 4]
# [8, 6, 3, 2]
# [8, 6, 3, 1, 0]
# [8, 6, 3, 1]
# [8, 6, 3]
# [8, 6, 2, 1]
# [8, 6, 2]
# [8, 6, 1, 0]
# [8, 6, 1]
# [8, 6]
# [8, 5, 4]
# [8, 5, 3, 2]
# [8, 5, 3, 1, 0]
# [8, 5, 3, 1]
# [8, 5, 3]
# [8, 5, 2, 1]
# [8, 5, 2]
# [8, 5, 1, 0]
# [8, 5, 1]
# [8, 5]
# [8, 4, 3]
# [8, 4, 2, 1]
# [8, 4, 2]
# [8, 4, 1, 0]
# [8, 4, 1]
# [8, 4]
# [8, 3, 2]
# [8, 3, 1, 0]
# [8, 3, 1]
# [8, 3]
# [8, 2, 1]
# [8, 2]
# [8, 1, 0]
# [8, 1]
# [8]
# [7, 6]
# [7, 5, 4]
# [7, 5, 3, 2]
# [7, 5, 3, 1, 0]
# [7, 5, 3, 1]
# [7, 5, 3]
# [7, 5, 2, 1]
# [7, 5, 2]
# [7, 5, 1, 0]
# [7, 5, 1]
# [7, 5]
# [7, 4, 3]
# [7, 4, 2, 1]
# [7, 4, 2]
# [7, 4, 1, 0]
# [7, 4, 1]
# [7, 4]
# [7, 3, 2]
# [7, 3, 1, 0]
# [7, 3, 1]
# [7, 3]
# [7, 2, 1]
# [7, 2]
# [7, 1, 0]
# [7, 1]
# [7]
# [6, 5]
# [6, 4, 3]
# [6, 4, 2, 1]
# [6, 4, 2]
# [6, 4, 1, 0]
# [6, 4, 1]
# [6, 4]
# [6, 3, 2]
# [6, 3, 1, 0]
# [6, 3, 1]
# [6, 3]
# [6, 2, 1]
# [6, 2]
# [6, 1, 0]
# [6, 1]
# [6]
# [5, 4]
# [5, 3, 2]
# [5, 3, 1, 0]
# [5, 3, 1]
# [5, 3]
# [5, 2, 1]
# [5, 2]
# [5, 1, 0]
# [5, 1]
# [5]
# [4, 3]
# [4, 2, 1]
# [4, 2]
# [4, 1, 0]
# [4, 1]
# [4]
# [3, 2]
# [3, 1, 0]
# [3, 1]
# [3]
# [2, 1]
# [2]
# [1, 0]
# [1]
# []
# 55