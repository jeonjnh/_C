"""
16. 3Sum Closest

Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
"""

# Time Limit Exceeded O(n^3)
"""
class Solution:
  def threeSumClosest(self, nums: list[int], target: int) -> int:
      
    closesum = float('inf')
    for i in range(len(nums)-2):
      for j in range(i+1,len(nums)-1):
        for k in range(j+1,len(nums)):
          total = nums[i] + nums[j] + nums[k]
          if(abs(closesum - target) > abs(total - target)):
            closesum = total

    
    return closesum
"""


# O(n^2)
class Solution:
  def threeSumClosest(self, nums: list[int], target: int) -> int:
      
    closesum = float('inf')
    nums.sort()

    for i in range(len(nums) - 2):
      if i > 0 and nums[i - 1] == nums[i]:
        continue

      left = i + 1
      right = len(nums) - 1
      while (left < right):
        total = nums[i] + nums[left] + nums[right]

        if total == target:
          return total
        elif total < target:
          left += 1
        else:
          right -= 1

        if (abs(closesum - target) > abs(total - target)):
          closesum = total

    return closesum    

# Test Case 1
nums = [-1, 2, 1, -4]
target = 1
ans = Solution().threeSumClosest(nums, target)
print(ans)

# Test Case 2 -> Time Limit
nums = [
  -754, -836, 7, 602, -412, -883, 724, -376, -692, 335, -130, -893, 259, 30,
  977, -831, 618, -707, 478, 319, -312, -575, -525, -704, -102, 753, -512,
  -449, 74, -819, 729, 509, -129, 354, 322, -391, -349, -537, -203, 779, 511,
  198, 961, -676, -535, 873, -963, 538, 695, 80, -971, 480, -890, -491, -567,
  102, -777, 595, -907, 897, -66, 985, -275, -159, -680, 190, 634, 262, 717,
  -936, -456, 2, -501, 428, -572, 64, -241, -33, -624, -849, -939, -541, -602,
  -51, -310, 853, 160, 141, 507, 56, -639, 905, 456, -62, -708, -443, 394,
  -813, -917, 716, 297, -810, 829, 206, 496, -610, 341, 292, 661, 994, 612,
  -95, 668, 791, -144, -249, 479, 522, -192, -464, -47, -418, -684, -592, 696,
  -267, -421, -825, -113, -451, -989, -966, 240, -168, 830, -516, -662, 895,
  -557, 585, 828, -263, 632, 438, -308, 760, 539, 152, -476, 700, 528, -643,
  790, -852, 884, 390, 840, -536, -133, -91, 377, -276, -379, 720, 451, -723,
  104, 148, -693, 964, 418, 899, 799, -771, 313, -884, 646, -672, 798, -611,
  34, -542, 167, -642, 232, 379, 217, -991, -434, -265, -158, 218, 130, 877,
  -985, -38, 737, 971, 32, -206, 817, 188, 500, -508, -251, 163, -383, -973,
  697, -24, -256, -659, 392, -377, -65, 814, 812, -230, -221, 625, -445, -545,
  -101, 83, 443, -4, -728, -982, -204, -331, -983, -588, 177, -362, -220, -314,
  868, -407, 158, 287, 1000, 211, -843, -946, 686, 684, -736, -156, -322, 800,
  367, -877, -651, -797, 943, -400, -780, -87, -960, 14, 183, 811, 461, 420,
  -623, -926, 105, 545, -857, -625, 196, -437, 222, -329, -97, -987, -603,
  -235, -105, 508, 459, 153, 680, 58, -134, 246, -865, -477, 126, 99, -160, 9,
  -54, 870, 761, -574, -606, 484, 304, -387, 843, -81, 888, 563, -209, -582,
  -12, -698, -543, -490, -938, -100
]
target = -6155
ans = Solution().threeSumClosest(nums, target)
print(ans)
