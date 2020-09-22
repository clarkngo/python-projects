# https://www.codewars.com/kata/57cfdf34902f6ba3d300001e/train/python

# Sort and Star

# You will be given an vector of string(s). You must sort it alphabetically (case-sensitive!!) and then return the first value.

# The returned value must be a string, and have "***" between each of its letters.

# You should not remove or add elements from/to the array.

# my solution
def two_sort(array):
    new_list = sorted(array)
    word = new_list[0]
    res = ''
    for i in range(len(word)-1):
        res += word[i] + '***'
    res += word[-1]
    return res

def two_sort(array):
        return ''.join(sorted(array)[0][i] + '***' for i in range(len(sorted(array)[0])))[:-3]

# other solution
def two_sort(lst):
    return '***'.join(min(lst))

