import interconvert_str_and_int # code to test
import unittest # unit test framework
import sys

### to_int ####
# Happy Path
class Test_String_123_ReturnAsInt_123(unittest.TestCase):
    def test_interconvert_str_and_int(self):
        self.assertEqual(interconvert_str_and_int.to_int('123'), 123)
        
class Test_String_Negative123_ReturnAsInt_Negative123(unittest.TestCase):
    def test_interconvert_str_and_int(self):
        self.assertEqual(interconvert_str_and_int.to_int('-123'), -123)

# 
class Test_PositiveString_ReturnAsGreaterThanOrEqualZeroInt(unittest.TestCase):
    def test_interconvert_str_and_int(self):
        self.assertGreaterEqual(interconvert_str_and_int.to_int('0'), 0)

class Test_NegativeString_ReturnAsLessThanZeroInt(unittest.TestCase):
    def test_interconvert_str_and_int(self):
        self.assertLess(interconvert_str_and_int.to_int('-1'), 0)

# edge cases
class Test_MaxValue_ReturnsNegativeOne(unittest.TestCase):
    def test_interconvert_str_and_int(self):
        self.assertEqual(interconvert_str_and_int.to_int('9223372036854775808'), -1)

class Test_EmptyString_ReturnsNegativeOne(unittest.TestCase):
    def test_interconvert_str_and_int(self):
        self.assertEqual(interconvert_str_and_int.to_int(''), -1)

class Test_EmptyString_ReturnsNegativeOne(unittest.TestCase):
    def test_interconvert_str_and_int(self):
        self.assertEqual(interconvert_str_and_int.to_int(None), -1)

# 
class Test_NegativeString_ReturnAsIntType(unittest.TestCase):
    def test_interconvert_str_and_int(self):
        self.assertTrue(type(interconvert_str_and_int.to_int('-1')) is int)

### to_str ####
# Happy Path
class Test_Int_123_ReturnAsString_123(unittest.TestCase):
    def test_interconvert_str_and_int(self):
        self.assertEqual(interconvert_str_and_int.to_str(123), '123')
        
class Test_Int_Negative123_ReturnAsInt_StringNegative123(unittest.TestCase):
    def test_interconvert_str_and_int(self):
        self.assertEqual(interconvert_str_and_int.to_str(-123), '-123')

class Test_None_ReturnsStringNotValid(unittest.TestCase):
    def test_interconvert_str_and_int(self):
        self.assertEqual(interconvert_str_and_int.to_str(None), "not valid")

class Test_FloatType_ReturnsStringNotValid(unittest.TestCase):
    def test_interconvert_str_and_int(self):
        self.assertEqual(interconvert_str_and_int.to_str(0.0), "not valid")

if __name__ == '__main__':
    unittest.main()
