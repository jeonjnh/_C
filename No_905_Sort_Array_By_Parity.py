"""
905. Sort Array By Parity

iven an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
Return any array that satisfies this condition.

Example 1:
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Example 2:
Input: nums = [0]
Output: [0]
"""


class Solution:

  def sortArrayByParity(self, nums: list[int]) -> list[int]:
    start = 0
    end = len(nums) - 1

    while start < end:
      # print(start, end)
      if nums[start]%2 == 1 and nums[end]%2 == 0:
        nums[start], nums[end] = nums[end], nums[start]

      if nums[start]%2 == 0:
        start += 1
      if nums[end]%2 == 1:
        end -= 1

    return nums

# test case
nums = [3,1,2,4]
ans = Solution().sortArrayByParity(nums)
print("expected:[2,4,3,1], output:",ans)