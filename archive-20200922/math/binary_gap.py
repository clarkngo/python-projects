# A binary gap within a positive integer N is any maximal sequence of consecutive zeros
# that is surrounded by ones at both ends in the binary representation of N.

# For example, number 9 has binary representation 1001 and contains a binary gap of length 2.
# The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3.
# The number 20 has binary representation 10100 and contains one binary gap of length 1.
# The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

# find first occurence of 1 digits from the right
# then remove all the 0 digits from its left

# def sliceFromLastOccurence(arr):
#     for index, digit in reversed(list(enumerate(arr))):
#         if digit == '1':
#             arr = arr[:index+1:]
#             break
#     return arr

# # using List Slice + index()
# # to get last element occurrence
# # then return slice from its right

# def sliceFromLastOccurence2(arr):

#     res = len(arr) - 1 - arr[::-1].index('1')
#     return arr[:res+1]


# find longest gap
class Solution:
    def longest_gap(self, strng: str) -> int:
        longest = 0
        count = 0
        for i in range(1, len(strng)):
            if strng[i] == '0':
                count += 1
            else:
                if count > longest:
                    longest = count
                count = 0
        return longest

binaryStr = "{0:b}".format(10000)

a = Solution
import unittest
class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(a.longest_gap(self, "{0:b}".format(10000)), 3)
    def test2(self):
        self.assertEqual(a.longest_gap(self, "{0:b}".format(1041)), 5)
    def test3(self):
        self.assertEqual(a.longest_gap(self, "{0:b}".format(15)), 0)
    def test4(self):
        self.assertEqual(a.longest_gap(self, "{0:b}".format(32)), 0)
    def test5(self):
        self.assertEqual(a.longest_gap(self, "{0:b}".format(1)), 0)

if __name__ == '__main__':
    unittest.main()
