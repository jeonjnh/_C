"""
566. Reshape the Matrix

In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.
You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.
The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.
If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]

Example 2:
Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]
"""
class Solution:
  def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
    m, n = len(mat), len(mat[0])
    if (m*n) != (r*c):
      return mat

    result = []
    sub = []
    cnt = 0

    for i in range(m):
      for j in range(n):
        sub.append(mat[i][j])
        cnt += 1
        if cnt == c:
          result.append(sub)
          sub = []
          cnt = 0

    return result

# Test Case 1
mat = [[1,2],[3,4]]
r = 1
c = 4
print("expected: [[1,2,3,4]], output: ",Solution().matrixReshape(mat,r,c))

# Test Case 2
mat = [[1,2],[3,4]]
r = 2
c = 4
print("expected: [[1,2],[3,4]], output: ",Solution().matrixReshape(mat,r,c))

# Test Case 3
mat = [[1,2],[3,4]]
r = 4
c = 1
print("expected: [[1],[2],[3],[4]], output: ",Solution().matrixReshape(mat,r,c))