"""
No_230_Kth_Smallest_Element_in_a_BST.py

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
"""

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right
class Solution:
  def kthSmallest(self, root: TreeNode, k: int) -> int:
      
    ptr = root
    def check_value(root,val):
      if root is not None:
        val.append(root.val)
        check_value(root.left,val)
        check_value(root.right,val)

      return val

    val_list = check_value(ptr,[])
    val_list.sort()
    print(val_list)
    return val_list[k-1]

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

ans = Solution().kthSmallest(root,1)
print(ans)