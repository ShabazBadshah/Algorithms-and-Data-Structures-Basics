# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    firstNum = self.getNumFromLL(l1)
    secondNum = self.getNumFromLL(l2)

    ans = str(firstNum + secondNum)
    print(ans)

    temp = ListNode(-1)
    currNode = temp

    for digit in reversed(ans):
      currNode.next = ListNode(digit)
      currNode = currNode.next

    return temp.next

  def getNumFromLL(self, l):
    curr_node = l
    numStr = ''

    while (curr_node != None):
      numStr = str(curr_node.val) + numStr
      curr_node = curr_node.next

    return int(numStr)

  