class TreeNode:
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

  def __str__(self):
    return str(self.data)

def constructMaxBinaryTree(nums):
  if not nums:
    return None

  maxNum = max(nums)
  maxNumIdx = nums.index(maxNum)

  root = TreeNode(maxNum)
  root.left = constructMaxBinaryTree(nums[:maxNumIdx])
  root.right = constructMaxBinaryTree(nums[maxNumIdx + 1:])

  return root


nums = [3,2,1,6,0,5]
print (constructMaxBinaryTree(nums))