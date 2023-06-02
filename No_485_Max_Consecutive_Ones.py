"""
485. Max Consecutive Ones
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
"""


class Solution:

  def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
    s = 0
    e = 0
    i = 0
    res = 0
    nums.append(0)
    if len(nums) == 1:
      if nums[0] == 0:
        return 0
      else:
        return 1

    while i < len(nums):
      while nums[i] == 0 and i < len(nums) - 1:
        i += 1
      s = i
      while nums[i] == 1 and i < len(nums) - 1:
        i += 1
      e = i
      res = max(res, e - s)
      i += 1

    return res

# Test Case 1
nums = [1,1,0,1,1,1]
ans = Solution().findMaxConsecutiveOnes(nums)
print("expected: 3, ouput:",ans)