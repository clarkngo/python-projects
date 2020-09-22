import merge_sorted_arrays # code to test
import unittest # unit test framework

class Test_combination1(unittest.TestCase):
    def test_merge_sorted_arrays(self):
        self.assertEqual(merge_sorted_arrays.merge([1,2,3,0,0,0],[2,5,6]), [1,2,2,3,5,6])

class Test_combination2(unittest.TestCase):
    def test_merge_sorted_arrays(self):
        self.assertEqual(merge_sorted_arrays.merge([2,5,6,0,0,0],[1,2,3]), [1,2,2,3,5,6])

class Test_combination3(unittest.TestCase):
    def test_merge_sorted_arrays(self):
        self.assertEqual(merge_sorted_arrays.merge([2,5,6,0,0,0],[1,2,4]), [1,2,2,4,5,6])

class Test_combination4(unittest.TestCase):
    def test_merge_sorted_arrays(self):
        self.assertEqual(merge_sorted_arrays.merge([2,5,6,8,0,0],[1,1]), [1,1,2,5,6,8])

if __name__ == '__main__':
    unittest.main()
