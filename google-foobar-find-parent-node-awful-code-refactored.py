class Node: 
	def __init__(self, data): 
		self.data = data 
		self.left = self.right = None
# Function to insert nodes in level order 
def insert_level_order(arr, root, i, n): 
	# Base case for recursion 
	if i < n: 
		temp = Node(arr[i]) 
		root = temp 
		# insert left child 
		root.left = insert_level_order(arr, root.left, 
									2 * i + 1, n) 
		# insert right child 
		root.right = insert_level_order(arr, root.right, 
									2 * i + 2, n) 
	return root 
# Function to insert nodes in level order 

def insert_post_order(arr, root, i, n): 
	# Base case for recursion 
	if i < n: 
		temp = Node(arr[i]) 
		root = temp 
		# insert left child 
		root.left = insert_post_order(arr, root.left, 
									2 * i + 1, n) 
		# insert right child 
		root.right = insert_post_order(arr, root.right, 
									2 * i + 2, n) 
	return root 

def postorderTraversal(root, lst):
    return _helper(root, lst)
def _helper(start, traversal):
    if start:
        if start.data == 0:
          _helper(start.left, traversal)
          _helper(start.right, traversal)
          start.data = traversal.pop()

def list_postorderTraversal(root):
    lst = []
    return _helper_list(root, lst)
def _helper_list(start, traversal):
    if start:
        traversal.append(start.data)
        traversal = _helper_list(start.left, traversal)
        traversal = _helper_list(start.right, traversal)
    return traversal

def flatten( parent): 
  
    # Queue to store nodes 
    # for BFS 
    q = [] 
    q.append(parent.left) 
    q.append(parent.right) 
    prev = parent 
  
    # Code for BFS 
    while (len(q) > 0) : 
          
        # Size of queue 
        s = len(q) 
        while (s > 0) : 
            s = s - 1
              
            # Front most node in 
            # the queue 
            curr = q[0] 
            q.pop(0) 
  
            # Base case 
            if (curr == None): 
                continue
            prev.right = curr 
            prev.left = None
            prev = curr 
  
            # appending elements 
            # in queue 
            q.append(curr.left) 
            q.append(curr.right) 
          
    prev.left = None
    prev.right = None
  
# Function to print flattened 
# Binary Tree 
# Function to print flattened 
# Binary Tree 
def to_list(parent): 
    lst = []
    curr = parent 
    while (curr != None): 
        lst.append(curr.data)
        curr = curr.right 
    return lst


def solution(h, q):

  n = pow(2, h)-1
  arr = [0 for i in range(n)]
  n = len(arr) 
  root = None
  root = insert_level_order(arr, root, 0, n) 
  lst = [i for i in range(n,0,-1)]
  postorderTraversal(root,lst)
  flatten(root)
  res_lst = to_list(root)
  res_lst.insert(0,0)
  print(res_lst)
  ans_lst = []
  test_lst = q
  for i in range(len(test_lst)):
    n = 0
    for j in range(len(res_lst)):
      if test_lst[i] == res_lst[j]:
        if j % 2 == 1:
          n = (j-1) // 2
          if n == 0:
            ans_lst.append(-1)
          else:
            ans_lst.append(res_lst[n])
        else:
          n = j // 2
          if n == 0:
            ans_lst.append(-1)
          else:
            ans_lst.append(res_lst[n])
  return ans_lst

print(solution(3, [7,3,5,1]))
