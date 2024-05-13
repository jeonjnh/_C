"""
861. Score After Flipping Matrix

You are given an m x n binary matrix grid.

A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score after making any number of moves (including zero moves).

Example 1:
Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation: 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
"""


class Solution:

  def matrixScore(self, grid: list[list[int]]) -> int:
    m = len(grid)
    n = len(grid[0])

    for i in range(m):
      if grid[i][0] == 0:
        for j in range(n):
          grid[i][j] ^= 1

    #print(grid)

    for j in range(1, n):
      row_sum = 0
      for i in range(m):
        row_sum += grid[i][j]
      if row_sum < m - row_sum:
        for i in range(m):
          grid[i][j] ^= 1

    #print(grid)

    score = 0

    for i in range(m):
      for j in range(n):
        c_score = grid[i][j] << (n - 1 - j)
        score += c_score

    return score

# Example 1
grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output = 39
ans = Solution().matrixScore(grid)
print("Output= ", Output, " ans= ", ans)