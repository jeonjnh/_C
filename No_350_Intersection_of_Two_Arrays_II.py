"""
350. Intersection of Two Arrays II
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
"""
class Solution:
  def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
    map = {}
    result = []
    for num in nums1:
      if num not in map:
        map[num] = 1
      else:
        map[num] += 1

    for num in nums2:
      if num in map and map[num] >= 1:
        result.append(num)
        map[num] -= 1
    
    return result

# Test 1
nums1 = [1,2,1]
nums2 = [2,2]
print("expected: [2], output: ",Solution().intersect(nums1,nums2))

# Test 2
nums1 = [1,2,2,1]
nums2 = [2,2]
print("expected: [2,2], output: ",Solution().intersect(nums1,nums2))

# Test 3
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print("expected: [4,9], output: ",Solution().intersect(nums1,nums2))