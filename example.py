# l1 = ["b","o","l","m","v"]
# l2 = ["r", "e", "i", "o", "a"]
# l3 = ["m", "l", "t", "c", "p"]
# l4 = ["t", "a", "u", "i", "h"]
# l5 = ["s", "h", "r", "m", "k"]
# arr = []
# arr_e = []

# for i in range(len(l1)):
#   for j in range(len(l2)):
#     for k in range(len(l3)):
#       for l in range(len(l4)):
#         for m in range(len(l5)):
#           arr.append(l1[i] + l2[j] + l3[j] + l4[l] + l5[m])


# for i in range(len(arr)):
#   if "e" in arr[i]:
#     arr_e.append(arr[i])

# print(arr_e)


l1 = ["b","o","l","m","v"]
l2 = ["e"]
l3 = ["m", "l", "t", "c", "p"]
l4 = ["a"]
l5 = ["r"]
arr = []
arr_e = []

for i in range(len(l1)):
  for j in range(len(l2)):
    for k in range(len(l3)):
      for l in range(len(l4)):
        for m in range(len(l5)):
          arr.append(l1[i] + l2[j] + l3[j] + l4[l] + l5[m])

print(arr)