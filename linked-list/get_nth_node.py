# Linked Lists - Get Nth

# Implement a GetNth() function that takes a linked list and an integer index and returns the node stored at the Nth index position. GetNth() uses the C numbering convention that the first node is index 0, the second is index 1, ... and so on. So for the list 42 -> 13 -> 666, GetNth() with index 1 should return Node(13);

# getNth(1 -> 2 -> 3 -> null, 0).data === 1
# getNth(1 -> 2 -> 3 -> null, 1).data === 2
# The index should be in the range [0..length-1]. If it is not, GetNth() should throw/raise an exception (ArgumentException in C#, InvalidArgumentException in PHP). You should also raise an exception (ArgumentException in C#, InvalidArgumentException in PHP) if the list is empty/null/None.

# test.it("tests for getting the Nth node in a linked list.")
# list = build_one_two_three()
# test.assert_equals(get_nth(list, 0).data, 1, "First node should be located at index 0.")
# test.assert_equals(get_nth(list, 1).data, 2, "Second node should be located at index 1.")
# test.assert_equals(get_nth(list, 2).data, 3, "Third node should be located at index 2.")
# test.expect_error("Invalid index value should throw error.", lambda : get_nth(list, 3))
# test.expect_error("Invalid index value should throw error.", lambda : get_nth(list, -1))
# test.expect_error("Invalid index value should throw error.", lambda : get_nth(list, 100))
# test.expect_error("None linked list should throw error.", lambda : get_nth(None, 0))

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def get_nth(node, index):
    if node is None: return node.next # throws error
    count = 0
    cur = node
    while cur:
        if count == index:
            return cur
        count += 1
        cur = cur.next
    cur.next          # throws error
