"""
448. Find All Numbers Disappeared in an Array

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:
Input: nums = [1,1]
Output: [2]
"""


class Solution:

  def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
    n = len(nums)
    nums = set(nums)

    ans = []

    for i in range(1, n + 1):
      if i not in nums:
        ans.append(i)

    return ans

nums = [4,3,2,7,8,2,3,1]
ans = Solution().findDisappearedNumbers(nums)
print("expected: [5,6], ouput:",ans)