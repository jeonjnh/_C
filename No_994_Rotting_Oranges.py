"""
994. Rotting Oranges

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
"""

from collections import deque

class Solution:
  def orangesRotting(self, grid: list[list[int]]) -> int:
    rows, columns = len(grid), len(grid[0])
    visit = grid
    cntFreshOrange = 0
    q = deque()
    for i in range(rows):
      for j in range(columns):
        if visit[i][j] == 2:
          q.append((i,j))
        if visit[i][j] == 1:
          cntFreshOrange += 1

    if cntFreshOrange == 0:
      return 0 #no fresh orage
    if not q:
      return -1 #no rotting oragne
      
    # print(q)
    # print(cntFreshOrange)
    minutes = 0
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    while q:
      size = len(q)
      while(size > 0):
        x, y = q.popleft()
        size -= 1
        for dx, dy in dirs:
          i = x + dx
          j = y + dy
          if 0 <=i<rows and 0<=j<columns and visit[i][j] == 1:
            visit[i][j] = 2
            cntFreshOrange -= 1
            q.append((i,j))

      minutes += 1

    if cntFreshOrange == 0:
      return minutes - 1
    
    return -1

# Test Case 1 -> ans = 4
grid = [[2,1,1],[1,1,0],[0,1,1]]
ans = Solution().orangesRotting(grid)
print("Test Case 1 expected 4, result = ",ans)

# Test Case 2 -> ans = -1
grid = [[2,1,1],[0,1,1],[1,0,1]]
ans = Solution().orangesRotting(grid)
print("Test Case 2 expected -1, result = ",ans)

# Test Case 3 -> ans = 0
grid = [[0,2]]
ans = Solution().orangesRotting(grid)
print("Test Case 3 expected 0, result = ",ans)
