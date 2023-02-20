"""
108. Convert Sorted Array to Binary Search Tree

Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
"""

#Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right
    
class Solution:
  def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
    if not nums:
        return None

    mid = len(nums) // 2
    root = TreeNode()
    root.val = nums[mid]
    root.left = self.sortedArrayToBST(nums[:mid])
    root.right = self.sortedArrayToBST(nums[mid+1:])

    return root




#print root value
def treeToString(root: TreeNode, root_list: list) -> str:
  if root is None:
    return root_list.append('null')
  else:
    root_list.append(root.val)

  treeToString(root.left, root_list)
  treeToString(root.right, root_list)

  return root_list

nums = [-10,-3,0,5,9]
solution = Solution()
root = solution.sortedArrayToBST(nums)
answer_list = []
tree_str = treeToString(root,answer_list)
print(tree_str)


  