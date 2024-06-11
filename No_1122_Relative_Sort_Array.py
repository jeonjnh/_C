"""
1122. Relative Sort Array

Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]

Example 2:

Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
Output: [22,28,8,6,17,44]
"""


class Solution:

  def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
    ans = []

    for val in arr2:
      for j in range(len(arr1)):
        if arr1[j] == val:
          ans.append(arr1[j])
          arr1[j] = -1

    #print(ans)
    #print(arr1)

    arr1.sort()
    for val in arr1:
      if val != -1:
        ans.append(val)

    return ans

# Example 1
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
Output = [2,2,2,1,4,3,3,9,6,7,19]
ans = Solution().relativeSortArray(arr1, arr2)
print("Output= ", Output, " ans= ", ans)