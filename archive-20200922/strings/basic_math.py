# Source: https://www.codewars.com/kata/5809b62808ad92e31b000031/train/python

# Basic Math (Add or Subtract)

# In this kata, you will do addition and subtraction on a given string. The return value must be also a string.

# Note: the input will not be empty.

# Examples
# "1plus2plus3plus4"  --> "10"
# "1plus2plus3minus4" -->  "2"

# Regex Solution
# import re

# class Solution:
#     def calculate(self, s):
#         arr = re.split("(\d+)", s)
#         arr.pop(0)
#         arr.pop()
#         total = int(arr[0])
#         for i in range(1, len(arr),2):
#             if arr[i] == 'plus':
#                 total += int(arr[i+1])
#             else:
#                 total -= int(arr[i+1])

#         return str(total)

# Without Regex
class Solution:
    def calculate(self, s: str) -> str:
        list_arr = list(s)
        arr = []
        word = ''
        digit = ''
        for char in list_arr:
            if ord(char) >= 97 and ord(char) <= 122:
                arr.append(digit)
                digit = ''
                word += char
            else:
                arr.append(word)
                word = ''
                digit += char

        arr.append(digit)       # add last digits

        # using remove() to 
        # perform removal 
        while("" in arr) : 
            arr.remove("")
            
        total = int(arr[0])     # fence post
        for i in range(1, len(arr),2):
            if arr[i] == 'plus':
                total += int(arr[i+1])
            else:
                total -= int(arr[i+1])

        return str(total)

# other solution
# def calculate(s):
#     return str(sum(int(n) for n in s.replace("minus", "plus-").split("plus")))
    
#     # I heard here and there that using eval is a very bad practice…
#     #return str(eval(s.replace("plus", "+").replace("minus", "-")))

a = Solution()

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(a.calculate('1plus2plus3plus4'), '10')
        
    def test2(self):
        self.assertEqual(a.calculate('1plus2plus3minus4'), '2')
        
    def test3(self):
        self.assertEqual(a.calculate('1minus2minus3minus4'), '-8')

    def test4(self):
        self.assertEqual(a.calculate('521plus947minus876plus730minus556'), '766')

if __name__ == '__main__':
    unittest.main()
