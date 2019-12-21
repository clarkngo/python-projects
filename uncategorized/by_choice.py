def sort(val: int) -> int:
  return val[1]

list1 = [(1,2), (3,3), (1,1)]

list1.sort(key=sort)

def reverse(arr: list) -> list:
  arr.sort(reverse=True)

print(list1)
reverse(list1)
print(list1)
