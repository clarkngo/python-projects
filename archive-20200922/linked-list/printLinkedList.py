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
