import by_freq_by_order2 # code to test
import unittest # unit test framework

class Test_TestReturnValue(unittest.TestCase):
    def test_base_conversion(self):
        self.assertEqual(by_freq_by_order2.sort([ 7, 8, 8, 4, 1 ,2, 2, 2, 2, 7]), [2, 2, 2, 2, 7, 7, 8, 8, 4, 1])

if __name__ == '__main__':
    unittest.main()
