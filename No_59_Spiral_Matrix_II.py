"""
59. Spiral Matrix II

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

"""


class Solution:

  def generateMatrix(self, n: int) -> list[list[int]]:
    ans = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 1
    for l in range((n+1)//2):
      # -->
      for c in range(l, n-l):
        ans[l][c] = cnt
        cnt += 1
      # |
      # V
      for r in range(l+1, n-l):
        ans[r][n-l-1] = cnt
        cnt += 1
      # <-
      for c in range(n-l-2, l-1, -1):
        ans[n-l-1][c] = cnt
        cnt += 1
      # ^
      # |
      for r in range(n-l-2, l, -1):
        ans[r][l] = cnt
        cnt += 1

    return ans

ans = Solution().generateMatrix(4)
print(ans)
