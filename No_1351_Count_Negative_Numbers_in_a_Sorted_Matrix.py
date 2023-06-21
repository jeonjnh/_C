"""
1351. Count Negative Numbers in a Sorted Matrix

Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

Example 1:
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.

Example 2:
Input: grid = [[3,2],[1,0]]
Output: 0
"""


class Solution:

  def countNegatives(self, grid: list[list[int]]) -> int:
    rows = len(grid)
    columns = len(grid[0])
    cnt = 0
    for r in range(rows):
      if grid[r][0] < 0:
        cnt += columns
      elif grid[r][-1] > 0:
        cnt += 0
      else:
        for c in range(columns):
          if grid[r][c] < 0:
            cnt += 1

    return cnt

# Test case
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
ans = Solution().countNegatives(grid)
print("expected:8, ouput:",ans)