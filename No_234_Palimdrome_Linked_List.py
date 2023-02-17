"""
234. Palindrome Linked List

Given the head of a singly linked list, return true if it is a palindrome  or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
"""


# Definition for singly-linked list.
class ListNode:

  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Solution:

  def isPalindrome(self, head: ListNode) -> bool:
    if not head:
      return False

    ptr = head
    answer = False
    array = []
    while (ptr):
      array.append(ptr.val)
      ptr = ptr.next

    if (array == array[::-1]):
      answer = True
    else:
      answer = False

    return answer


# Test Case : Example 1
head = ListNode()
Node_1 = ListNode()
Node_1.val = 1
Node_2 = ListNode()
Node_2.val = 2
Node_3 = ListNode()
Node_3.val = 2
Node_4 = ListNode()
Node_4.val = 1

head.next = Node_1
Node_1.next = Node_2
Node_2.next = Node_3
Node_3.next = Node_4

answer_1 = Solution().isPalindrome(head.next)
print(answer_1)

# Test Case : Example 2
answer_2 = Solution().isPalindrome(head)
print(answer_2)
