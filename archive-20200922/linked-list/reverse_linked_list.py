# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        nodeVals = []
        while cur:
            nodeVals.append(cur.val)
            cur = cur.next
            head = ListNode(nodeVals[-1])
        cur = head
        for val in nodeVals[len(nodeVals)-2::-1]:
            cur.next =  ListNode(val)
            cur = cur.next
            cur.next = None
        return head

# Runtime: 32 ms, faster than 94.86% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Reverse Linked List.
    def reverseList2(self, head: ListNode) -> ListNode:
        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev

    def reverseList3(self, head, prev=None):
        if not head:
            return prev

        curr, head.next = head.next, prev
        return self.reverseList3(curr, head)


    def reverseList4(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev_node = None
        curr_node = head
        while curr_node:
            next_node = curr_node.next # Remember next node
            curr_node.next = prev_node  # REVERSE! None, first time round.
            prev_node = curr_node  # Used in the next iteration.
            curr_node = next_node  # Move to next node.
        head = prev_node
        return head

    def printLinkedList(self, head: ListNode) -> None:
        strng = ""
        cur = head
        strng += str(cur.val)
        if (head.next == None):
            print(strng)
            return
        cur = cur.next
        while cur.next != None:
            strng += "->" + str(cur.val)
            cur = cur.next
            strng += "->" + str(cur.val)
        print(strng)


one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)
one.next = two
two.next = three
three.next = four
four.next = five

a = Solution()
a.printLinkedList(one)
# a.printLinkedList(a.reverseList(one))
# a.printLinkedList(a.reverseList2(one))
a.printLinkedList(a.reverseList3(one))
