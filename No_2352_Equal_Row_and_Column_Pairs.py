"""
2352. Equal Row and Column Pairs

Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

Example 1:

Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]

"""


class Solution:

  def equalPairs(self, grid: list[list[int]]) -> int:
    n = len(grid)
    rev = [[0] * n for _ in range(n)]
    for i in range(n):
      for j in range(n):
        rev[i][j] = grid[j][i]

    cnt = 0

    for i in range(n):
      for j in range(n):
        if rev[i] == grid[j]:
          cnt += 1

    return cnt

# Test Case 1
grid = [[3,2,1],[1,7,6],[2,7,7]]
ans = Solution().equalPairs(grid)
print("Test Case 1")
print("expected: 1, ouput:",ans)

# Test Case 2
grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
ans = Solution().equalPairs(grid)
print("Test Case 2")
print("expected: 3, ouput:",ans)

# Test Case 3
grid = [[13,13],[13,13]]
ans = Solution().equalPairs(grid)
print("Test Case 3")
print("expected: 4, ouput:",ans)