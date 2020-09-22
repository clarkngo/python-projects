# Source: https://leetcode.com/problems/uncommon-words-from-two-sentences/submissions/

# We are given two sentences A and B.  (A sentence is a string of space
# separated words.  Each word consists only of lowercase letters.)
# A word is uncommon if it appears exactly once in one of the sentences,
# and does not appear in the other sentence.
# Return a list of all uncommon words.
# You may return the list in any order.

# Example 1:

# Input: A = "this apple is sweet", B = "this apple is sour"
# Output: ["sweet","sour"]
# Example 2:

# Input: A = "apple apple", B = "banana"
# Output: ["banana"]

# Runtime: 32 ms, faster than 95.15% of Python3 online submissions
# for Uncommon Words from Two Sentences.

# Memory Usage: 13.9 MB, less than 9.09% of Python3 online submissions
# for Uncommon Words from Two Sentences.

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        word_dict = {}
        A_words = A.split(" ")
        B_words = B.split(" ")
        for word in A_words:
            if word not in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] += 1
        for word in B_words:
            if word not in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] += 1
        return [key for (key, value) in word_dict.items() if value == 1]
