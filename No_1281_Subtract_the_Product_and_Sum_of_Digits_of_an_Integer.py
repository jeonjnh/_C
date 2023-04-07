"""
1281. Subtract the Product and Sum of Digits of an Integer

Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 
Example 1:
Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15

Example 2:
Input: n = 4421
Output: 21
Explanation: 
Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21
"""


class Solution:

  def subtractProductAndSum(self, n: int) -> int:
    p_digit = 1
    s_digit = 0

    while n > 0:
      d = n % 10
      n = n // 10
      p_digit *= d
      s_digit += d

    return p_digit - s_digit

# Test Case 1
n = 234
ans = Solution().subtractProductAndSum(n)
print("expected: 15, output:",ans)