"""
1496. Path Crossing

Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise
"""


class Solution:

  def isPathCrossing(self, path: str) -> bool:
    curr = (0, 0)
    prev_path = [(0, 0)]
    direction_dict = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}

    for dir in path:
      curr = (curr[0] + direction_dict[dir][0],
              curr[1] + direction_dict[dir][1])
      if curr in prev_path:
        return True
      else:
        prev_path.append(curr)

    return False

# Test Case 1
path = "NES"
ans = Solution().isPathCrossing(path)
print(ans)

# Test Case 2
path = "NESWW"
ans = Solution().isPathCrossing(path)
print(ans)