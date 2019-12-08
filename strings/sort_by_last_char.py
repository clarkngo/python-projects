# https://www.codewars.com/kata/57eba158e8ca2c8aba0002a0/train/python

# Sort by Last Char

# Given a string of words (x), you need to return an array of the words, sorted alphabetically by the final character in each.

# If two words have the same last letter, they returned array should show them in the order they appeared in the given string.

# All inputs will be valid.

# Test.describe("Basic Tests")
# Test.assert_equals(last("man i need a taxi up to ubud"), ["a", "need", "ubud", "i", "taxi", "man", "to", "up"])
# Test.assert_equals(last("what time are we climbing up the volcano"), ["time", "are", "we", "the", "climbing", "volcano", "up", "what"])
# Test.assert_equals(last("take me to semynak"), ["take", "me", "semynak", "to"])
# Test.assert_equals(last("massage yes massage yes massage"), ["massage", "massage", "massage", "yes", "yes"])
# Test.assert_equals(last("take bintang and a dance please"), ["a", "and", "take", "dance", "please", "bintang"])

# my solution
def last(s):
    lst = s.split(" ")
    last_chars = []
    sorted_by_last_char = []
    for i in range(len(lst)):
        last_chars.append(lst[i][-1])
    last_chars.sort()
    print(last_chars)
    while last_chars != []:
        for j in range(len(lst)):
            if last_chars[0] == lst[j][-1]:
                sorted_by_last_char.append(lst[j])
                lst.pop(j)
                last_chars.pop(0)
                break
    return sorted_by_last_char

# best practice solution
def last(s):
    return sorted(s.split(), key=lambda x: x[-1])
