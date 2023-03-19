"""
415. Add Strings

Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

Example 1:
Input: num1 = "11", num2 = "123"
Output: "134"

Example 2:
Input: num1 = "456", num2 = "77"
Output: "533"

Example 3:
Input: num1 = "0", num2 = "0"
Output: "0"
"""


class Solution:

  def strToInt(self, num: str):
    sum_i = 0
    for s in num:
      c = ord(s) - ord('0')
      sum_i = sum_i * 10 + c
    return sum_i

  def intToStr(self, num: int):
    num_s = ""
    if num == 0:
      return str(0)
    while (num > 0):
      c = num % 10
      num = num // 10
      num_s = str(c) + num_s
    return num_s

  def addStrings(self, num1: str, num2: str) -> str:
    sum_num = self.strToInt(num1) + self.strToInt(num2)
    return self.intToStr(sum_num)

# Test Case 1
num1 = "11"
num2 = "123"
ans = Solution().addStrings(num1, num2)
print("expected: 134, output:",ans)

# Test Case 2
num1 = "456"
num2 = "77"
ans = Solution().addStrings(num1, num2)
print("expected: 533, output:",ans)

# Test Case 3
num1 = "0"
num2 = "0"
ans = Solution().addStrings(num1, num2)
print("expected: 0, output:",ans)