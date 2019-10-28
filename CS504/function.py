''' DEFINITION
def function1():
    name = "Harry"
    print("Hello, ", name, "! Good morning!")

def function2():
    name = "Sally"
    print("Hello, ", name, "! Good morning!")

function1()
function2()
'''

''' This function greets to everyone!'''
'''
 def greeting (name):
     print("Hello, " + name + "! Good morning!")

print("What is your name? ")
name = input()
greeting(name)
'''
''' 
def greeting2 (greet_name):
    greet_name = "Hello, " + name + "! Good morning!"
    return greet_name

print("What is your name? ")
greet_name = input() # greeting2 uses both local "greet_name" + global "name"
name = input() # global "name" has been updated
'''
'''
def greeting2 (name):
    name = "Hello, " + name + "! Good morning!"
    return name

print("What is your name? ")
name = input()
print(greeting2(name))
'''


name = "Harry" # this is a global variable
def name_change():
    #    global name    accessing the global var
    name = "Sally"
    print("inside name_change(): ", name) # Sally (from local)

name_change()
print("outside name_change(): ", name) # Harry (from global)


''' nonlocal (not global, nor local, super-local works within nested blocks)'''
'''
def function1():
    name = "Harry"
    def function2():
        # nonlocal name (follow the block)
        name = "Sally"
        print("Function2: ", name)
    function2()
    print("Function1:", name)
function1()
'''
'''
x = 'global x'
def foo():
    # y = 'local y'
    # global x
    x = 'local x'
    print (x)
foo()
print(x)
'''

'''
def test(z):
    x = 'local x'
    print(z)

test('local z') # try z out of scope
'''
''' built-in (min vs min(list))
# import builtins
# print(dir(builtins))

def my_min():
    pass

m = min([5, 2, 1, 3])
print (m)
'''
'''
def outer():
    x = 'outer x'
    def inner():
        #nonlocal x # only available in the nest function blocks
        x = 'inner x' 
        print(x)
    inner()
    print(x)
outer()    
'''

''' (summary)
x = 'global x'
def outer():
    x = 'outer x'
    def inner():
        x = 'inner x' 
        print(x)
    inner()
    print(x)
outer()    
print(x)
'''




''' Arguments '''

''' This function greets to everyone! '''
'''
def greeting (name):
   print("Hello, " + name + "! Good morning!")

print("What is your name? ")
name = input()
greeting(name)

def greeting3 (name, msg):
   print("Hello, " + name + "! " + msg)
'''

''' std IO
print("What is your name? ")
name = input()
print("Enter the greeting message ")
msg = input()
greeting3(name, msg) # try without msg and explain the error message
'''


def greeting3 (name, msg = "Good Morning!"): # default argument
   print("Hello, " + name + "! " + msg)

print("What is your name? ")
name = input()
print("Enter the greeting message ")
msg = input()
if len(msg) == 0:
    greeting3(name)
else:
    greeting3(name, msg) 


''' print the list of names 

def greeting3 (*names): # receive those parameters in a form of list
    for name in names:
        print("Hello ", name)
'''
''' std IO
greeting3("David", "John", "Jin-")
greeting3("David", "John-")
greeting3("David-")
'''

''' Exception handling 
def division(divisor):
    return 100/divisor
'''
def division(divisor):
    try:
        return 100/divisor
    except ZeroDivisionError:
        print('Error: Invalid Argument.')
        # return -1

print(division(10))
print(division(0)) 
print(division(50))

