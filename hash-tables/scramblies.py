# Source: https://www.codewars.com/kata/55c04b4cc56a697bb0000048/train/python

# Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

# Notes:

# Only lower case letters will be used (a-z). No punctuation or digits will be included.
# Performance needs to be considered
# Input strings s1 and s2 are null terminated.
# Examples
# scramble('rkqodlw', 'world') ==> True
# scramble('cedewaraaossoqqyt', 'codewars') ==> True
# scramble('katas', 'steak') ==> False

# Test.assert_equals(scramble('rkqodlw', 'world'),  True)
# Test.assert_equals(scramble('cedewaraaossoqqyt', 'codewars'), True)
# Test.assert_equals(scramble('katas', 'steak'), False)
# Test.assert_equals(scramble('scriptjava', 'javascript'), True)
# Test.assert_equals(scramble('scriptingjava', 'javascript'), True)

# performance not met
def scramble(s1, s2):
    my_dict = {}

    # iterate over s1
    # add char as key and add frequency as value of s1
    for i in range(len(s1)):
        if s1[i] not in my_dict:
            my_dict[s1[i]] = 1
        else:
            my_dict[s1[i]] += 1

    # iterate over s2
    # minus frequency value whenever char is found
    for j in range(len(s2)):
        if s2[j] not in my_dict:
            return False
        else:
            my_dict[s2[j]] -= 1

    # dict values converted to list
    # negative int means the char of s1 not sufficient for char of s2
    numList = my_dict.values()
    for num in numList:
        if num < 0:
            return False
    return True

# performance not met
def scramble2(s1, s2):
    my_dict = {}
    # iterate over s1
    # add char as key and add frequency as value of s1
    for i in range(len(s1)):
        if s1[i] not in my_dict:
            my_dict[s1[i]] = 1
        else:
            my_dict[s1[i]] += 1

    # iterate over s2
    # minus frequency value whenever char is found
    for j in range(len(s2)):
        if s2[j] not in my_dict:
            return False
        else:
            my_dict[s2[j]] -= 1

    # return true if there's no values with -1 or less
    return not any(x < 0 for x in my_dict.values())
