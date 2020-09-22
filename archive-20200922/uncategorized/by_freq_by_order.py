# Input: [8,2,4,2,1,7,8,7,2,2]
# Output: [2,2,2,2,8,8,7,7,4,1]

# 1) Sort by Frequency
# 2) Sort by Order: i.e. if two values have the same frequency, order must be retained.

# Declare a dictionary 
dict = {}
frequency = 1
input_list = [8,2,4,2,1,7,8,7,2,2]
placeholder_index = len(input_list) + 1

# add numbers to hashtable and count frequency 
# also get the index of their first occurence

# iterate over array
for index, value in enumerate(input_list):
  if not str(value) in dict:      # if value not in dictionary
    # add arr value as 'key' and frequency and index as 'value' in dictionary
    dict.update({str(value):[frequency,placeholder_index]})  
  if dict[str(value)][1] > index: # if index in dict is greater than current index
      dict[str(value)][1] = index   # replace it. This will store the first occurence 
  else:
    dict[str(value)][0] += 1  # if it exists, increment the frequency

# dict = sorted(dict.items(), key = lambda kv:(kv[1], kv[0]))

print("array to hashtable:")
print(dict)

# dictionary can't be sorted!! I think??

# i'll put the dict in a list

new_list = []

# iterate over dictionary
for key, value in dict.items():
  # add key and values as a list in a list
  new_list.append([int(key),value[0],value[1]])
print("hashtable to list:")
print(new_list)
from operator import itemgetter
# sort by each list by the values in their index 1 (which is the frequency)
new_list = sorted(new_list, key=itemgetter(1), reverse=True)

print("sort by first index (frequency) and order is kept the same:")
print(new_list)

solution_list = []

# iterate over new_list
for i in new_list: 
    # loop condition of each list depends on index 1 (which is the frequency)
    for j in range(i[1]):
      solution_list.append(i[0])  # add only index 0 (which is the value)

print(solution_list)
