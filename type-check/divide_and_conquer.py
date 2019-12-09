# https://www.codewars.com/kata/57eaec5608fed543d6000021/train/python

# Divide and Conquer

# Given a mixed array of number and string representations of integers, add up the string integers and subtract this from the total of the non-string integers.

# test.describe("Example Tests")
# test.assert_equals(div_con([9, 3, '7', '3']), 2)
# test.assert_equals(div_con(['5', '0', 9, 3, 2, 1, '9', 6, 7]), 14)
# test.assert_equals(div_con(['3', 6, 6, 0, '5', 8, 5, '6', 2,'0']), 13)
# test.assert_equals(div_con(['1', '5', '8', 8, 9, 9, 2, '3']), 11)
# test.assert_equals(div_con([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7]), 61)

def div_con(x):
    total_int = 0
    total_non_int = 0
    for val in x:
        if isinstance(val, str):
            total_non_int += int(val)
        else:
            total_int += val
    return total_int - total_non_int

def div_con(lst):
    return sum(n if isinstance(n, int) else -int(n) for n in lst)

