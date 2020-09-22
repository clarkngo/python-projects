
def sort(arr):
  dict = {}
  frequency = 1

  # iterate over array
  for index, value in enumerate(arr):
    if not str(value) in dict:
      dict.update({str(value):[frequency,index]})   
    else:
      dict[str(value)][0] += 1

  new_list = []

  for key, value in dict.items():
    new_list.append([int(key),value[0],value[1]])

  from operator import itemgetter
  new_list = sorted(new_list, key=itemgetter(1), reverse=True)

  solution_list = []
  for i in new_list: 
      for j in range(i[1]):
        solution_list.append(i[0])
  return solution_list
