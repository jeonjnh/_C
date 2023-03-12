"""
169. Majority Element

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""
from collections import Counter
class Solution:
  def majorityElement(self, nums: list[int]) -> int:
    num_counter = Counter(nums)
    
    return num_counter.most_common(1)[0][0]

# Test case 1
nums = [2,2,1,1,1,2,2]
print("expected: 2, output:",Solution().majorityElement(nums))

# Test case 2
nums = [3,2,3]
print("expected: 3, output:",Solution().majorityElement(nums))