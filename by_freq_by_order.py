# Input: [8,2,4,2,1,7,8,7,2,2]
# Output: [2,2,2,2,8,8,7,7,4,1]

# 1) Sort by Frequency
# 2) Sort by Order: i.e. if two values have the same frequency, order must be retained.

# Declare a dictionary 
dict = {}
frequency = 1
arr = [8,2,4,2,1,7,8,7,2,2]
placeholder_index = len(arr)

# add numbers to hashtable and count frequency 
# also get the index of their first occurence
for index, value in enumerate(arr):
  if not str(value) in dict:
    dict.update({str(value):[frequency,placeholder_index]})
  if dict[str(value)][1] > index:
      dict[str(value)][1] = index    
  else:
    dict[str(value)][0] += 1

# dict = sorted(dict.items(), key = lambda kv:(kv[1], kv[0]))

print("array to hashtable:")
print(dict)

# dictionary can't be sorted!!

# i'll put the dict in a list

list = []
for key, value in dict.items():
  list.append([int(key),value[0],value[1]])
print("hashtable to list:")
print(list)
from operator import itemgetter
list = sorted(list, key=itemgetter(1), reverse=True)

print("sort by first index (frequency) and order is kept the same:")
print(list)

solution_arr = []

for i in list: 
    for j in range(i[1]):
      solution_arr.append(i[0])

print(solution_arr)
