"""
56. Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""


class Solution:

  def merge(self, intervals: list[list[int]]) -> list[list[int]]:
    res = []
    intervals.sort()
    for inter in intervals:
      if not res or res[-1][1] < inter[0]:
        res.append(inter)
      else:
        res[-1][1] = max(res[-1][1], inter[1])

    return res

# Test Case 1
intervals = [[1,3],[2,6],[8,10],[15,18]]
print("expected: [[1,6],[8,10],[15,18]], output:",Solution().merge(intervals))

# Test Case 2
intervals = [[1, 4], [2, 3]]
print("expected: [[1,4]], output:",Solution().merge(intervals))

