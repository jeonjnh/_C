"""
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself. 

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next
      
class Solution:
  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    dummyHead = ListNode()
    curr = dummyHead
    carry = 0

    while (l1 != None) or (l2 != None) or (carry == 1):
      l1Val = l1.val if l1 else 0
      l2Val = l2.val if l2 else 0
      node_sum = l1Val + l2Val + carry
      carry = node_sum // 10
      newNode = ListNode(node_sum % 10)
      curr.next = newNode
      curr = curr.next

      l1 = l1.next if l1 else None
      l2 = l2.next if l2 else None

    return dummyHead.next

def printNode(node: ListNode):
  ptr = node
  res = []
  while(ptr):
    res.append(ptr.val)
    ptr = ptr.next
  return res
  
# Test Case 1
l1 = ListNode(2)
l1_1 = ListNode(4)
l1_2 = ListNode(3)
l1.next = l1_1
l1_1.next = l1_2

l2 = ListNode(5)
l2_1 = ListNode(6)
l2_2 = ListNode(4)
l2.next = l2_1
l2_1.next = l2_2

ans = Solution().addTwoNumbers(l1,l2)
res = printNode(ans)
print("expected: 708, output:",res)