"""
414. Third Maximum Number

Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

Example 1:
Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.

Example 2:
Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.

Example 3:
Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.
"""

import collections
class Solution:

  def thirdMax(self, nums: list[int]) -> int:
    ans = collections.deque([])
    for num in nums:

      if not ans:
        ans.append(num)
      elif len(ans) <= 2:
        if num > ans[-1]:
          ans.append(num)
        elif ans[0] < num and num < ans[1]:
          temp = ans[1]
          ans.append(temp)
          ans[1] = num
        elif num < ans[0]:
          ans.appendleft(num)
      else:
        if ans[0] < num and num < ans[1]:
          ans[0] = num
        elif ans[1] < num and num < ans[2]:
          ans[0] = ans[1]
          ans[1] = num
        elif ans[2] < num:
          ans[0] = ans[1]
          ans[1] = ans[2]
          ans[2] = num
          
      if len(ans) > 3:
        ans.popleft()

    return ans[0] if len(ans) == 3 else ans[-1]

nums = [5,2,4,1,3,6,0]
ans = Solution().thirdMax(nums)
print("expected: 4, ouput:",ans)