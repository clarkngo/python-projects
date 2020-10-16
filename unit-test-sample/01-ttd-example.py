import unittest # unit test framework

class Solution:
    def plus_seven_to_positive_num(self, x):
        return -1 if x > 100 or x < 0 else x + 7

a = Solution
class Test(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(a.plus_seven_to_positive_num(self,100), 107)

    def test_negative_num(self):
        self.assertEqual(a.plus_seven_to_positive_num(self,-100), -1)


    def test_more_than_100(self):
        self.assertEqual(a.plus_seven_to_positive_num(self,101), -1)

if __name__ == '__main__':
    unittest.main()
