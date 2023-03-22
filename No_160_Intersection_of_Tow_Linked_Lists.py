"""
160. Intersection of Two Linked Lists
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:
The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Custom Judge:

The inputs to the judge are given as follows (your program is not given these inputs):

intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.

Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
- Note that the intersected node's value is not 1 because the nodes with value 1 in A and B (2nd node in A and 3rd node in B) are different node references. In other words, they point to two different locations in memory, while the nodes with value 8 in A and B (3rd node in A and 4th node in B) point to the same location in memory.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

  def getIntersectionNode(self, headA: ListNode,
                          headB: ListNode) -> ListNode:
    ptrA = headA
    ptrB = headB
    cntA = 0
    cntB = 0
    while (ptrA or ptrB):
      while (ptrA):
        cntA += 1
        ptrA = ptrA.next
      while (ptrB):
        cntB += 1
        ptrB = ptrB.next

    diff = abs(cntA - cntB)

    if cntA > cntB:
      while (diff > 0):
        headA = headA.next
        diff -= 1
    else:
      while (diff > 0):
        headB = headB.next
        diff -= 1

    while (headA != headB):
      headA = headA.next
      headB = headB.next
    
    return headA


# Test Case 1
l1 = ListNode(2)
l1_1 = ListNode(4)
l1_2 = ListNode(3)
l1.next = l1_1
l1_1.next = l1_2

l2 = ListNode(5)
l2_1 = ListNode(4)
l2_2 = ListNode(3)
l2.next = l2_1
l2_1.next = l2_2

