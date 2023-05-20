"""
643. Maximum Average Subarray I

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
"""

# Time Limit
"""class Solution:

  def findMaxAverage(self, nums: list[int], k: int) -> float:
    res = sum(nums[0:k])
    for i in range(1, len(nums) - k + 1):
      res = max(res, sum(nums[i:k + i]))
      print(i, k + 1 + i)
    return float(res / k)"""


class Solution:

  def findMaxAverage(self, nums: list[int], k: int) -> float:
    summe = [0] * len(nums)
    summe[0] = nums[0]
    for i in range(1, len(nums)):
      summe[i] = summe[i-1] + nums[i]
    #print(summe)

    res = summe[k-1]

    for i in range(k, len(nums)):
      res = max(res, (summe[i] - summe[i-k]))
    
    return float(res/k)

# Test case
nums = [1,12,-5,-6,50,3]
k = 4
ans = Solution().findMaxAverage(nums, k)
print("expected: 12.75, ouput:",ans)
