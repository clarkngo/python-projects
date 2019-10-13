# Source: https://leetcode.com/problems/first-unique-character-in-a-string/

# First Unique Character in a String

# Given a string, find the first non-repeating character
# in it and return it's index. If it doesn't exist,
# return -1.

import unittest # unit test framework
from typing import List

class Solution:
    def firstUniqChar(self, s: str) -> int:
        my_dict = {}
        for i in range(len(s)):
            if s[i] not in my_dict:
                my_dict[s[i]] = [i, 1]      # [index, count]
            else:
                my_dict[s[i]][1] += 1
        arr = list(my_dict.values())

        # linear search first occurence of 1 count
        for j in range(len(arr)):
            # if count of character is 1
            if arr[j][1] == 1:
                return arr[j][0]    # return index



a = Solution()
class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(a.firstUniqChar("leetcode"), 0)

    def test2(self):
        self.assertEqual(a.firstUniqChar("loveleetcode"), 2)

if __name__ == '__main__':
    unittest.main()
