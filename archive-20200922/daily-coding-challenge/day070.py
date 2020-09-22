# This is your coding interview problem for today.

# This problem was asked by Microsoft.

# A number is considered perfect if its digits sum up to exactly 10.

# Given a positive integer n, return the n-th perfect number.

# For example, given 1, you should return 19. Given 2, you should return 28.

# helper method to add digits
def sum_of_digits(n):
    sum = 0
    while n > 0:
      sum += n % 10   # add each digit to sum
      n //= 10        # reduce the digit
    return sum

# n-th perfect number. Perfect num is digits summing up to 10

def perfect(target_n):
    num, n = 0, 0
    while n < target_n:
      num += 1
      if sum_of_digits(num) == 10:
        n += 1
    return num

# Solution
# There's no faster way than simply iterating over all the numbers and
# keeping track of the current perfect number until we hit n.
# So that's what we'll do:

# def sum_of_digits(n):
#     current_sum = 0
#     while n > 0:
#         current_sum += n % 10
#         n = n // 10
#     return current_sum

# def perfect(n):
#     i, current = 0, 0
#     while current < n:
#         i += 1
#         if sum_of_digits(i) == 10:
#             current += 1
#     return i
# This will run in O(N) time.
