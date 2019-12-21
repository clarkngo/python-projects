# Source: https://www.programiz.com/python-programming/methods/built-in/print

# print() syntax

# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# objects - object to the printed. * indicates that there may be more than one object
# sep - objects are separated by sep. Default value: ' '
# end - end is printed at last
# file - must be an object with write(string) method. If omitted it, sys.stdout will be used which prints objects on the screen.
# flush - If True, the stream is forcibly flushed. Default value: False

# # One string is passed
# print('Hello, World!')

# # Two strings are passed
# print('Hello, World!', 'again!')

# a = 5
# # Two objects are passed
# print('a =', a)

# b = a
# # Three objects are passed
# print('a =', a, '= b')

# # print() with separator and end parameters
# a = 5
# print("a =", a, sep='00000', end='\n\n\n')
# print("a =", a, sep='0', end='')

# # ends the output with a <space>  
# print("Welcome to" , end = ' ')  
# print("GeeksforGeeks", end = ' ') 


# This program tries to open the python.txt in writing mode. 
# If this file doesn't exist, python.txt file is created and opened in writing mode.

sourceFile = open('python.txt', 'w')
print('Pretty cool, huh!', file = sourceFile)
sourceFile.close()

import sys
print(sys.maxsize)
