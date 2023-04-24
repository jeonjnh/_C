"""
739. Daily Temperatures

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
"""

# Time O(n²) --> not accepted
"""class Solution:
  def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
    ans = []
    for i in range(len(temperatures)):
      step = 0
      for j in range(i,len(temperatures)):
        if temperatures[i] < temperatures[j]:
          ans.append(step)
          break
        elif j == len(temperatures)-1:
          ans.append(0)
        step += 1
    return ans"""

# Time O(n)
class Solution:
  def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
    ans = [0] * len(temperatures)
    stack = []

    for i,t in enumerate(temperatures):
      while stack and temperatures[stack[-1]] < t:
        curr = stack.pop()
        ans[curr] = i - curr

      stack.append(i)
    
    return ans

# Test Case
temperatures = [73,74,75,71,69,72,76,73]
ans = Solution().dailyTemperatures(temperatures)
print(ans)
