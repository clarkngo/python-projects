# https://www.codewars.com/kata/5dd5128f16eced000e4c42ba/train/python

# Most valuable character

# In this Kata, you will be given a string and your task is to return the most valuable character. The value of a character is the difference between the index of its last occurrence and the index of its first occurrence. Return the character that has the highest value. If there is a tie, return the lexicographically lowest character.

# All inputs will be lower case.

# For example:
# solve('a') = 'a'
# solve('ab') = 'a'. Last occurrence is equal to first occurrence of each character. Return lexicographically lowest.
# solve("axyzxyz") = 'x'


def solve(st):
    print(st)
    import sys
    my_dict = {}
    maximum = -sys.maxsize - 1
    lowest_char = sys.maxsize
    for i in range(len(st)):
        if st[i] not in my_dict:
            my_dict[st[i]] = 1
        else:
            my_dict[st[i]] += 1
    for value in my_dict.values():
        if value > maximum:
          maximum = value
    for key, value in my_dict.items():
        if value == maximum and ord(key) < lowest_char:
            lowest_char = ord(key)

    return chr(lowest_char)

import string
my_dict = dict.fromkeys(string.ascii_lowercase, 0)
# output:
# {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0,'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

