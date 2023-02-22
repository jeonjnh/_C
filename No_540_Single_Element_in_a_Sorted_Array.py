"""
540. Single Element in a Sorted Array

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

Example 1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: nums = [3,3,7,7,10,11,11]
Output: 10
"""


# Bitwise XOR Operation is O(n) Solution
class Solution:

  def singleNonDuplicate(self, nums: list[int]) -> int:
    if len(nums) == 0:
      return None

    sum = nums[0]
    for num in nums[1:]:
      sum ^= num

    return sum


"""
#Binary Search (not finished) O(log n) solution
class Solution:
  def singleNonDuplicate(self, nums: list[int]) -> int:
    start = 0 
    end = len(nums) - 1
    if(end == 0):
      return nums[0]
    elif(nums[0] != nums[1]):
      return nums[0]
    elif(nums[end - 1] != nums[end]):
      return nums[end]

    while(start <= end):
      mid = (start + end) // 2
      print(nums[start:end+1])
      if(nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]):
        return nums[mid]
      elif(nums[mid] == nums[mid+1] and nums[mid] != nums[mid-1]):
        start = mid + 1
      else:
        end = mid - 1    
    
    return -1
"""
# Example 1 --> output 2
nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
ans = Solution().singleNonDuplicate(nums)
print(ans)

# Example 2 --> output 10
nums = [3, 3, 7, 7, 10, 11, 11]
ans = Solution().singleNonDuplicate(nums)
print(ans)
