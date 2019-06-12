# https://www.codewars.com/kata/57eba158e8ca2c8aba0002a0/train/pythons

def sort(arr):
  new_arr = []
  temp = "z"
  length = len(arr)
  length2 = len(arr)
  for n in range(0, length2):
    for i in range(0, length-1):
      print(i)
      str = arr[i]
      print(str)
      last_char = str[len(str)-1]
      if last_char < temp:
        temp = last_char
        if i == length - 1:
          new_arr.append(temp)
        arr.remove(arr[i])
        length -= 1
  print(new_arr)
    

sort(["bb","d", "cab","zba"])
