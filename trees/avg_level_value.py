import collections

class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

n4 = Node(5)
n3 = Node(3)
n2 = Node(1, n4)
n1 = Node(4, n3)
root = Node(2, n1, n2)

def averageOfLevels(root):
  """
  :type root: TreeNode
  :rtype: List[float]
  """

  if not root:
    return []

  avgValLevel = []

  if not root.left and not root.right:
    return [root.val]

  queue = collections.deque()
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

print (averageOfLevels(root))