from collections import deque

class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def levelOrderArray(root):
  """
  :type root: TreeNode
  :rtype: List[float]

  Given a binary tree, returns the array representation
  of the tree where each sub-array is a level; and the 
  the contents of each sub-array are the value of the 
  nodes on that level

  e.g.
  
  Given the following tree

    3
   / \
  9  20
    /  \
   15   7

  The array representation that will be returned will be
  [[3], [9, 20], [15, 7]]
  """

  treeArr = []
        
  if not root:
    return treeArr

  if not root.left and not root.right:
    return [[root.val]]

  queue = deque()
  queue.append(root)

  while queue:
    currLevelNodes = []
    size = len(queue)
    
    for i in range(size):
      currNode = queue.popleft()
      currLevelNodes.append(currNode.val)
    
      if currNode.left:
        queue.append(currNode.left)
      if currNode.right:
        queue.append(currNode.right)

    treeArr.append(currLevelNodes)
      
  return treeArr

tree = Node(3, Node(9), Node(20, Node(15), Node(7)))
print (levelOrderArray(tree)) # [[3], [9, 20], [15, 7]]