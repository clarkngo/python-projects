# Source: https://www.codewars.com/kata/52aeb2f3ad0e952f560005d3/train/python

# Sort the Gift Code

# Happy Holidays fellow Code Warriors!
# Santa's senior gift organizer Elf developed a way to represent up to 26 gifts by assigning a unique alphabetical character to each gift. After each gift was assigned a character, the gift organizer Elf then joined the characters to form the gift ordering code.

# Santa asked his organizer to order the characters in alphabetical order, but the Elf fell asleep from consuming too much hot chocolate and candy canes! Can you help him out?

# Sort the Gift Code
# Write a function called sortGiftCode/sort_gift_code/SortGiftCode that accepts a string containing up to 26 unique alphabetical characters, and returns a string containing the same characters in alphabetical order.

# Examples:
# sort_gift_code( 'abcdef' ) # 'abcdef'
# sort_gift_code( 'pqksuvy' ) # 'kpqsuvy'
# sort_gift_code( 'zyxwvutsrqponmlkjihgfedcba' ) # 'abcdefghijklmnopqrstuvwxyz'

class Solution:
    def sort_gift_code(self, code):
        arr_code = list(code)
        arr_code.sort()
        return ''.join(arr_code)

# other solution
# def sort_gift_code(code):
#     return "".join(sorted(code))      # sorted returns an array of an iterable
# Source: https://www.w3schools.com/python/ref_func_sorted.asp

import unittest

a = Solution()

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(a.sort_gift_code('ba'), 'ab')
    
    def test2(self):
        self.assertEqual(a.sort_gift_code('abcdef'), 'abcdef')
    
    def test3(self):
        self.assertEqual(a.sort_gift_code('pqksuvy'), 'kpqsuvy')
    
    def test4(self):
        self.assertEqual(a.sort_gift_code('zyxwvutsrqponmlkjihgfedcba'), 'abcdefghijklmnopqrstuvwxyz')


if __name__ == "__main__":
    unittest.main()
