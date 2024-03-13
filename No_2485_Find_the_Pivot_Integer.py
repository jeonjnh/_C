"""
2485. Find the Pivot Integer

Given a positive integer n, find the pivot integer x such that:

The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.

Example 1:

Input: n = 8
Output: 6
Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.

Example 2:

Input: n = 1
Output: 1
Explanation: 1 is the pivot integer since: 1 = 1.

Example 3:

Input: n = 4
Output: -1
Explanation: It can be proved that no such integer exist.
"""


class Solution:

  def pivotInteger(self, n: int) -> int:
    x = n // 2

    for i in range(x, n + 1):
      sum_1_x = (1 + i) / 2 * i
      sum_x_n = (i + n) / 2 * (n - i + 1)

      if sum_1_x == sum_x_n:
        return i
      elif sum_1_x > sum_x_n:
        return -1

    return -1

# Example 1
n = 8
ans = Solution().pivotInteger(n)
Output = 6
print("output= ", Output, " ans= ", ans)