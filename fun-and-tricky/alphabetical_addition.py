# https://www.codewars.com/kata/5d50e3914861a500121e1958/train/python

# Alphabetical Addition

# Your task is to add up letters to one letter.

# The function will be given a variable amount of arguments, each one being a letter to add.

# Notes:
# Letters will always be lowercase.
# Letters can overflow (see second to last example of the description)
# If no letters are given, the function should return 'z'
# Examples:
# add_letters('a', 'b', 'c') = 'f'
# add_letters('a', 'b') = 'c'
# add_letters('z') = 'z'
# add_letters('z', 'a') = 'a'
# add_letters('y', 'c', 'b') = 'd' # notice the letters overflowing
# add_letters() = 'z'

# my solution
def add_letters(*letters):
    # a is 97 ... z is 122
    if not letters: return 'z'
    total = 0
    for ch in letters:
        total += ord(ch) - 96
    while total > 26:
        total -= 26

    return chr(total + 96)

# other solution
def add_letters(*letters):
    return chr( (sum(ord(c)-96 for c in letters)-1)%26 + 97)
