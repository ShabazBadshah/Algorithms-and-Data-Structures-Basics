class Node:
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

  def __str__(self):
    if self.data:
      return str(self.data) + " " + str(self.left) + " " + str(self.right)

'''
Invert a binary tree.

Algorithm runs in O(n) time

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''
def invertBinaryTree(root):
  if root:
    root.left, root.right = root.right, root.left
    invertBinaryTree(root.left)
    invertBinaryTree(root.right)


tree = Node(3, Node(9), Node(20, Node(15), Node(7)))
print (invertBinaryTree(tree))
