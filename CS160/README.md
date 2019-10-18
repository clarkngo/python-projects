# Coding Challenges
## String Problems
1. Write a Python program to calculate the length of a string.
2. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string
- Sample String : 'w3resource'
- Expected Result : 'w3ce'
- Sample String : 'w3'
- Expected Result : 'w3w3'
- Sample String : ' w'
- Expected Result : Empty String
3. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
- Sample String : 'restart'
- Expected Result : 'resta$t'
4. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string
- Sample String : 'abc', 'xyz'
- Expected Result : 'xyc abz'
5. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
- Sample String : 'abc'
- Expected Result : 'abcing'
- Sample String : 'string'
- Expected Result : 'stringly'
6. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
- Sample String : 'The lyrics is not that poor!'
- 'The lyrics is poor!'
- Expected Result : 'The lyrics is good!'
- 'The lyrics is poor!'
7. Write a Python function that takes a list of words and returns the length of the longest one.
8. Write a Python program to remove the characters which have odd index values of a given string.
9. Write a Python program to count the occurrences of each word in a given sentence.
10. Write a Python function to create the HTML string with tags around the word(s)
### Answers to String Problems
1. Write a Python program to calculate the length of a string.
```
def string_length(str1):
    count = 0
    for char in str1:
        count += 1
    return count
print(string_length('w3resource.com'))
```
2. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string
- Sample String : 'w3resource'
- Expected Result : 'w3ce'
- Sample String : 'w3'
- Expected Result : 'w3w3'
- Sample String : ' w'
- Expected Result : Empty String
```
def string_both_ends(str):
  if len(str) < 2:
    return ''

  return str[0:2] + str[-2:]

print(string_both_ends('w3resource'))
print(string_both_ends('w3'))
print(string_both_ends('w'))
```
3. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
- Sample String : 'restart'
- Expected Result : 'resta$t'
```
def change_char(str1):
  char = str1[0]
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:]

  return str1

print(change_char('restart'))
```

4. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string
- Sample String : 'abc', 'xyz'
- Expected Result : 'xyc abz'
```
def chars_mix_up(a, b):
  new_a = b[:2] + a[2:]
  new_b = a[:2] + b[2:]

  return new_a + ' ' + new_b
print(chars_mix_up('abc', 'xyz'))
```
5. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
- Sample String : 'abc'
- Expected Result : 'abcing'
- Sample String : 'string'
- Expected Result : 'stringly'
```
def add_string(str1):
  length = len(str1)

  if length > 2:
    if str1[-3:] == 'ing':
      str1 += 'ly'
    else:
      str1 += 'ing'

  return str1
print(add_string('ab'))
print(add_string('abc'))
print(add_string('string'))
```

6. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
- Sample String : 'The lyrics is not that poor!'
- 'The lyrics is poor!'
- Expected Result : 'The lyrics is good!'
- 'The lyrics is poor!'
```
def not_poor(str1):
  snot = str1.find('not')
  spoor = str1.find('poor')


  if spoor > snot and snot>0 and spoor>0:
    str1 = str1.replace(str1[snot:(spoor+4)], 'good')
    return str1
  else:
    return str1
print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))
```
7. Write a Python function that takes a list of words and returns the length of the longest one.
```
def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][1]

print(find_longest_word(["PHP", "Exercises", "Backend"]))
```
8. Write a Python program to remove the characters which have odd index values of a given string.
```
def odd_values_string(str):
  result = ""
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result

print(odd_values_string('abcdef'))
print(odd_values_string('python'))
```
9. Write a Python program to count the occurrences of each word in a given sentence.
```
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('the quick brown fox jumps over the lazy dog.'))
```
10. Write a Python function to create the HTML string with tags around the word(s)
```
def add_tags(tag, word):
	return "<%s>%s</%s>" % (tag, word, tag)
print(add_tags('i', 'Python'))
print(add_tags('b', 'Python Tutorial'))
```
## Function Problems
1. Write a Python function to sum all the numbers in a list.
- Sample List : (8, 2, 3, 0, 7)
- Expected Output : 20
2. Write a Python program to reverse a string.
- Sample String : "1234abcd"
- Expected Output : "dcba4321"
3. Write a Python program to print the even numbers from a given list.
- Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
- Expected Result : [2, 4, 6, 8]
4. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
- Sample Items : green-red-yellow-black-white
- Expected Result : black-green-red-white-yellow
5. Write a Python function to find the Max of three numbers.
6. Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included).
7. Write a Python function to check whether a number is in a given range.
- Sample Input: 1
- Expected Output: 5 is in the range
8. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
- Sample String : 'The quick Brow Fox'
- Expected Output :
- No. of Upper case characters : 3
- No. of Lower case Characters : 12
9. Write a Python function that takes a number as a parameter and check the number is prime or not.
Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.
10. Write a Python function that prints out the first n rows of Pascal's triangle.
Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together

### Answers to Function Problems
1. Write a Python function to sum all the numbers in a list.
- Sample List : (8, 2, 3, 0, 7)
- Expected Output : 20
```
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((8, 2, 3, 0, 7)))
```
2. Write a Python program to reverse a string.
- Sample String : "1234abcd"
- Expected Output : "dcba4321"
```
def string_reverse(str1):

    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[ index - 1 ]
        index = index - 1
    return rstr1
print(string_reverse('1234abcd'))
```
3. Write a Python program to print the even numbers from a given list.
- Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
- Expected Result : [2, 4, 6, 8]
```
def is_even_num(l):
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum
print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))
```
4. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
- Sample Items : green-red-yellow-black-white
- Expected Result : black-green-red-white-yellow
```
items=[n for n in input().split('-')]
items.sort()
print('-'.join(items))
```
5. Write a Python function to find the Max of three numbers.
```
def max_of_two( x, y ):
    if x > y:
        return x
    return y
def max_of_three( x, y, z ):
    return max_of_two( x, max_of_two( y, z ) )
print(max_of_three(3, 6, -5))
```
6. Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included).
```
def printValues():
	l = list()
	for i in range(1,21):
		l.append(i**2)
	print(l)

printValues()
```
7. Write a Python function to check whether a number is in a given range.
- Sample Input: 1
- Expected Output: 5 is in the range
```
def test_range(n):
    if n in range(3,9):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
test_range(5)
```
8. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
- Sample String : 'The quick Brow Fox'
- Expected Output :
- No. of Upper case characters : 3
- No. of Lower case Characters : 12
```
def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('The quick Brown Fox')
```
9. Write a Python function that takes a number as a parameter and check the number is prime or not.
Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.
```
def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True
print(test_prime(9))
```
10. Write a Python function that prints out the first n rows of Pascal's triangle.
Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together
```
def pascal_triangle(n):
   trow = [1]
   y = [0]
   for x in range(max(n,0)):
      print(trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
   return n>=1
pascal_triangle(6)
```
Sources:
- https://www.w3resource.com/python-exercises/string/
- https://www.w3resource.com/python-exercises/python-functions-exercises.php
