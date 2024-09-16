"""
539. Minimum Time Difference

Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.


Example 1:

Input: timePoints = ["23:59","00:00"]
Output: 1
Example 2:

Input: timePoints = ["00:00","23:59","00:00"]
Output: 0

"""

from typing import List

class Solution:

  def findMinDifference(self, timePoints: List[str]) -> int:
    time_min = [int(time[:2]) * 60 + int(time[3:]) for time in timePoints]
    time_min.sort()
    print(time_min)

    min_diff = min(
      [time_min[i + 1] - time_min[i] for i in range(len(time_min) - 1)])
    print(min_diff)

    return min(min_diff, 24 * 60 - time_min[-1] + time_min[0])

# Example 1
timePoints = ["23:59","00:00"]
Output = 1
ans = Solution().findMinDifference(timePoints)
print("ans = ", ans, " Output = ", Output)