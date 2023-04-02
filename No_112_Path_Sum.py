"""
112. Path Sum
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.
"""
# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
class Solution:
  def helper(self, root, targetSum, nodeSum):
    if not root:
      return False
    if not root.left and not root.right:
      nodeSum += root.val
      if targetSum == nodeSum:
        return True
      else:
        return False
    return self.helper(root.left, targetSum, nodeSum+root.val) and self.helper(root.right, targetSum, nodeSum+root.val)
  def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
    if not root:
      return False
    nodeSum = 0
    return self.helper(root, targetSum, nodeSum)

def buildTree(nodes):
  # 트리가 비어있을 경우 None 반환
  if not nodes:
    return None

  # root 노드 생성
  root = TreeNode(nodes[0])
  queue = [root]  # 현재 레벨의 노드를 담는 큐
  i = 1  # 리스트 인덱스

  # 큐가 빌 때까지 노드 생성
  while queue and i < len(nodes):
    curr_node = queue.pop(0)  # 큐의 첫 번째 노드 pop
    
    # 왼쪽 자식 노드 생성
    if i < len(nodes) and nodes[i] is not None:
      curr_node.left = TreeNode(nodes[i])
      queue.append(curr_node.left)
    i += 1
    
    # 오른쪽 자식 노드 생성
    if i < len(nodes) and nodes[i] is not None:
      curr_node.right = TreeNode(nodes[i])
      queue.append(curr_node.right)
    i += 1

  return root

def printRoot(root):
  if not root:
    return
  print(root.val)
  printRoot(root.left)
  printRoot(root.right)

# Test Case 1
nodes = [5,4,8,11,None,13,4,7,2,None,None,None,1]
root = buildTree(nodes)
printRoot(root)
targetSum = 22
ans = Solution().hasPathSum(root, targetSum)
print(ans)