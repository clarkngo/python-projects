# https://www.codewars.com/kata/56b1eb19247c01493a000065/train/python

# Unique Sum

# Given a list of integers values, your job is to return the sum of the values; however, if the same integer value appears multiple times in the list, you can only count it once in your sum.

# For example:

# [ 1, 2, 3] ==> 6

# [ 1, 3, 8, 1, 8] ==> 12

# [ -1, -1, 5, 2, -7] ==> -1

# [] ==> None

# test.assert_equals( unique_sum([1,2,3]), 6)
# test.assert_equals( unique_sum([1,3,8,1,8]), 12)
# test.assert_equals( unique_sum([-1,-1,5,2,-7]),-1)

def unique_sum(lst):
    if lst == []: return None
    my_dict = {}
    total = 0
    for val in lst:
        if str(val) not in my_dict:
            my_dict[str(val)] = None
            total += val
    return total

# using set
def unique_sum(lst):
    return sum(set(lst)) if lst else None

def unique_sum(lst):
    if lst:
       return sum(set(lst))

# using lambda
unique_sum = lambda l: sum(set(l)) if l else None
