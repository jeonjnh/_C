"""
1207. Unique Number of Occurrences

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
"""


class Solution:

  def uniqueOccurrences(self, arr: list[int]) -> bool:
    dic = {}
    for i in range(len(arr)):
      if arr[i] not in dic:
        dic[arr[i]] = 1
      else:
        dic[arr[i]] += 1

    res = []

    for val in dic.values():
      res.append(val)

    for r in res:
      if res.count(r) > 1:
        return False

    return True

# Test Case 
arr = [1,2,2,1,1,3]
ans = Solution().uniqueOccurrences(arr)
print("expected: True, ouput:",ans)