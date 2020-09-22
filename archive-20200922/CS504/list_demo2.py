>>> a = []
>>> a = [1,2,3]
>>> a = [3, 'cat', 'dog', 0.24]
>>> a
[3, 'cat', 'dog', 0.24]

# nested
>>> b = [a, '*']
>>> b
[[3, 'cat', 'dog', 0.24], '*']

# operations
a.append(b)
a.extend(b)
a + b


[[3, 'cat', 'dog', 0.24], '*']
>>> b[0][2]
'dog'
>>> b[1][0]
'*'
>>> b[1][2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> len(b[1])
1
>>> len(b[0])
4
>>> a
[3, 'cat', 'dog', 0.24]
>>> a[1:3]
['cat', 'dog']
>>> a[:3]
[3, 'cat', 'dog']

>>> a
[1, 3, 9, 2, 'cat', 'dog', 0.24, 'eight', 100, 'a', 'b', 'c']
>>> a[3:] # 3rd to end
[2, 'cat', 'dog', 0.24, 'eight', 100, 'a', 'b', 'c']
>>> a[:3] # first to 3rd
[1, 3, 9]

# replacing existing list items
>>> a[0] = 'my'
>>> a
['my', 3, 9, 2, 'cat', 'dog', 0.24, 'eight', 100, 'a', 'b', 'c']
>>> a[1:4]
[3, 9, 2]
>>> a[1:4] = ['cat', 'bird', 'dog']
>>> a
['my', 'cat', 'bird', 'dog', 'cat', 'dog', 0.24, 'eight', 100, 'a', 'b', 'c']

#inserting an items
>> a.insert(0, 'your')
>>> a
['your', 'my', 'cat', 'bird', 'dog', 'cat', 'dog', 0.24, 'eight', 100, 'a', 'b', 'c']
>>> a.insert(12, 'your')
>>> a
['your', 'my', 'cat', 'bird', 'dog', 'cat', 'dog', 0.24, 'eight', 100, 'a', 'b', 'your', 'c']

#removing an item that is known.
>>> a
['your', 'my', 'cat', 'bird', 'dog', 'cat', 'dog', 0.24, 'eight', 100, 'a', 'b', 'your', 'c']
>>> a.remove('my')
>>> a
['your', 'cat', 'bird', 'dog', 'cat', 'dog', 0.24, 'eight', 100, 'a', 'b', 'your', 'c']
>>> a.remove('your')
>>> a
['cat', 'bird', 'dog', 'cat', 'dog', 0.24, 'eight', 100, 'a', 'b', 'your', 'c']
>>> a.remove('your')
>>> a
['cat', 'bird', 'dog', 'cat', 'dog', 0.24, 'eight', 100, 'a', 'b', 'c']
>>> a.remove('your')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list

#removing an item based on index location
>>> del a[1]
>>> a
['cat', 'dog', 'cat', 'dog', 0.24, 'eight', 100, 'a', 'b', 'c']

>>> del a[:3]
>>> a
['dog', 0.24, 'eight', 100, 'a', 'b', 'c']

# sorting a list, reverse

num=[3,2,1]
num.sort()
num
[1, 2, 3]
num.reverse()

#pop
>>> a
['dog', 0.24, 'eight', 100, 'a', 'b', 'c']
>>> a.index('dog')
0
>>> a.pop(2)
'eight'

# index
>>> a
['dog', 0.24, 100, 'a', 'b', 'c']
>>> a.index('dog')
0

'''
# Challenge: can you print all the items in the list?

b = [2, 3, 10, 'shoes', 'dress', 'bag', 0.114]
for i in range(len(b)):
    print("item at " + str(i) + " is " + str(b[i]))
'''

#immutable (string)
>>> str1 = "Hello CityU"
>>> str1[0]
'H'
for i in str1:
      #print('* ' + i ' *')
      #print(i, end=' ') # instead of \n


# TUPLE demo
>>> tuple1 = ()
>>> tuple1
()
>>> tuple1 = (1,3,5)
>>> tuple1 = (1,"hello",5)
>>> tuple1
(1, 'hello', 5)
>>> tuple1[0]
1
>>> a = [1,2,3,4]
>>> b = ['a', 'b', 'c']
>>> tuple1 = (a, b, 'name')
>>> tuple1
([1, 2, 3, 4], ['a', 'b', 'c'], 'name')

# TUPLE with nested list which can be modified
>>> tuple1[0]
[1, 2, 3, 4]
>>> tuple1[0][2]
3
>>> tuple1[0][2] = -999
>>> tuple1
([1, 2, -999, 4], ['a', 'b', 'c'], 'name')
>>> tuple1[2]
'name'
>>> tuple1[2] = 'Jin'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment

# TUPLE packing
>>> tuple1 = ()
>>> tuple1 = 1, 3, "dog"
>>> tuple1
(1, 3, 'dog')
>>> a, b, c = tuple1
>>> a
1
>>> b
3
>>> c
'dog'

# LIST <--> TUPLE

>>> type(tuple1)
<class 'tuple'>
>>> list1 = [1,2,34]
>>> type(list1)
<class 'list'>
>>> list(tuple1)
[1, 3, 'dog']
>>> tuple1 = list(tuple1)
>>> tuple1
[1, 3, 'dog']
>>> type(tuple1)
<class 'list'>

# LIST REFERENCE (address)
# but when you reassign the value, it doesn't change
# only for the value modification

>>> list1
[1, 2, 34]
>>> list2 = ['h', 'i', 'j']
>>> list1
[1, 2, 34]
>>> list2
['h', 'i', 'j']
>>> list1 = list2
>>> list1
['h', 'i', 'j']
>>> list2
['h', 'i', 'j']
>>> list1 == list2
True
>>> list1[0] = 1
>>> list1
[1, 'i', 'j']
>>> list2
[1, 'i', 'j']

# If you have to change the values in tuple, reassign the values
>>> list1[0] = 1
>>> list1
[1, 'i', 'j']
>>> list2
[1, 'i', 'j']
>>> tuple1 = list1
>>> tuple1
[1, 'i', 'j']
>>> tuple1 = (1,2,3)
>>> tuple1
(1, 2, 3)
>>> tuple2 = tuple1
>>> type(tuple1)
<class 'tuple'>
>>> type(tuple2)
<class 'tuple'>
>>> tuple1
(1, 2, 3)
>>> tuple2
(1, 2, 3)
>>> tuple2 = list1
>>> tuple2
[1, 'i', 'j']
>>> tuple1
(1, 2, 3)
>>> list1
[1, 'i', 'j']
>>> list2
[1, 'i', 'j']
>>> list2 = tuple1
>>> list2
(1, 2, 3)
>>> list1
[1, 'i', 'j']
>>> tuple1
(1, 2, 3)
>>> tuple2
[1, 'i', 'j']
>>> tuple2 = tuple1
>>> tuple1
(1, 2, 3)
>>> tuple1[0]=0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> tuple1 = ([1,2,3], 0, 'hi')
>>> tuple2
(1, 2, 3)
>>> tuple1
([1, 2, 3], 0, 'hi')


for i in range(len(t1)):
    print(i)

for i in t1:
     print(i)




import copy
a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]
d = c

print(id(c) == id(d))          # True - d is the same object as c
print(id(c[0]) == id(d[0]))    # True - d[0] is the same object as c[0]

d = copy.copy(c)
print(id(c) == id(d))          # False - d is now a new object
print(id(c[0]) == id(d[0]))    # True - d[0] is the same object as c[0]

d = copy.deepcopy(c)
print(id(c) == id(d))          # False - d is now a new object
print(id(c[0]) == id(d[0]))    # False - d[0] is now a new object


