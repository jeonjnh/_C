"""
53. Maximum Subarray
Given an integer array nums, find the subarray  with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
"""

#Time Limited O(n^2)
# class Solution:
#   def maxSubArray(self, nums: list[int]) -> int:
#     ans = float('-inf')
#     for i in range(len(nums)):
#         sum = 0
#         for j in range(i, len(nums)):
#             sum += nums[j]
#             ans = max(ans,sum)

#     return ans


# Sliding Window
class Solution:

  def maxSubArray(self, nums: list[int]) -> int:
    maxSum = nums[0]
    currSum = 0

    for n in nums:
      if currSum < 0:
        currSum = 0
      currSum += n
      maxSum = max(currSum, maxSum)

    return maxSum


# Test 1 --> output 6
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(Solution().maxSubArray(nums))

# Test 2 --> output 23
nums = [5, 4, -1, 7, 8]
print(Solution().maxSubArray(nums))