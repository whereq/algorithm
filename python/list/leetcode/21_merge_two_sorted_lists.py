import sys
import os

sys.path.append(os.getcwd())

from list.list_node import ListNode

class Solution:
  def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if l1 and l2:
        dummyHead = ListNode(None)
        current = dummyHead
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        current.next = l1 if l1 else l2
        return dummyHead.next
    return l1 or l2

  def mergeTwoLists_1(self, l1: ListNode, l2: ListNode) -> ListNode:
    if ((l1 or l2) is None):
      return None

    if (l1 is None):
      return l2
    
    if (l2 is None):
      return l1

    dummyNode = currentNode = ListNode(None)

    while (l1 and l2):
      if (l1.val <= l2.val):
        currentNode.next = l1
        currentNode = l1
        l1 = l1.next
      else:
        currentNode.next = l2
        currentNode = l2
        l2 = l2.next

    currentNode.next = l1 if l1 else l2
    return dummyNode.next

if __name__ == '__main__':
  list_1 = ListNode.buildSortedList(2)
  list_2 = ListNode.buildSortedList(3)

  ListNode.show(list_1)
  ListNode.show(list_2)

  solution = Solution()
  merged = solution.mergeTwoLists(list_1, list_2) 

  ListNode.show(merged)

  # list_1 = ListNode.buildEmptyList()
  # list_2 = ListNode.buildSortedList(1)

  # ListNode.show(list_1)
  # ListNode.show(list_2)

  # solution = Solution()
  # merged = solution.mergeTwoLists_1(list_1, list_2) 

  # ListNode.show(merged)

