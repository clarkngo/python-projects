# brute force

def rotate_right(arr):
  arr[0][2], arr[0][0] = arr[0][0], arr[0][2]
  arr[1][2], arr[0][1] = arr[0][1], arr[1][2]
  arr[2][2], arr[0][0] = arr[0][0], arr[2][2]
  arr[0][1], arr[1][0] = arr[1][0], arr[0][1]
  arr[2][1], arr[1][0] = arr[1][0], arr[2][1]
  arr[0][0], arr[2][0] = arr[2][0], arr[0][0]
  return arr

input_arr = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate_right(input_arr))

# expected output [[7,4,1],[8,5,2],[9,6,3]]