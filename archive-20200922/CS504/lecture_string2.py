# escape character
print('this is Jin's worksplace')
print("this is Jin's worksplace")
print('this is Jin\'s worksplace')

print('David said "hi"')
print("David said \"hi\"")
print("David said \t \"hi\"")
print("David said \n \"hi\"")
print("David said \a \"hi\"")
print("David said \v \v \"hi\"")

# multiple lines
print(''' Hi David
How are you?
Bye!''')
print('Hi David\How are you?\nBye!')


#buitin function
str = "$ 2145"
str.isalnum()
str[i].isnumeric()
str[i].isspace()


# Indexing and Slicing

>>> str = 'This is CityU'
>>> str[0]
'T'
>>> str[1:3]
'hi'
>>> str[1:]
'his is CityU'
>>> str[:3]
'Thi'
>>> str[:]
'This is CityU'

>>> str[-1]
'U'
>>> str[-2]
'y'
>>> len(str)
13

>>> 'T' in str
False
>>> 'K' in str
True

for i in str:
  print(i)

# Replacing a value

>>> str.replace('T', 'K')
'Khis is CityU'
>>> str.replace('T', 'K')
'Khis is CityU'
>>> str
'This is CityU'
>>> str = str.replace('T', 'K')
>>> str
'Khis is CityU'

'Khis is CityU'
>>> str[0] = 'T' # immutable


str1 = '      test  '
str1.lstrip() # removing white spaces before and after
str1.rstrip() # removing white spaces before and after
str1.strip() # removing white spaces before and after

str1.find('t')
str1.rfind('t')


# built in functions
>>> str.upper()
'KHIS IS CITYU'
>>> str.lower()
'khis is cityu'

# split() removes the character and split

>>> str = '''123
abc
&**
'''
>>> str
'123\nabc\n&**\n'
>>> str.split()
['123', 'abc', '&**']
>>> str.split('\n')
['123', 'abc', '&**', '']
>>> str.split('3')
['12', '\nabc\n&**\n']
>>> str.split('&')
['123\nabc\n', '**\n']

# printing justification

>>> str.rjust(20, '*')
'********123\nabc\n&**\n'
>>> str.ljust(20, '*')
'123\nabc\n&**\n********'
>>> str.cjust(20, '*')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'cjust'
>>> str.center(20, '*')
'****123\nabc\n&**\n****'




