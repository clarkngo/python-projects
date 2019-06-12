
# list_indices = [2,3,4]
# for i in range(0, len(list_indices) - 1):
#   print(i)
#   if (list_indices[i] + list_indices[i+1] == 6):
#       list_indices.append(i + 1)
#       list_indices.append(i + 2)
#       print(list_indices)
      
# solution
x =210
def reverse(x):
  solution = 0
  isNegative = False
  digit = 0
  if (x < 0):
      x *= - 1
      isNegative = True
  while (x % 10 == 0):
      x //= 10
  while (x > 0):
      digit = x % 10
      solution = digit + solution * 10
      x //= 10
  if (isNegative):
      solution *= -1
  return solution  
  