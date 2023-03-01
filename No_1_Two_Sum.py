"""
1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
 
Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

"""

# Approach 1 : Brute Force
# Time Complexity : O(n^2), Space Complexity : O(1)
# class Solution:

#   def twoSum(self, nums: list[int], target: int) -> list[int]:
#     ans = []

#     for i in range(len(nums) - 1):
#       for j in range(i + 1, len(nums)):
#         if ((nums[i] + nums[j]) == target):
#           ans.append(i)
#           ans.append(j)
#           break

#     return ans

# Approach 2 : Hash Table -> Dictionanry
# Time Complexity : O(n), Space Complexity : O(n)
# class Solution:

#   def twoSum(self, nums: list[int], target: int) -> list[int]:
#     map = {}
#     for i in range(len(nums)):
#       map[nums[i]] = i

#     for i in range(len(nums)):
#       check = target - nums[i]
#       if check in map and map[check] != i:
#         return [i, map[check]]


# Code Improvement
class Solution:

  def twoSum(self, nums: list[int], target: int) -> list[int]:
    map = {}
    for i in range(len(nums)):
      check = target - nums[i]
      if check in map and map[check] != i:
        return [i, map[check]]
      map[nums[i]] = i


# Test Case 1
nums = [2, 7, 11, 15]
target = 9
print("expected: [0,1], Output: ", Solution().twoSum(nums, target))

# Test Case 2
nums = [3, 2, 4]
target = 6
print("expected: [1,2], Output: ", Solution().twoSum(nums, target))
