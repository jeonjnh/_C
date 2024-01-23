"""
1287. Element Appearing More Than 25% In Sorted Array

Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

Example 1:
Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6

Example 2:
Input: arr = [1,1]
Output: 1
"""


class Solution:

  def findSpecialInteger(self, arr: list[int]) -> int:
    target = len(arr) / 4

    dic = {}

    for n in arr:
      if n not in dic:
        dic[n] = 1
      else:
        dic[n] += 1

    for key, value in dic.items():
      if value > target:
        return key

    return -1

# Example 1
arr = [1,2,2,6,6,6,6,7,10]
output = 6
ans = Solution().findSpecialInteger(arr)
print("output: ", output, " | ", "ans: ", ans)