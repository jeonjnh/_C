"""
645. Set Mismatch

You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]

Example 2:
Input: nums = [1,1]
Output: [1,2]
"""


class Solution:

  def findErrorNums(self, nums: list[int]) -> list[int]:

    duplicate = -1
    missing = -1

    dic_nums = [0] * (len(nums) + 1)

    for num in nums:
      dic_nums[num] += 1

    for i in range(1, len(nums) + 1):
      if dic_nums[i] == 2:
        duplicate = i

      if dic_nums[i] == 0:
        missing = i

    return [duplicate, missing]

# Example 1:
nums = [1, 2, 2, 4]
Output = [2,3]
ans = Solution().findErrorNums(nums)
print("Expect : ", Output, " , Got : ", ans)