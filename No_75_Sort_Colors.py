"""
75. Sort Colors

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]
"""
"""
class Solution:

  def sortColors(self, nums: list[int]) -> None:

    low = 0
    mid = 0
    high = len(nums) - 1
    while mid <= high:
      if nums[mid] == 0:
        self.swap(nums, mid, low)
        low += 1
        mid += 1
      elif nums[mid] == 2:
        self.swap(nums, mid, high)
        high -= 1
      else:
        mid += 1

  def swap(self, nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp
"""


class Solution:

  def sortColors(self, nums: list[int]) -> None:
    """
      Do not return anything, modify nums in-place instead.
      """
    cnt = [0] * 3
    for n in nums:
      cnt[n] += 1

    i = 0

    for clr, freq in enumerate(cnt):
      for _ in range(freq):
        nums[i] = clr
        i += 1


# Test Case 1
nums = [2, 0, 2, 1, 1, 0]
ans = Solution().sortColors(nums)
print("expected: [0,0,1,1,2,2], output:", nums)

# Test Case 2
nums = [2, 0, 1]
ans = Solution().sortColors(nums)
print("expected: [0,1,2], output:", nums)
