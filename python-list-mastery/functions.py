# swap two positions of the elements
def swap_positions_with_multiple_assignment(num_list, pos1, pos2):
  pos1, pos2 = pos1 - 1, pos2 - 1
  num_list[pos1], num_list[pos2] = num_list[pos2], num_list[pos1]
  return num_list

def swap_positions_with_pop_and_insert(num_list, pos1, pos2):
  pos1, pos2 = pos1 - 1, pos2 - 1
  first_element = num_list.pop(pos1)
  second_element = num_list.pop(pos2 - 1)
  num_list.insert(pos1, second_element)
  num_list.insert(pos2, first_element)
  return num_list

def swap_positions_with_tuple_variable(num_list, pos1, pos2):
  pos1, pos2 = pos1 - 1, pos2 - 1
  get = num_list[pos1], num_list[pos2]
  num_list[pos2], num_list[pos1] = get
  return num_list
