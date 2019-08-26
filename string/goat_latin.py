# Source: https://leetcode.com/problems/goat-latin/

# A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

# We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

# The rules of Goat Latin are as follows:

# If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
# For example, the word 'apple' becomes 'applema'.

# If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
# For example, the word "goat" becomes "oatgma".

# Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
# For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
# Return the final sentence representing the conversion from S to Goat Latin.


class Solution:
  def toGoatLatin(self, S: str) -> str:
      new_sentence = ""             # initialize a string variable
      words = S.split(" ")          # convert sentence string to list
      i = 1                         # initialize a counter
      for word in words:            # iterate the list

          # word starting with vowel: add 'ma' at the end
          if (word[0] == "a" or word[0] == "A" or
              word[0] == "e" or word[0] == "E" or
              word[0] == "i" or word[0] == "I" or
              word[0] == "o" or word[0] == "O" or
              word[0] == "u" or word[0] == "U"):
              new_sentence += " " + word + "ma"

          # word starting with consonant:
          # move first letter to the end of the word and add 'ma' at the end
          else:
              # [1:] return word without first character
              # [:1] return first character of the word only
              new_sentence += " " + word[1:] + word[:1] + "ma"

          # add 'a' to the word depending on the index, starting at 1
          new_sentence += "a" * i
          i += 1  # increment counter for 'a'

      # return setence without the first ' ' to deal with fence post
      return new_sentence[1:]

s = Solution()
s.toGoatLatin("I speak Goat Latin")
