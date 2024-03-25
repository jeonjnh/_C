"""
287. Find the Duplicate Number

Given an array of integers containing  integers where each integer is in the range inclusive.numsn + 1[1, n]

There is only one repeated number in , return this repeated number.nums

You must solve the problem without modifying the array  and uses only constant extra space.nums

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2

Example 2:

Input: nums = [3,1,3,4,2]
Output: 3

Example 3:

Input: nums = [3,3,3,3,3]
Output: 3

"""


class Solution:

  def findDuplicate(self, nums: list[int]) -> int:
    dic = {}

    for num in nums:
      if num in dic:
        return num
      else:
        dic[num] = 1

    return -1

# example 1
nums = [1,3,4,2,2]
Output = 2
ans = Solution().findDuplicate(nums)
print("ouput: ", Output, "result: ", ans)