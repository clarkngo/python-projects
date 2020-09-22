# empty dictionary
>>> d = {}
>>> d = {1: 'a', 2: 'b', 3: 'c'}
>>> d
{1: 'a', 2: 'b', 3: 'c'}
# create a dict (1)
>>> d = {'name': 'John', 1: [2,3,4]}
>>> d
{'name': 'John', 1: [2, 3, 4]}

# create a dict (2) using the dict() to create
>>> d = dict({1:'a', 2:'b', 3:'c'}) # {} ==> uses ":"
>>> d
{1: 'a', 2: 'b', 3: 'c'}

# create a dict (3) using the dict() to create
# each item as a pair <-- using a list
>>> d = dict([(1,'a'),(2,'b')]) # [] ==> uses ","
>>> d
{1: 'a', 2: 'b'}

# accessing a dictionary
>>> d = {'name': 'Jack', 'age': 35}
>>> d
{'name': 'Jack', 'age': 35}
>>> d['name']
'Jack'
>>> d['Jack']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Jack'
>>> d['age']
35
>>> d.get('age') #funciton ()
35
>>> d['age']      # direct access []

# modification of value by accessing 'key'
>>> d['age']
35
>>> d['age'] = 47
>>> d
{'name': 'Jack', 'age': 47}
>>> d['name'] = 'Jim'
>>> d
{'name': 'Jim', 'age': 47}

# adding a key value pair

>>> d
{'name': 'Jim', 'age': 47}
>>> d['address'] = 'Downtown'
>>> d
{'name': 'Jim', 'age': 47, 'address': 'Downtown'}
>>> d['job'] = 'Engineer'
>>> d
{'name': 'Jim', 'age': 47, 'address': 'Downtown', 'job': 'Engineer'}

# delete or remove the item by keys

>>> s = {1:1, 2:4, 3:9, 4:16, 5:25}
>>> s.pop(2)
4
>>> s
{1: 1, 3: 9, 4: 16, 5: 25}
>>> s.popitem()
(5, 25)
>>> del s[1]
>>> s
{3: 9, 4: 16}

# clear and delete the entire array

>>> s.clear()
>>> s
{}
>>> del s
>>> s
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 's' is not defined

 # display the keys/values of a dictionary
>>> d.keys()
dict_keys(['Jim', 'Tim', 'John', 'Kate'])
>>> d.values()
dict_values([1253, 9923, 4923, 2342])
>>> d.items()
dict_items([('Jim', 1253), ('Tim', 9923), ('John', 4923), ('Kate', 2342)])
>>> list(d.items())
[('Jim', 1253), ('Tim', 9923), ('John', 4923), ('Kate', 2342)]

# Key or value exist in a dictionary
>>> d = {'Jim': 1253, 'Tim': 9923, 'John': 4923, 'Jake': 2342}
# d --> by default, it looks at the keys
>>> 'Jim' in d
True

>>> 1253 in d.values()
True
>>> 1253 in d.keys()
False
>>> 'Jim' in d.keys()
True
>>> 'Kate' in d.keys()
False
>>> 'Kate' not in d.keys()
True

# setdefault, use the value if key doesn't exist, return the value if key exists
>>> d.setdefault('Tom', 0)
9211
>>> d
{'Jim': 1253, 'Tim': 9923, 'John': 4923, 'Kate': 2342, 'Tom': 9211}
>>> d.setdefault('Jim', 9211) # Jim exists so it returns Jim's value from dictionary
1253
>>> d
{'Jim': 1253, 'Tim': 9923, 'John': 4923, 'Kate': 2342, 'Tom': 9211}

# merging two dicts
>>> d1 = {'a': 10, 'b': 8, 'd': 6, 'e': 11}
>>> d2 = {'d': 6, 'e': 11}
>>> d1.update(d2) # d1 + d2

>>> d1 = {'a': 10, 'b': 8}
>>> d3 = {**d1, **d2}
>>> d3
{'a': 10, 'b': 8, 'd': 6, 'e': 11}

# other methods
>>> len(d1)
2
>>> type(d1)
<class 'dict'>
>>> d4 = d1.copy() # shallow copy
>>> d4
{'a': 10, 'b': 8}
>>> d5 = d1
>>> d5
{'a': 10, 'b': 8}
>>> d4
{'a': 10, 'b': 8}
>>> d1
{'a': 10, 'b': 8}
>>> d4.clear()
>>> d1
{'a': 10, 'b': 8}
>>> d4
{}
>>> del d4

# sorting (dict -> sorted list, per key, per value)
>>> d3
{'a': 10, 'b': 8, 'd': 6, 'e': 11}
>>> sorted(d3.keys())
['a', 'b', 'd', 'e']
>>> sorted(d3.values())
[6, 8, 10, 11]
>>> sorted(d3.items()) #sort by key and display all items
[('a', 10), ('b', 8), ('d', 6), ('e', 11)]

# nested dictionary
>>> ppl = {1: {'name': 'John', 'age':'27', 'sex':'Male'}, 2: {'name': 'Dave', 'age': '30', 'sex':'Male'}}
>>> ppl
{1: {'name': 'John', 'age': '27', 'sex': 'Male'}, 2: {'name': 'Dave', 'age': '30', 'sex': 'Male'}}
>>> ppl.get(1)
{'name': 'John', 'age': '27', 'sex': 'Male'}
>>> ppl.get(2)
{'name': 'Dave', 'age': '30', 'sex': 'Male'}
>>> ppl.get(2).get('name')
'Dave'
>>> ppl[1]['name']
'John'
>>> ppl[3] = {}
>>> ppl[3]['name'] = 'Linda'
>>> ppl[3]['age'] = '22'
>>> ppl[3]['sex'] = 'Female'
>>> ppl
{1: {'name': 'John', 'age': '27', 'sex': 'Male'}, 2: {'name': 'Dave', 'age': '30', 'sex': 'Male'},
3: {'name': 'Linda', 'age': '22', 'sex': 'Female'}}

>>> ppl[1]['married'] = 'No' # additional key value pair between sub-dicts

del ppl[1] # to remove the sub dict.

people = {1: {'Name': 'John', 'Age': '27', 'Gender': 'Male'},
          2: {'Name': 'Marie', 'Age': '22', 'Gender': 'Female'}}

for id, info in people.items():
      print("\nPerson ID:", id)

      for key in info:
            print(key + ': ', info[key])



