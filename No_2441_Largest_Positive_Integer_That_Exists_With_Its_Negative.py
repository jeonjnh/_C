"""
2441. Largest Positive Integer That Exists With Its Negative

Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.

Return the positive integer k. If there is no such integer, return -1.



Example 1:

Input: nums = [-1,2,-3,3]
Output: 3
Explanation: 3 is the only valid k we can find in the array.

Example 2:

Input: nums = [-1,10,6,7,-7,1]
Output: 7
Explanation: Both 1 and 7 have their corresponding negative values in the array. 7 has a larger value.

Example 3:

Input: nums = [-10,8,6,7,-2,-3]
Output: -1
Explanation: There is no a single valid k, we return -1.

"""


class Solution:

  def findMaxK(self, nums: list[int]) -> int:
    neg = []
    for n in nums:
      if n < 0:
        neg.append(n)

    ans = -1

    for n in nums:
      if n > ans and -n in neg:
        ans = n

    return ans

nums = [-49,8,19,-39,37,22,-39,4,37,8,20,-2,-4,-5,14,-14,-27,24,30,3,-12,19,22,28,-3,-6,6,22,37,27,16,27,-6,-49,31,29]
Output = 27

ans = Solution().findMaxK(nums)


print("Output= ", Output, " ans= ", ans)