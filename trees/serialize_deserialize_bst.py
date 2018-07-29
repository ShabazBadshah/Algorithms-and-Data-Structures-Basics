from collections import deque
from level_order_array import levelOrderArray

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def serializeBst(root):
  """
  :type root: TreeTreeNode
  :rtype: str

  Given a binary tree serialize it while using the minimal amount
  of space

  e.g.
  
  Given the following tree

    3
   / \
  9  20
    /  \
   15   7

  The serialized representation of the tree above is the following
  3 9 20 # # 15 7
  """
 
  treeArr = []

  if not root:
    return '#'

  if not root.left and not root.right:
    return str(root.val) + "# #"

  queue = deque()
  queue.append(root)

  treeArr.append(root.val)

  while queue:
    size = len(queue)
    
    for _ in range(size):
      currTreeNode = queue.popleft()

      if currTreeNode.left:
        queue.append(currTreeNode.left)
        treeArr.append(currTreeNode.left.val)
      else:
        treeArr.append('#')
      if currTreeNode.right:
        queue.append(currTreeNode.right)
        treeArr.append(currTreeNode.right.val)
      else:
        treeArr.append('#')

  return ' '.join(map(str, treeArr))

def createNode(val):
  if val == '#':
    return None
  return TreeNode(int(val))

def deserializeBst(serializedBst):
  nodes = serializedBst.split(' ')

  if not nodes[0] or nodes[0] == '#':
    return None

  root = createNode(int(nodes[0]))

  i = 1
  queue = deque()
  queue.append(root)

  while queue:
    currNode = queue.popleft()
    if currNode:
      currNode.left = createNode(nodes[i])
      currNode.right = createNode(nodes[i + 1])
      queue.append(currNode.left)
      queue.append(currNode.right)
      i += 2
  return root

tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
serializedBst = serializeBst(tree)
print (serializedBst)

root = deserializeBst(serializedBst)
print(levelOrderArray(root))