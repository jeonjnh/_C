"""
735. Asteroid Collision

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
"""


class Solution:

  def asteroidCollision(self, asteroids: list[int]) -> list[int]:
    stack = []
    stack.append(asteroids[0])

    for i in range(1, len(asteroids)):
      if stack[-1] * asteroids[i] > 0:
        stack.append(asteroids[i])
      elif stack[-1] * asteroids[i] < 0:
        val = stack.pop()
        if abs(val) < abs(asteroids[i]):
          stack.append(asteroids[i])
        elif abs(val) > abs(asteroids[i]):
          stack.append(val)

    while len(stack) > 1 and stack[-1] * stack[-2] < 0:
      val_1 = stack.pop()
      val_2 = stack.pop()
      if abs(val_1) < abs(val_2):
        stack.append(val_2)
      elif abs(val_1) > abs(val_2):
        stack.append(val_1)

    return stack

# Test Case
asteroids = [5,10,-5]
ans = Solution().asteroidCollision(asteroids)
print("expected: [5,10], output:",ans)

# Test Case
asteroids = [-2,-1,1,2]
ans = Solution().asteroidCollision(asteroids)
print("expected: [-2,-1,1,2], output:",ans)