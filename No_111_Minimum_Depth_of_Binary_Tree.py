"""
111. Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 2
"""


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:

  def minDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0

    if not root.left and not root.right:
      return 1

    if root.left:
      left = self.minDepth(root.left)
    else:
      left = float('inf')

    if root.right:
      right = self.minDepth(root.right)
    else:
      right = float('inf')

    return 1 + min(left, right)
