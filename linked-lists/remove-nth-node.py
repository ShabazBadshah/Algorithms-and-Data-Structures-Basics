class LinkedListNode:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next
  
  def __str__(self):
    return str(self.value) + "->" + str(self.next)


def remove_nth_node(head, n):
  
  if not head:
    return None

  list_length = 1
  pointer = head

  while pointer.next:
    list_length += 1
    pointer = pointer.next

  i = 1
  prev = head
  current = head
  temp = head

  while i < n:
    prev = prev.next
    current = current.next
    i += 1

  prev.next = current.next
  return temp

  

head = LinkedListNode(1)
n1 = LinkedListNode(2)
n2 = LinkedListNode(3)
n3 = LinkedListNode(4)
n4 = LinkedListNode(5)

head.next = n1
n1.next = n2
n2.next = n3
n3.next = n4

print (remove_nth_node(head, 3))