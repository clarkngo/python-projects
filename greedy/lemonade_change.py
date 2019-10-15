# Source: https://leetcode.com/problems/lemonade-change/

# Lemonade Change
# At a lemonade stand, each lemonade costs $5.

# Customers are standing in a queue to buy from you, and order one at a time
# (in the order specified by bills).

# Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.
# You must provide the correct change to each customer, so that the net transaction is
# that the customer pays $5.

# Note that you don't have any change in hand at first.

# Return true if and only if you can provide every customer with correct change.



# Example 1:

# Input: [5,5,5,10,20]
# Output: true
# Explanation:
# From the first 3 customers, we collect three $5 bills in order.
# From the fourth customer, we collect a $10 bill and give back a $5.
# From the fifth customer, we give a $10 bill and a $5 bill.
# Since all customers got correct change, we output true.

import unittest # unit test framework
from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change_for_cust: int = 0
        dict: object = {"5": 0, "10": 0, "20": 0}

        # no change for first customer
        if bills[0] == 10 or bills[0] == 20:
            return False
        else:
            # if 1 customer and pays 5 usd
            if len(bills) == 1:
                return True
            dict[str(bills[0])] += 1

        for i in range(1, len(bills)):
            if bills[i] == 10:
                if dict.values("10") < 0:
                    dict.values("10") -= 1





a = Solution
class Test(unittest.TestCase):

    def test_5usd(self):
        self.assertEqual(a.lemonadeChange(self,[5]), True)

    def test_10usd(self):
        self.assertEqual(a.lemonadeChange(self,[10,20,5]), False)

    def test_20usd(self):
        self.assertEqual(a.lemonadeChange(self,[10,20,5]), False)

    def test_2nd_20usd(self):
        self.assertEqual(a.lemonadeChange(self,[5,20,5]), False)

    def test_3rd_20usd(self):
        self.assertEqual(a.lemonadeChange(self,[5,5,]), False)
    # def test(self):
    #     self.assertEqual(a.lemonadeChange(self,[5,5,5,10,20]), True)

if __name__ == '__main__':
    unittest.main()

