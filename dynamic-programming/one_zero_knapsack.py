# 0/1 Knapsack Problem Dynamic Programming
# Given the total weight of the knapsack,
# Return the list of items that would maximize the weight with the most value

# Given:
# items: [1,1],[3,4],[4,5],[5,7]
# weight: 7
#
#       items
#   weight | value
#        1 | 1
#        3 | 4
#        4 | 5
#        5 | 7
#
# Output: []

from typing import List
def knapsack(items: List, weight: int) -> List:
  table = []

  # add first item to the table
  for i in range(1):
    table.append([])
    for j in range(weight+1):
      if items[i][0] <= j:
        table[i].append(items[i][1])
      else:
        table[i].append(0)

  # add second to the last item in table
  for i in range(1, len(items)):
    # if item weight == table weight, we add 0
    table.append([0])
    for j in range(1,weight+1):
      # if item weight is greater than current table weight (column) [j]
      # add item (in the table) weight of previous row [i-1] of the same column [j]
      if items[i][0] > j:
        table[i].append(table[i-1][j])
      else: # if item weight is equal or less than current table weight (column)
        # add item of greater value:
        #   current item value + item (in the table) value of previous row [i-1] of with remaining weight available
        #   remaining weight available: current table weight [j] - current item weight [items[i][0]]
        # OR:
        #   item (in the table) weight of previous row [i-1] of the same column [j]
        table[i].append(max(items[i][1] + table[i-1][j-items[i][0]], table[i-1][j]))

  # print(table)

  total_val = table[-1][-1]
  row = len(table) - 1
  column = len(table[i]) - 1
  items_obtained = []

  while total_val != 0:
    # check if value exist in previous row at same column
    if table[row][column] == table[row-1][column]:
      row -= 1  # move row pointer to previous row
    # if value does NOT exist in previous row at same column
    else:
      items_obtained.append(items[row])
      column -= items[row][0] # move column pointer to current column - item weight
      total_val -= items[row][1]  # reduce total value with item value
  return items_obtained

# items = [[weight, value], [weight, value]]
k = knapsack([[1,1],[3,4],[4,5],[5,7]], 7)
# print(k)
