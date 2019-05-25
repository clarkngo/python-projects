import ret_val # code to test
import unittest # unit test framework

class Test_TestReturnValue(unittest.TestCase):
    def test_ret_val(self):
        self.assertEqual(ret_val.return_value('hello'), 'hello')

if __name__ == '__main__':
    unittest.main()
