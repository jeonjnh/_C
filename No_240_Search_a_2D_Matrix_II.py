"""
240. Search a 2D Matrix II

Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
 
Example 1:
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true

Example 2:
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false
"""
class Solution:
  def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
    row = len(matrix)
    column = len(matrix[0])

    for i in range(row):
      if matrix[i][0] > target:
        continue
      elif matrix[i][0] == target or matrix[i][-1] == target:
        return True
      elif matrix[i][0] < target or matrix[i][-1] > target:
        l, r = 0, column-1
        while l<=r:
          m = (l+r)//2
          if matrix[i][m] == target:
            return True
          elif matrix[i][m] < target:
            l = m + 1
          else:
            r = m - 1

    return False

# Test Case 1
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
ans = Solution().searchMatrix(matrix, target)
print("expexted: True, output:", ans)

# Test Case 2
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 20
ans = Solution().searchMatrix(matrix, target)
print("expexted: False, output:", ans)

# Test Case 3
matrix = [[-5]]
target = -5
ans = Solution().searchMatrix(matrix, target)
print("expexted: True, output:", ans)