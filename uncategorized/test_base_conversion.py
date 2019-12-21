import base_conversion # code to test
import unittest # unit test framework

class Test_TestReturnValue(unittest.TestCase):
    def test_base_conversion(self):
        self.assertEqual(base_conversion.toDeci('11A', 16), 282)

if __name__ == '__main__':
    unittest.main()
