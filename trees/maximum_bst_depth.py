from collections import deque

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def maximumTreeDepth(root):
  """
  :type root: TreeTreeNode
  :rtype: int

  Given a binary tree find its maximum depth

  Notes: A single node tree (i.e. just a root node) has a depth of 1

  e.g.
  
  Given the following tree

    3
   / \
  9  20
    /  \
   15   7

  The maximum depth is 3
  """
  
  currDepth = 0

  if not root: 
    return 0

  if not root.left and not root.right:
    return 1

  queue = deque()
  queue.append(root)

  while queue:
    amtNodesOnCurrLevel = len(queue)

    for _ in range(amtNodesOnCurrLevel):
      currNode = queue.popleft()
      if currNode.left:
        queue.append(currNode.left)

      if currNode.right:
        queue.append(currNode.right)

    currDepth += 1

  return currDepth

tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print (maximumTreeDepth(tree)) # 3