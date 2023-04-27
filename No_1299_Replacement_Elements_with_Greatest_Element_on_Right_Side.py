"""
1299. Replace Elements with Greatest Element on Right Side

Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

Example 1:
Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation: 
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.
"""


class Solution:

  def replaceElements(self, arr: list[int]) -> list[int]:

    max_num = arr[-1]
    n = len(arr) - 1

    for i in range(n, -1, -1):
      if i == n:
        arr[i] = -1
      else:
        temp = arr[i]
        arr[i] = max_num
        if temp > max_num:
          max_num = temp

    return arr


# test case
arr1 = [17,18,5,4,6,1]
arr2 = [400]
out1 = [18,6,6,6,1,-1]
out2 = [-1]
test = [arr1, arr2]
out = [out1, out2]

for i in range(len(test)):
  ans = Solution().replaceElements(test[i])
  print(f'expected: {out[i]}, output: {ans}')