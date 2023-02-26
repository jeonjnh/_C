"""
100. Same Tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false
"""


# Definition for a binary tree node.
class TreeNode:

  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:

  def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    if (p == None and q == None):
      return True
    elif (p != None and q == None):
      return False
    elif (p == None and q != None):
      return False

    if (p.val != q.val):
      return False
    left = self.isSameTree(p.left, q.left)
    right = self.isSameTree(p.right, q.right)

    return left and right


# Create the tree from the bottom up
leaf1 = TreeNode(1)
leaf2 = TreeNode(3)

leaf3 = TreeNode(6)
leaf4 = TreeNode(9)

# Attach leaves to create subtrees
p = TreeNode(2, leaf1, leaf2)
q = TreeNode(8, leaf3, leaf4)
"""
    2       8
   / \     / \
  1   3   6   9
  """

ans = Solution().isSameTree(p, q)
print(ans)

# Create the tree from the bottom up
leaf1 = TreeNode(1)
leaf2 = TreeNode(3)

leaf3 = TreeNode(1)
leaf4 = TreeNode(3)

# Attach leaves to create subtrees
p = TreeNode(2, leaf1, leaf2)
q = TreeNode(2, leaf3, leaf4)
"""
    2       2
   / \     / \
  1   3   1   3
  """

ans = Solution().isSameTree(p, q)
print(ans)