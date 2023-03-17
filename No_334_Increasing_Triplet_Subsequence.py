"""
334. Increasing Triplet Subsequence

Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Example 1:
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
"""

# Time Limit - Brute Force
"""
class Solution:
  def increasingTriplet(self, nums: list[int]) -> bool:
    for i in range(len(nums)-2):
      for j in range(i+1, len(nums)-1):
        if nums[i] < nums[j]:
          for k in range(j+1, len(nums)):
            if nums[j] < nums[k]:
              return True
    return False
"""


# Accepted
class Solution:

  def increasingTriplet(self, nums: list[int]) -> bool:
    first = second = float('inf')
    for num in nums:
      if num <= first:
        first = num
        #print("first",first)
      elif num <= second:
        second = num
        #print("second",second)
      else:
        return True

    return False


print("334. Increasing Triplet Subsequence\n")
# Test Case 1
nums = [1,2,3,4,5]
ans = Solution().increasingTriplet(nums)
print("expected: True, output:", ans)

# Test Case 2
nums = [5, 4, 3, 2, 1]
ans = Solution().increasingTriplet(nums)
print("expected: False, output:", ans)

# Test Case 3
nums = [2, 1, 5, 0, 4, 6]
ans = Solution().increasingTriplet(nums)
print("expected: True, output:", ans)
