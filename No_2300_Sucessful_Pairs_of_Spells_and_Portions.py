"""
2300. Successful Pairs of Spells and Potions
You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

Example 1:
Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
Output: [4,0,3]
Explanation:
- 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
- 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
- 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
Thus, [4,0,3] is returned.

Example 2:
Input: spells = [3,1,2], potions = [8,5,8], success = 16
Output: [2,0,2]
Explanation:
- 0th spell: 3 * [8,5,8] = [24,15,24]. 2 pairs are successful.
- 1st spell: 1 * [8,5,8] = [8,5,8]. 0 pairs are successful. 
- 2nd spell: 2 * [8,5,8] = [16,10,16]. 2 pairs are successful. 
Thus, [2,0,2] is returned.
"""

# Brute Force --> not accepted : Time Limit Exceeded
# class Solution:

#   def successfulPairs(self, spells: list[int], potions: list[int],
#                       success: int) -> list[int]:
#     ans = []
#     for s in spells:
#       cnt = 0
#       for p in potions:
#         if s * p >= success:
#           cnt += 1
#       ans.append(cnt)

#     return ans

# Sort and Binary Search
import math
class Solution:

  def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
    ans = []
    potions.sort()

    def findMid(arr, target):
      start = 0
      end = len(arr)-1
      mid = (start + end)//2
      while start <= end:
        if potions[mid] == target:
          return mid
        elif potions[mid] < target:
          start = mid + 1
        else:
          end = mid - 1
        mid = (start + end)//2
      return start

    for s in spells:
      check = math.ceil(success / s)
      if potions[0] >= check:
        ans.append(len(potions))
      elif potions[-1] < check:
        ans.append(0)
      else:
        mid = findMid(potions, check)
        ans.append(len(potions)-mid)

    return ans






# Test Case
spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7

ans = Solution().successfulPairs(spells,potions,success)
print("expected: [4,0,3], output:",ans)

# start = 0
# end = len(potions)-1
# mid = (start + end)//2
# target = 9
# while start < end:
#   print(start, end, mid)
#   if potions[mid] == target:
#     print("mid", mid)
#   elif potions[mid] < target:
#     start = mid + 1
#   else:
#     end = mid - 1
#   mid = (start + end)//2

# print(mid)