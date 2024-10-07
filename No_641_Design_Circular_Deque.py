"""
641. Design Circular Deque

Design your implementation of the circular double-ended queue (deque).

Implement the MyCircularDeque class:

MyCircularDeque(int k) Initializes the deque with a maximum size of k.
boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
boolean isEmpty() Returns true if the deque is empty, or false otherwise.
boolean isFull() Returns true if the deque is full, or false otherwise.


Example 1:

Input
["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 2, true, true, true, 4]

Explanation
MyCircularDeque myCircularDeque = new MyCircularDeque(3);
myCircularDeque.insertLast(1);  // return True
myCircularDeque.insertLast(2);  // return True
myCircularDeque.insertFront(3); // return True
myCircularDeque.insertFront(4); // return False, the queue is full.
myCircularDeque.getRear();      // return 2
myCircularDeque.isFull();       // return True
myCircularDeque.deleteLast();   // return True
myCircularDeque.insertFront(4); // return True
myCircularDeque.getFront();     // return 4

"""


class MyCircularDeque:

  def __init__(self, k: int):
    self.myDeque = []
    self.maxLength = k
    self.current = 0

  def insertFront(self, value: int) -> bool:
    if self.current >= self.maxLength:
      return False
    self.myDeque = [value] + self.myDeque
    self.current += 1
    return True

  def insertLast(self, value: int) -> bool:
    if self.current >= self.maxLength:
      return False
    self.myDeque.append(value)
    self.current += 1
    return True

  def deleteFront(self) -> bool:
    if self.current == 0:
      return False
    self.myDeque.pop(0)
    self.current -= 1
    return True

  def deleteLast(self) -> bool:
    if self.current == 0:
      return False
    self.myDeque.pop()
    self.current -= 1
    return True

  def getFront(self) -> int:
    if self.current == 0:
      return -1
    return self.myDeque[0]

  def getRear(self) -> int:
    if self.current == 0:
      return -1
    return self.myDeque[-1]

  def isEmpty(self) -> bool:
    if self.current == 0:
      return True
    else:
      return False

  def isFull(self) -> bool:
    if self.current == self.maxLength:
      return True
    else:
      return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
