"""
1051. Height Checker

A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.

You are given an integer array heights representing the current order that the students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).

Return the number of indices where heights[i] != expected[i].

Example 1:

Input: heights = [1,1,4,2,1,3]
Output: 3
Explanation: 
heights:  [1,1,4,2,1,3]
expected: [1,1,1,2,3,4]
Indices 2, 4, and 5 do not match.
"""


class Solution:

  def bubble_sort(self, sort_array):
    n = len(sort_array)
    for i in range(n - 1):
      for j in range(n - i - 1):
        if sort_array[j] > sort_array[j + 1]:
          sort_array[j], sort_array[j + 1] = sort_array[j + 1], sort_array[j]

    return sort_array

  def heightChecker(self, heights: list[int]) -> int:

    cnt = 0
    sort_height = heights[:]
    self.bubble_sort(sort_height)

    for i in range(len(heights)):
      if heights[i] != sort_height[i]:
        cnt += 1

    return cnt

# Example 1
heights = [1,1,4,2,1,3]
Output = 3
ans = Solution().bubble_sort(heights)
print("Output= ", Output, " ans= ", ans)