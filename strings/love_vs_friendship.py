# https://www.codewars.com/kata/59706036f6e5d1e22d000016/train/python

# If　a = 1, b = 2, c = 3 ... z = 26

# Then l + o + v + e = 54

# and f + r + i + e + n + d + s + h + i + p = 108

# So friendship is twice stronger than love :-)

# The input will always be in lowercase and never be empty.

# test.assert_equals(words_to_marks('attitude'), 100)
# test.assert_equals(words_to_marks('friends'), 75)
# test.assert_equals(words_to_marks('family'), 66)
# test.assert_equals(words_to_marks('selfness'), 99)
# test.assert_equals(words_to_marks('knowledge'), 96)

def words_to_marks(s):
    # Easy one
    result = 0
    for chr in s:
        result += ord(chr) - 96
    return result

