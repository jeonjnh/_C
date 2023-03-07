"""
69. Sqrt(x)
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
"""

class Solution:
  def mySqrt(self, x: int) -> int:
    lx = x
    i = 0
    sq = i*i

    while sq<lx:
      i += 1
      sq = i*i

    if sq == lx:
      return i
    if sq > lx:
      return i-1

# Test Case 1
x = 4
print("expected: 2, output: ",Solution().mySqrt(x))

# Test Case 2
x = 8
print("expected: 2, output: ",Solution().mySqrt(x))

# Test Case 3
x = 3
print("expected: 1, output: ",Solution().mySqrt(x))