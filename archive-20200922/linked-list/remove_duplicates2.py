# Source: https://www.codewars.com/kata/linked-lists-remove-duplicates/train/python

# Linked Lists - Remove Duplicates

# Write a RemoveDuplicates() function which takes a list sorted in increasing order and deletes any duplicate nodes from the list. Ideally, the list should only be traversed once. The head of the resulting list should be returned.

# var list = 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5 -> null
# removeDuplicates(list) === 1 -> 2 -> 3 -> 4 -> 5 -> null

# test.it("should be able to handle an empty list.")
# test.assert_equals(remove_duplicates(None), None, "removing duplicates from None should return None.")

# test.it("should be able to handle a list of length 1.")
# test.assert_equals(remove_duplicates(Node(23)).data, 23, "removing duplicates from linked list consisting of one node should return the node.")

# test.it("should be able to handle a list without duplicates.")
# assert_linked_list_equals(remove_duplicates(build_one_two_three()), build_one_two_three(), "removing duplicates from a linked list without duplicates node should return the list.")
# assert_linked_list_equals(remove_duplicates(build_one_two_three_four_five_six()), build_one_two_three_four_five_six(), "removing duplicates from linked list without duplicates node should return the list.")

# test.it("should be able to handle a list with duplicates.")
# assert_linked_list_equals(remove_duplicates(build_list([1, 2, 2])), build_list([1, 2]), "should remove the duplicate '2' entries")
# assert_linked_list_equals(remove_duplicates(build_list([1, 1, 1, 1, 1])), build_list([1]), "should remove the duplicate '1' entries")
# assert_linked_list_equals(remove_duplicates(build_list([1, 2, 3, 3, 4, 4, 5])), build_list([1, 2, 3, 4, 5]), "should remove the duplicate '3' and '4' entries")
# assert_linked_list_equals(remove_duplicates(build_list([1, 1, 1, 1, 2, 2, 2, 2])), build_list([1, 2]), "should remove the duplicate '1' and '2' entries")

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if None: return None
    if head is None: return head
    cur = head
    while cur.next != None:
        if cur.data == cur.next.data:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head
