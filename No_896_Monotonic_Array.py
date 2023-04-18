"""
896. Monotonic Array

An array is monotonic if it is either monotone increasing or monotone decreasing.
An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
Given an integer array nums, return true if the given array is monotonic, or false otherwise.

Example 1:
Input: nums = [1,2,2,3]
Output: true

Example 2:
Input: nums = [6,5,4,4]
Output: true

Example 3:
Input: nums = [1,3,2]
Output: false 

Constraints:
1 <= nums.length <= 105
-105 <= nums[i] <= 105
"""


"""class Solution:

  def isMonotonic(self, nums: list[int]) -> bool:

    if len(nums) == 1:
      return True

    idx = 0
    while nums[idx] == nums[idx + 1]:
      idx += 1
      if idx >= len(nums) - 1:
        return True

    if nums[idx] < nums[idx + 1]:
      for i in range(idx, len(nums) - 1):
        if nums[i] > nums[i + 1]:
          return False
    elif nums[idx] > nums[idx + 1]:
      for i in range(idx, len(nums) - 1):
        if nums[i] < nums[i + 1]:
          return False

    return True"""

class Solution:

  def isMonotonic(self, nums: list[int]) -> bool:
    isNondec = True
    isNoninc = True

    for i in range(1,len(nums)):
      if nums[i-1] <= nums[i]:
        isNondec = False
      if nums[i-1] >= nums[i]:
        isNoninc = False
      
    return isNondec or isNoninc
    
nums = [5,3,2,4,1]
ans = Solution().isMonotonic(nums)
print(ans)
