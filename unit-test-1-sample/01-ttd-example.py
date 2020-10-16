import unittest # unit test framework

class Solution:
    def plus_seven_to_positive_num(self, x):
        return

a = Solution
class Test(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(a.plusSeven(self,100), 107)

    def test_negative_num(self):
        self.assertEqual(a.plusSeven(self,-100), 0)


    def test_more_than_100(self):
        self.assertEqual(a.plusSeven(self,-100), 0)

    # def test_input_as_str_type(self):
    #     self.assertEqual(type(a.plusSeven("100")), False)

    # def test_empty(self):
    #     self.assertEqual(a.plusSeven(1), 1)

if __name__ == '__main__':
    unittest.main()
