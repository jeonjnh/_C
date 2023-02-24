"""
199. Binary Tree Right Side View
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []
"""


# Definition for a binary tree node.
class TreeNode:

  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


from collections import deque


class Solution:

  def rightSideView(self, root: TreeNode) -> list[int]:
    if root is None:
      return []

    result = []
    q = deque()
    q.append(root)

    while (q):
      level = len(q)
      for i in range(level):
        node = q.popleft()
        if (i == level - 1):
          result.append(node.val)
        if (node.left):
          q.append(node.left)
        if (node.right):
          q.append(node.right)

    return result


# Create the tree from the bottom up
leaf1 = TreeNode(1)
leaf2 = TreeNode(3)
leaf3 = TreeNode(6)
leaf4 = TreeNode(9)

# Attach leaves to create subtrees
subtree1 = TreeNode(2, leaf1, leaf2)
subtree2 = TreeNode(8, leaf3, leaf4)

# Attach subtrees to create the full tree
root = TreeNode(4, subtree1, subtree2)
"""
        4
      /   \
     /     \
    2       8
   / \     / \
  1   3   6   9
"""

ans = Solution().rightSideView(root)
print(ans)
