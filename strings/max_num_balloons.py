# Source: https://leetcode.com/problems/maximum-number-of-balloons/
# Maximum Number of Balloons

# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.

# Example 1:
# Input: text = "nlaebolko"
# Output: 1

# Example 2:
# Input: text = "loonbalxballpoon"
# Output: 2

# Example 3:
# Input: text = "leetcode"
# Output: 0

# Constraints:

# 1 <= text.length <= 10^4
# text consists of lower case English letters only.

# Runtime: 32 ms, faster than 90.17% of Python3 online submissions for Maximum Number of Balloons.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Maximum Number of Balloons.

class Solution:
    # def maxNumberOfBalloons(self, text: str) -> int:
    #     # this is DUMB, why did I even create two dictionaries (╯°□°)╯︵ ┻━┻
    #     single_dict = {
    #         "b": 0,
    #         "a": 0,
    #         "n": 0
    #     }
    #     double_dict = {
    #         "l": 0,
    #         "o": 0
    #     }
    #     # iterate over string
    #     for char in text:
    #         if char in single_dict:
    #             single_dict[char] += 1
    #         elif char in double_dict:
    #             double_dict[char] += 1
    #     # get the minimum key for each dictionary
    #     single_key_min = min(single_dict, key=single_dict.get)
    #     double_key_min = min(double_dict, key=double_dict.get)
    #     # update dictionary values with the mininum values
    #     single_dict = {x: single_dict[single_key_min] for x in single_dict}
    #     double_dict = {x: double_dict[double_key_min] for x in double_dict}
    #     # divide everything by 2 in double dictionary
    #     double_dict = {x: double_dict[double_key_min] // 2 for x in double_dict}
    #     # get the values for both dictionaries
    #     single_chars = single_dict["b"]
    #     double_chars = double_dict["l"]
    #     # edge case
    #     if single_chars == 0 or double_chars == 0:
    #         return 0
    #     elif single_chars >= double_chars:
    #         return double_chars
    #     else:
    #         return 0

    # import collections
    # def maxNumberOfBalloons(self, text: str) -> int:
    #     cnt = collections.Counter(text)
    #     cntBalloon = collections.Counter('balloon')
    #     return min([cnt[c] // cntBalloon[c] for c in cntBalloon])

# Runtime: 32 ms, faster than 90.17% of Python3 online submissions for Maximum Number of Balloons.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Maximum Number of Balloons.

    def maxNumberOfBalloons(self, text: str) -> int:
        my_dict = {
            "b": 0,
            "a": 0,
            "l": 0,
            "o": 0,
            "n": 0
        }
        for char in text:
            if char in my_dict:
                my_dict[char] += 1
        minKey = min(my_dict, key=my_dict.get)
        if my_dict[minKey] == 0: return 0
        else:
            my_dict["o"] = my_dict["o"] // 2
            my_dict["l"] = my_dict["l"] // 2
            newMinKey = min(my_dict, key=my_dict.get)
        return my_dict[newMinKey]

a = Solution
import unittest
class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(a.maxNumberOfBalloons(self, "nlaebolko"), 1)
    def test2(self):
        self.assertEqual(a.maxNumberOfBalloons(self, "krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"), 10)
    def test3(self):
        self.assertEqual(a.maxNumberOfBalloons(self, "lloo"), 0)

if __name__ == '__main__':
    unittest.main()
