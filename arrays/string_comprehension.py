# https://leetcode.com/problems/string-compression/

# String Compression

# Given an array of characters, compress it in-place.

# The length after compression must always be smaller than or equal to the original array.

# Every element of the array should be a character (not int) of length 1.

# After you are done modifying the input array in-place, return the new length of the array.


# Follow up:
# Could you solve it using only O(1) extra space?


# Example 1:

# Input:
# ["a","a","b","b","c","c","c"]

# Output:
# Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

# Explanation:
# "aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".


# Example 2:

# Input:
# ["a"]

# Output:
# Return 1, and the first 1 characters of the input array should be: ["a"]

# Explanation:
# Nothing is replaced.


# Example 3:

# Input:
# ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

# Output:
# Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

# Explanation:
# Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
# Notice each digit has it's own entry in the array.


# Note:

# All characters have an ASCII value in [35, 126].
# 1 <= len(chars) <= 1000.

from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1: return 1
        count = 1
        j = 0
        flag = False
        for i in range(1, len(chars)):
            while i < len(chars) and chars[i-1] == chars[i]:
                count += 1
                chars.pop(i)
                flag = True
            if flag:
                while count >= 10:
                  chars.insert(i, str(count//10))
                  count = count % 10
                  j+= 1
                chars.insert(i+j, str(count))
                j = 0
                flag = False
                count = 1
        print(chars)
        return len(chars)

import unittest
a = Solution()
class Test(unittest.TestCase):
	def test1(self):
		self.assertEqual(a.compress(["a"]), 1)
	def test2(self):
		self.assertEqual(a.compress(["a","a","b","b"]), 4)
	def test3(self):
		self.assertEqual(a.compress(["a","b","b"]), 3)
	def test4(self):
		self.assertEqual(a.compress(["a","b","b","b","b","b","b","b","b","b","b","b"]), 4)
	def test5(self):
		self.assertEqual(a.compress(["a","a","b","b","c","c","c"]), 6)
	def test6(self):
		self.assertEqual(a.compress(["a","a","a","b","b","a","a"]), 6)
	def test7(self):    # ['a', '6', 'b', '1', '2', 'c', '1', '4']
		self.assertEqual(a.compress(["a","a","a","a","a","a","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","c","c","c","c","c","c","c","c","c","c","c","c","c","c"]), 8)
	def test8(self):
		self.assertEqual(a.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]), 4)

	def test9(self):  # ["p","4","m","2","b","5","u","2","r","2","u","n","1","1","u","4","a","2","u","2","r","3","s","2","a","2","y","3","g","5"]
        # wrong       ["p","4","m","2","b","5","u","2","r","2","u","n","1","2","u","4","a","2","u","2","r","3","s","2","a","2","y","3","g","5"]
		self.assertEqual(a.compress(["p","p","p","p","m","m","b","b","b","b","b","u","u","r","r","u","n","n","n","n","n","n","n","n","n","n","n","u","u","u","u","a","a","u","u","r","r","r","s","s","a","a","y","y","y","g","g","g","g","g"]), 30)
if __name__ == '__main__':
    unittest.main()
