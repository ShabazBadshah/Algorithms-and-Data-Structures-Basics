from collections import deque

class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def averageOfLevels(root):
  """
  :type root: TreeNode
  :rtype: List[float]

  Given a binary tree, returns the average value of 
  all the nodes on each level

  e.g.
  
  Given the following tree

    3
   / \
  9  20
    /  \
   15   7

  The list of floats to be returned will be the following
  [3, 14.5, 11]
  """

  if not root:
    return []

  avgValLevel = []

  if not root.left and not root.right:
    return [root.val]

  queue = deque()
  queue.append(root)

  while queue:
    currLevelSum = 0
    currLevelCount = len(queue)

    for i in range(currLevelCount):
      current = queue.popleft()
      currLevelSum += current.val
      if current.left:
        queue.append(current.left)
      if current.right:
        queue.append(current.right)

    if currLevelCount != 0:
      avgValLevel.append(currLevelSum / currLevelCount)

  return avgValLevel

n4 = Node(5)
n3 = Node(3)
n2 = Node(1, n4)
n1 = Node(4, n3)
root = Node(2, n1, n2)

print (averageOfLevels(root))