"""
1232. Check If It Is a Straight Line
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

Example 1:
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Example 2:
Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
"""
"""
class Solution:
  def checkStraightLine(self, coordinates: list[list[int]]) -> bool:

    kx = coordinates[1][0] - coordinates[0][0]
    ky = coordinates[1][1] - coordinates[0][1]

    if kx == 0:
      for i in range(1, len(coordinates)-1):
        if coordinates[i+1][0] - coordinates[i][0] != 0:
          return False
    elif ky == 0:
      for i in range(1, len(coordinates)-1):
        if coordinates[i+1][1] - coordinates[i][1] != 0:
          return False
    else:
      for i in range(1, len(coordinates)-1):
        if (coordinates[i+1][0] - coordinates[i][0]) == 0:
          return False
        if (coordinates[i+1][1] - coordinates[i][1]) == 0:
          return False
        k_curr = (coordinates[i+1][1] - coordinates[i][1]) / (coordinates[i+1][0] - coordinates[i][0])
        if k_curr != (ky/kx):
          return False
    
    return True
"""


class Solution:

  def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
    x1, x2 = coordinates[0][0], coordinates[1][0]
    y1, y2 = coordinates[0][1], coordinates[1][1]
    for x3, y3 in coordinates[2:]:
      if (y3 - y2) * (x2 - x1) != (y2 - y1) * (x3 - x2):
        return False

    return True


# Test Case 1 : straight line
coordinates = [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]
ans = Solution().checkStraightLine(coordinates)
print(ans)

# Test Case 2 : not straight line
coordinates = [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]
ans = Solution().checkStraightLine(coordinates)
print(ans)

# Test case 3 : vertical straight line
coordinates = [[0, 0], [0, 1], [0, -1]]
ans = Solution().checkStraightLine(coordinates)
print(ans)

# Test case 4 : horizontal straight line
coordinates = [[1, 0], [-1, 0], [1, 0]]
ans = Solution().checkStraightLine(coordinates)
print(ans)
