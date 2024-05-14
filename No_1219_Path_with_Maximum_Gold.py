"""
1219. Path with Maximum Gold

In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position, you can walk one step to the left, right, up, or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.


Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.

Example 2:

Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.

"""


class Solution:
  row_dir = [1, -1, 0, 0]
  col_dir = [0, 0, -1, 1]

  def dfs(self, grid, x, y, n, m):
    if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == 0:
      return 0

    curr = grid[x][y]
    grid[x][y] = 0
    maxgold_local = curr

    for i in range(4):
      newX = x + self.row_dir[i]
      newY = y + self.col_dir[i]
      maxgold_local = max(maxgold_local,
                          curr + self.dfs(grid, newX, newY, n, m))

    grid[x][y] = curr

    #print(maxgold_local)

    return maxgold_local

  def getMaximumGold(self, grid: list[list[int]]) -> int:
    n = len(grid)
    m = len(grid[0])
    maxGold = 0

    for i in range(n):
      for j in range(m):
        if grid[i][j] != 0:
          maxGold = max(maxGold, self.dfs(grid, i, j, n, m))

    return maxGold

grid = [[0,6,0],[5,8,7],[0,9,0]]
Output = 24
ans = Solution().getMaximumGold(grid)
print("Output= ", Output, " ans= ", ans)
