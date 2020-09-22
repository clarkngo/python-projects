import by_freq_by_order2 # code to test
import unittest # unit test framework

class Test_Combination1(unittest.TestCase):
    def test_freq_by_order(self):
        self.assertEqual(by_freq_by_order2.sort([ 7, 8, 8, 4, 1 ,2, 2, 2, 2, 7]), [2, 2, 2, 2, 7, 7, 8, 8, 4, 1])

class Test_Combination2(unittest.TestCase):
    def test_freq_by_order(self):
        self.assertEqual(by_freq_by_order2.sort([ 7, 8, 4, 1 ,2, 2, 2, 2, 7, 8]), [2, 2, 2, 2, 7, 7, 8, 8, 4, 1])

class Test_Combination3(unittest.TestCase):
    def test_freq_by_order(self):
        self.assertEqual(by_freq_by_order2.sort([ 7, 8, 4, 1 ,2, 7, 8, 2, 2, 2]), [2, 2, 2, 2, 7, 7, 8, 8, 4, 1])

class Test_Combination4(unittest.TestCase):
    def test_freq_by_order(self):
        self.assertEqual(by_freq_by_order2.sort([ 7, 7, 8, 8, 4, 1 ,2, 2, 2, 2]), [2, 2, 2, 2, 7, 7, 8, 8, 4, 1])


if __name__ == '__main__':
    unittest.main()
