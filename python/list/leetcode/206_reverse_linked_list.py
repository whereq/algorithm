import sys
import os

sys.path.append(os.getcwd())


from list.singly_node import SinglyNode

def initSinglyList(length: int) -> SinglyNode:
  head = SinglyNode(0, None)
  current = head

  i = 0
  while (i < length):
    i = i + 1
    temp = SinglyNode(i, None)
    current.next = temp
    current = temp

  return head


def show(head: SinglyNode):
  if head is None:
    return
    
  i = 0
  while (head.next is not None):
    print ("#%d is %d"%(i, head.data))
    head = head.next
    i = i + 1

def reverse(head: SinglyNode) -> SinglyNode:
  prev, curr = None, head

  while (curr is not None):
    prev, prev.next, curr = curr, prev, curr.next

  head = prev
  return head

def test():
  head = initSinglyList(5)

  print("original list")
  show(head)

  print("reversed list")
  head = reverse(head)
  show(head)

if __name__ == "__main__":
  test()

