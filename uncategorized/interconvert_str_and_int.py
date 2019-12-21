# def to_int(str):
#   return int(str)

import sys
def to_int(str):
  if str == '' or str == None:
    return -1
  digit = 0
  result = 0
  isNegative = False
  for elem in str:
    if elem == '-':
      isNegative = True
      continue
    digit = ord(elem) - ord('0')
    result = result * 10 + digit
  if isNegative == True:
    result *= - 1
  if result > sys.maxsize:
    return -1
  return result

def to_str(num):
  if type(num) == float or num == None:
    return "not valid"    
  my_str = ''
  digit = 0
  isNegative = False
  if num < 0:
    isNegative = True
    num *= - 1
  while num > 1:
    digit = int(num % 10)
    my_str = str(digit) + my_str
    num /= 10
  if isNegative == True:
    my_str = "-" + my_str
  return my_str

# print(to_str(123))
# print(to_int("-123"))
