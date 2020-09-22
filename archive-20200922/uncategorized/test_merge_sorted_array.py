import merge_sorted_arrays # code to test
import unittest # unit test framework

class Test_test(unittest.TestCase):
    def test_merge_sorted_arrays(self):
        self.assertEqual(merge_sorted_arrays.merge([1,2,3,0,0,0],[2,5,6]), [1,2,2,3,5,6])

if __name__ == '__main__':
    unittest.main()
