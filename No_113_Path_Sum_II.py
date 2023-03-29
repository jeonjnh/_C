"""
113. Path Sum II

Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: []

Example 3:
Input: root = [1,2], targetSum = 0
Output: []
"""


# Definition for a binary tree node.
class TreeNode:

  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:

  def pathSum(self, root: TreeNode, targetSum: int) -> list[list[int]]:

    ans = []

    def dfs(root, targetSum, path):
      if not root:
        print("here")
        return None

      targetSum -= root.val
      path.append(root.val)

      if not root.left and root.right:
        if targetSum == 0:
          ans.append(path.copy())
      else:
        dfs(root.left, targetSum, path)
        dfs(root.right, targetSum, path)

      path.pop()  # leaf node but not right sum path

    dfs(root, targetSum, [])
    return ans


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
nodes = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
root = buildTree(nodes)
#printRoot(root)
targetSum = 22
ans = Solution().pathSum(root, targetSum)
print(ans)