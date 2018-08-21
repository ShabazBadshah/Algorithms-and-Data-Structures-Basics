import heapq

class LLNode:
  def __init__(self, value):
    self.value = value
    self.next = None

  def __str__(self):
    return str(self.value) + "->" + str(self.next)

# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

def mergeKSortedLinkedList(lists):
  heap = []
  current = head = LLNode(None)

  for node in lists:
    heapq.heappush(heap, (node.value, node))

  while heap:
    minNode = heapq.heappop(heap)[1]
    current.next = minNode
    current = current.next

    if minNode.next:
      heapq.heappush(heap, (minNode.next.value, minNode.next))

  return head.next


l1 = LLNode(1)
l1.next = LLNode(21)
l2 = LLNode(24)
l2.next = LLNode(83)

print (mergeKSortedLinkedList([l1, l2]))