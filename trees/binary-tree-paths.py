'''
Given a binary tree, return all root-to-leaf paths.

E.g.
Given the following tree
   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
'''

class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

def dfs(root):

  res = []
  stack = [(root, '')]

  while stack:
    node = stack.pop()
    currPath = node[1]
    node = node[0]

    if node:
      if node and not node.left and not node.right:
        res.append(currPath + str(node.val))

      stack.append((node.left, currPath + str(node.val) + '->'))
      stack.append((node.right, currPath + str(node.val) + '->'))

  return res

def binaryTreePaths(root):
  if not root:
    return [""]

  if not root.left and not root.right:
    return [str(root.val)]
  
  allPaths = dfs(root)

  return allPaths

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)

print(binaryTreePaths(root))