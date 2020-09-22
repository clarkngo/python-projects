# import remove_dupl_return_len
# import unittest
# from parameterized import parameterized

# class TestSequence(unittest.TestCase):
#     @parameterized.expand([
#         [1, 2, 3],
#         [1, 2, 3],
#         [1, 2, 3],
#     ])
#     def test_sequence(self, a, 2):
#         self.assertEqual(a,2)

# class Test(unittest.TestCase):
#     def setUp(self):
#         expected = 3
#         actual = remove_dupl_return_len.removeDuplicates([1,2,2,3])

#     def test(self):
#         self.assertEqual(expected,actual)

# if __name__ == '__main__':
#     unittest.main()

import wo_dupl_return_len
import unittest

l = [[1, 2, 3], [2, 3, 4], [5, 6, 7]]

class TestSequense(unittest.TestCase):
    pass

def test_generator(a, b):
    def test(self):
        self.assertEqual(a,b)
    return test

if __name__ == '__main__':
    for t in l:
        test_name = str(t)
        test = test_generator(wo_dupl_return_len.returnLength(t), 3)
        setattr(TestSequense, test_name, test)
    unittest.main()
