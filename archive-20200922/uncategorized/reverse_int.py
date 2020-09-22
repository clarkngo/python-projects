# Reverse Integer
# Given a 32-bit signed integer, reverse digits of an integer.
# https://leetcode.com/problems/reverse-integer/submissions/

# Runtime: 40 ms, faster than 83.55% of Python3 online submissions for Reverse Integer.
# Memory Usage: 13.1 MB, less than 86.76% of Python3 online submissions for Reverse Integer.

def reverse(x: int) -> int:
  solution = 0
  isNegative = False
  digit = 0
  
  if (x == 0):
      return 0
  
  # change negative number to positive
  if (x < 0):
      x *= - 1
      isNegative = True
      
  # if have zeroes on the right
  while (x % 10 == 0):
      x //= 10
      
  # iterate over the integer
  while (x > 0):
      digit = x % 10
      solution = digit + solution * 10
      x //= 10

  # integer overflow
  if (solution > 2**31):
      return 0
  
  # convert back to negative if was a negative number
  if (isNegative):
      solution *= -1

  return solution

x = 123
print(reverse(x))

x = -123
print(reverse(x))

x = 210
print(reverse(x))

x = 1234567899
print(reverse(x))
