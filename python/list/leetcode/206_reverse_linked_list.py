import sys
import os

sys.path.append(os.getcwd())


from list.list_node import ListNode

def initSinglyList(length: int) -> ListNode:
  head = ListNode(0, None)
  current = head

  i = 0
  while (i < length):
    i = i + 1
    temp = ListNode(i, None)
    current.next = temp
    current = temp

  return head


def show(head: ListNode):
  if head is None:
    return
    
  i = 0
  while (head.next is not None):
    print ("#%d is %d"%(i, head.val))
    head = head.next
    i = i + 1

"""
Runtime: 24 ms, faster than 99.17% of Python3 online submissions for Reverse Linked List.
Memory Usage: 15.7 MB, less than 42.36% of Python3 online submissions for Reverse Linked List.
"""
def reverseSingle(head: ListNode) -> ListNode:
  prev, curr, next = None, head, None

  while (curr is not None):
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next
  
  return prev 

"""
Runtime: 36 ms, faster than 61.62% of Python3 online submissions for Reverse Linked List.
Memory Usage: 15.7 MB, less than 42.36% of Python3 online submissions for Reverse Linked List.
"""
def reverseTuple(head: ListNode) -> ListNode:
  prev, curr = None, head

  while (curr is not None):
    prev, prev.next, curr = curr, prev, curr.next

  return prev 

def test():
  head = initSinglyList(5)

  print("original list")
  show(head)

  print("reversed list by single assignment")
  show(reverseSingle(head))

  head = initSinglyList(5)
  print("reversed list by tuple assignment")
  show(reverseTuple(head))

if __name__ == "__main__":
  test()

