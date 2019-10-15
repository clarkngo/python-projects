list(range(100)) # lists with values from 0 to 99
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
# 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
# 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
# 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53,
# 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66,
# 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
# 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92,
# 93, 94, 95, 96, 97, 98, 99]

([1] + [0] * 10) # [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

A = [2,2]
A.remove(2)   # removes 1 instance of the value 2 in the list
A      # [2]

# A.remove(10)   # raises ValueError

A.append(1)   # add element at the end of the list
A      # [2, 1]

A.insert(0, 28) # insert element before the index
A      # [28, 2, 1]

A.insert(6, 100)  # if index > len(A), append.
A      # [28, 2, 1, 100]
A.insert(-4,15)   # if absolute value of index >= len(A), insert at index 0.
A      # [15, 28, 2, 1, 100]

# check if value is present in the list
# O(n) complexity
5 in A        # returns False
1 in A        # returns True

# copy
A = [15, 28, 2, 1, 100]
B = A
A = [1,5,6,7]

B       # [15, 28, 2, 1, 100]

# copy
A = [15, 28, 2, 1, 100]
D = list(A)
A = [1,5,6,7]
D       # [15, 28, 2, 1, 100]

import copy

# shallow copy
A = [1,5,6,7]
E = copy.copy(A)
A = [4,5]
E       # [1,5,6,7]

# deep copy
A = [1,5,6,7]
F = copy.deepcopy(A)
A = [4,5]
F       # [1,5,6,7]
