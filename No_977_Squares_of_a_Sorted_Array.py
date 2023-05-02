"""
977. Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""


class Solution:

  def sortedSquares(self, nums: list[int]) -> list[int]:
    n = len(nums)
    s = 0
    e = n-1
    k = n-1

    ans = [0]*n

    while k >= 0:
      if abs(nums[s]) > nums[e]:
        ans[k] = nums[s]*nums[s]
        s += 1
      else:
        ans[k] = nums[e]*nums[e]
        e -= 1
      k -= 1

    return ans

# Test Case 1
nums = [-4,-1,0,3,10]
ans = Solution().sortedSquares(nums)
print("expected: [0,1,9,16,100], ouput:",ans)

# Test Case 2
nums = [-7,-3,2,3,11]
ans = Solution().sortedSquares(nums)
print("expected: [4,9,9,49,121], ouput:",ans)