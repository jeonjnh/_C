"""
258. Add Digits

Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Example 1:
Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.

Example 2:
Input: num = 0
Output: 0
"""
class Solution:
  def addDigits(self, num: int) -> int:
    def checkSum(n):
      if n==0:
        return 0
      nSum = 0
      while n > 0:
        nSum += n%10
        n //= 10

      if nSum >= 10:
        return checkSum(nSum)
      else:
        return nSum

    return checkSum(num)

num = 99
ans = Solution().addDigits(num)
print(ans)
