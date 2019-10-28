"""
This is the first Python program.
"""
import math

x = 1                       # int
y = 3.14                    # float
name = 'City U @ Seattle'   # str
is_cool = True              # bool

# Multiple assignment
x, y, name, is_cool = (1, 3.14, 'City U @ Seattle', True)

# print the values of each variable
print(x)
print(name)

print(type(x))          # getting the type information of variables
print(type(is_cool))

# Type conversion (casting)
x = str(x)
print(type(x))          # getting the type information of variables

y = int(y)
print(type(y))          # type conversion

z = float(y)
print(type(z))  
print(z)

a = 5
b = 6
c = 2
a/c
b/c

# unary operator
a ** c
-b
+b
a//c
round(a/c)
round(3.141592, 3)
round(3.141592, 4)
round(3.141549, 4)

a + b
a - b
a * b
a / b
a % b
abs(-1)
a**b
math.sqrt(a)

# associativitiy precedence
5 * 2 % 3
5 * (2 % 3)
# L -- R (if they have the same precedence, L first)
# but here is one operator that has R-L associativity
2 ** 3 ** 2
(2 ** 3) ** 2
2 ** (3 ** 2) # right first then left

# type precedence int * float = float
2 * 2.3

import keyword
keyword.iskeyword('xor')
keyword.iskeyword('or')



# String Manipulation, string is a type expressed inside single quotes
name = 'Tom'
age  = 40
# concatenation
print('Hello, My name is ' + name + ' and I am ' + str(age)) # age --> str(age)

a = 'City'
b = 'University'
(a + ' ' + b)
('a' + 'b') * 5

brd = '''
-+-+-
X| |
-+-+-
 |O|
-+-+-
 |O|O
-+-+-
'''
print(brd)

# formating by position
print('Hello, My name is {str1} and I am {str2}'.format(str1 = name, str2 = age))

# Formatted string
print(f'Hello, My name is {name} and I am {age}')

# Some string methods
s = "Tom"
print(f'Hello, My name is {s} and I am {age}')
s = f'Hello, My name is {s} and I am {age}'
print(len(s.upper()))
print(s.capitalize())
print(s.replace("Tom", "Jin")

# adjustment
"|{:<30}|".format("how are you?") #right adjustment
"|{:^30}|".format("how are you?") #center adjustment
"|{:>30}|".format("how are you?") #left adjustment

# Sample program to gather input and manipulate the input.

print("Please enter your name")
name = input()
print(f"you are {name}")
print("How old are you?")
age = int(input())
new_age = age + 1
print(f"you're {age} and you will be {new_age} next year")


x, y = input("Enter a two value: ").split()# default delimiter = " "
print("Number of boys: ", x) 
print("Number of girls: ", y) 


>>> 10 > 100
False
>>> 10 != 100
True
>>> 'str' == 'str'
True
>>> 'str' == 10
False
>>> (10 < 100) and (1 > 0)
True
>>> True and True
True
>>> False and True
False
>>> not (10 < 100)
False
>>> not (not (10 < 100))
True


>>> print(range(10))
range(0, 10)
>>> print(list(range(10)))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> print(list(range(0, 10, 2)))
[0, 2, 4, 6, 8]
>>> print(list(range(0, 10, 3)))
[0, 3, 6, 9]