"""
1089. Duplicate Zeros

Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

Example 1:
Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Example 2:
Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]
"""


class Solution:

  def duplicateZeros(self, arr: list[int]) -> None:
    """
        Do not return anything, modify arr in-place instead.
        """
    m = len(arr)
    i = 0
    while i < m - 1:
      if arr[i] == 0:
        for n in range(m - 1, i + 1, -1):
          arr[n] = arr[n - 1]
        arr[i + 1] = 0
        i += 1
      i += 1

# test case
arr = [1,0,2,3,0,4,5,0]
ans = Solution().duplicateZeros(arr)
print("expected: [1,0,0,2,3,0,0,4], ouput:", arr)