class TreeNode:
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

  def __str__(self):
    return str(self.data)

'''
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

  1. The root is the maximum number in the array.
  2. The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
  3. The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.

Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1

Runs in worst case O(n) time
Leetcode Link: https://leetcode.com/problems/maximum-binary-tree/
'''
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