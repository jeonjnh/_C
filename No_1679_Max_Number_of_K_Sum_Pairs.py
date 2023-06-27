"""
1679. Max Number of K-Sum Pairs

You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.

Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
"""


class Solution:

  def maxOperations(self, nums: list[int], k: int) -> int:
    ans = 0
    nums.sort()
    l, r = 0, len(nums) - 1
    while l < r:
      pair_sum = nums[l] + nums[r]
      if pair_sum == k:
        ans += 1
        l += 1
        r -= 1
      elif pair_sum < k:
        l += 1
      elif pair_sum > k:
        r -= 1

    return ans

# Test Case 1:
nums = [1,2,3,4]
k = 5
ans = Solution().maxOperations(nums, k)
print("expected:2, ouput:",ans)

# Test Case 2:
nums = [3,1,3,4,3]
k = 6
ans = Solution().maxOperations(nums, k)
print("expected:1, ouput:",ans)