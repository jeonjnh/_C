"""
1700. Number of Students Unable to Eat Lunch

The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers and respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.01

The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:

If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
Otherwise, they will leave it and go to the queue's end.
This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

You are given two integer arrays and where is the type of the sandwich in the stack ( is the top of the stack) and is the preference of the student in the initial queue ( is the front of the queue). Return the number of students that are unable to eat.studentssandwichessandwiches[i]i​​​​​​thi = 0students[j]j​​​​​​thj = 0



Example 1:

Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
Output: 0 
Explanation:
- Front student leaves the top sandwich and returns to the end of the line making students = [1,0,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,0,1,1].
- Front student takes the top sandwich and leaves the line making students = [0,1,1] and sandwiches = [1,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [1,1,0].
- Front student takes the top sandwich and leaves the line making students = [1,0] and sandwiches = [0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,1].
- Front student takes the top sandwich and leaves the line making students = [1] and sandwiches = [1].
- Front student takes the top sandwich and leaves the line making students = [] and sandwiches = [].
Hence all students are able to eat.
Example 2:

Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
Output: 3
"""

from collections import deque

class Solution:

  def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
    
    students_deque = deque(students[::-1])
    sandwich_stack = sandwiches[::-1]

    #print(students_deque)
    #print(sandwich_stack)

    last_served = 0

    while len(students_deque) > 0 and last_served < len(students_deque):
      if sandwich_stack[-1] == students_deque[0]:
        sandwich_stack.pop()
        students_deque.popleft()
        last_served = 0
      else:
        students_deque.append(students_deque.popleft())
        last_served += 1

    return len(students_deque)

    return 0

# Test Case 1
students = [1,1,0,0]
sandwiches = [0,1,0,1]
Output = 0 
ans = Solution().countStudents(students, sandwiches)
print("Output= ", Output, " ans = ", ans)