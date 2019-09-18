# source: https://dbader.org/blog/python-reverse-string

def reverse_string1(s):
    """Return a reversed copy of `s`"""
    return s[::-1]

def reverse_string2(s):
    """Return a reversed copy of `s`"""
    return "".join(reversed(s))

def reverse_string3(s):
    """Return a reversed copy of `s`"""
    chars = list(s)
    for i in range(len(s) // 2):
        tmp = chars[i]
        chars[i] = chars[len(s) - i - 1]
        chars[len(s) - i - 1] = tmp
    return ''.join(chars)

print("Input: TURBO")
print("Output in 3 different string reversal:")
print("Slicing:")
print(reverse_string1('TURBO'))
print("reverse + join:")
print(reverse_string2('TURBO'))
print("class / in-place:")
print(reverse_string3('TURBO'))
print("new string with for loop:")
print(reverse_string3('TURBO'))
print()

print("Performance comparison - repeat 3x and time in seconds:")
print("Input string:")
print("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz")
import timeit
s = 'abcdefghijklmnopqrstuvwxyz' * 5
print()
print("Slicing:")
print(timeit.repeat(lambda: reverse_string1(s)))
print("reverse + join:")
print(timeit.repeat(lambda: reverse_string2(s)))
print("classic / in-place:")
print(timeit.repeat(lambda: reverse_string3(s)))
