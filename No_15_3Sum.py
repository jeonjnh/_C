"""
15. 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""
class Solution:
  def threeSum(self, nums: list[int]) -> list[list[int]]:
    nums.sort()
    res = []
    for i, a in enumerate(nums):
      if i > 0 and a == nums[i-1]:
        continue

      l, r = i+1, len(nums)-1
      while l < r:
        tSum = a + nums[l] + nums[r]
        if tSum > 0:
          r -= 1
        elif tSum < 0:
          l += 1
        else:
          if not [a, nums[l], nums[r]] in res:
            res.append([a, nums[l], nums[r]])
          r -= 1

    return res

# Tese case 1
nums = [0,0,0,0]
ans = Solution().threeSum(nums)
print("expected: [[0,0,0]], output: ",ans)

# Tese case 2
nums = nums = [-1,0,1,2,-1,-4]
ans = Solution().threeSum(nums)
print("expected: [[-1,-1,2],[-1,0,1]], output: ",ans)