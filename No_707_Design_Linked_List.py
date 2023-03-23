"""
707. Design Linked List
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
 
Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3
"""


class Node:

  def __init__(self, val=0, nextNode=None):
    self.val = val
    self.next = nextNode


class MyLinkedList:

  def __init__(self):
    self.head = Node(0)
    self.size = 0

  def get(self, index: int) -> int:
    if index >= self.size:
      return -1
    curr = self.head
    for _ in range(index + 1):
      curr = curr.next
    return curr.val

  def addAtHead(self, val: int) -> None:
    self.addAtIndex(0, val)

  def addAtTail(self, val: int) -> None:
    self.addAtIndex(self.size, val)

  def addAtIndex(self, index: int, val: int) -> None:
    if index > self.size:
      return

    prev = self.head
    for _ in range(index):
      prev = prev.next

    newNode = Node(val, prev.next)
    #print(newNode.val, index)
    prev.next = newNode
    self.size += 1

  def linkedlistprint(self):
    ptr = self.head.next
    linkedlist = []
    for i in range(self.size):
      linkedlist.append(ptr.val)
      #print(ptr.val)
      ptr = ptr.next

    print(linkedlist)

  def deleteAtIndex(self, index: int) -> None:
    if index >= self.size:
      return

    prev = self.head
    for _ in range(index):
      prev = prev.next

    prev.next = prev.next.next
    self.size -= 1


LinkedList = MyLinkedList()
LinkedList.addAtIndex(0, 99)
LinkedList.addAtIndex(1, 100)
LinkedList.linkedlistprint()
print(LinkedList.get(1))
LinkedList.addAtHead(11)
LinkedList.addAtTail(22)
LinkedList.linkedlistprint()
LinkedList.deleteAtIndex(0)
LinkedList.linkedlistprint()
