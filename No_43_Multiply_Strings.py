"""
43. Multiply Strings

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"
"""


class Solution:

  def multiply(self, num1: str, num2: str) -> str:
    dic = {
      "1": 1,
      "2": 2,
      "3": 3,
      "4": 4,
      "5": 5,
      "6": 6,
      "7": 7,
      "8": 8,
      "9": 9,
      "0": 0
    }
    int_nums1, int_nums2 = 0, 0
    for n in num1:
      a = dic[n]
      int_nums1 = int_nums1 * 10 + a

    for n in num2:
      a = dic[n]
      int_nums2 = int_nums2 * 10 + a

    return str(int_nums1 * int_nums2)

# Test Case 1
num1 = "2"
num2 = "3"
ans = Solution().multiply(num1,num2)
print("expected: 6, output:",ans)

# Test Case 2
num1 = "123"
num2 = "456"
ans = Solution().multiply(num1,num2)
print("expected: 56088, output:",ans)