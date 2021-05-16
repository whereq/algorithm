class DoublyNode:
  def __init__(self, data: int, prev=DoublyNode, next=DoublyNode):
    self.data = data
    self.prev = prev 
    self.next = next 
