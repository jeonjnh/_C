"""
24. Swap Nodes in Pairs
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]
"""


# Definition for singly-linked list.
class ListNode:

  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Solution:

  def swapPairs(self, head: ListNode) -> ListNode:
    if not head or not head.next:
      return head

    dummyHead = ListNode(0, head)
    prev = dummyHead

    while head and head.next:
      f = head
      r = head.next
      prev.next = r

      f.next = r.next
      r.next = f

      prev = f
      head = f.next

    return dummyHead.next

def Node_Print(head):
  ptr = head
  res = []
  while ptr:
    res.append(ptr.val)
    ptr = ptr.next

  print(res)
    
# Test Case 1
node_4 = ListNode(4, None)
node_3 = ListNode(3, node_4)
node_2 = ListNode(2, node_3)
head = ListNode(1, node_2)

Node_Print(head)

ans = Solution().swapPairs(head)
Node_Print(ans)