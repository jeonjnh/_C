"""
33. Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1
"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start, end = 0, len(nums)-1
        pivot = nums.index(min(nums))

        if(nums[pivot] <= target and target <= nums[end]):
            if(nums[pivot] == target):
                return pivot
            elif(nums[end] == target):
                return end
            else:
                start = pivot
        elif(nums[start] <= target and nums[pivot-1] >= target):
            if(nums[start] == target):
                return start
            elif(nums[pivot-1] == target):
                return pivot - 1
            else:
                end = pivot - 1
        else:
            return -1

        while(start <= end):
            mid = (start + end)//2
            if(nums[mid] == target):
                return mid
            elif(nums[mid]>target):
                end = mid - 1
            else:
                start = mid + 1
    
  
        return -1


nums = [5,1,3]
target = 5
sol = Solution()  # Create an instance of the Solution class
answer = sol.search(nums, target)  # Call the search method on the instance and pass in nums and target
print(answer)

nums = [4,5,6,7,0,1,2]
target = 0
sol = Solution()  # Create an instance of the Solution class
answer = sol.search(nums, target)  # Call the search method on the instance and pass in nums and target
print(answer)