"""
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""


class Solution:

  def productExceptSelf(self, nums: list[int]) -> list[int]:

    left = [1] * len(nums)
    right = [1] * len(nums)

    # left array
    for i in range(1, len(nums)):
      left[i] = left[i - 1] * nums[i - 1]
    # right array
    for i in range(len(nums) - 2, -1, -1):
      right[i] = right[i + 1] * nums[i + 1]

    for i in range(len(nums)):
      nums[i] = left[i] * right[i]

    return nums


# Test Case 1
nums = [1, 2, 3, 4]
ans = Solution().productExceptSelf(nums)
print("expected: [24,12,8,6], output:", ans)

# Test Case 2
nums = [-1, 1, 0, -3, 3]
ans = Solution().productExceptSelf(nums)
print("expected: [0,0,9,0,0], output:", ans)
