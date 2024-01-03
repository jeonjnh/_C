"""
1758. Minimum Changes To Make Alternating Binary String

You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

Return the minimum number of operations needed to make s alternating.

Example 1:
Input: s = "0100"
Output: 1
Explanation: If you change the last character to '1', s will be "0101", which is alternating.

Example 2:
Input: s = "10"
Output: 0
Explanation: s is already alternating.

Example 3:
Input: s = "1111"
Output: 2
Explanation: You need two operations to reach "0101" or "1010".
"""


class Solution:

  def minOperations(self, s: str) -> int:
    cnt_0 = 0
    cnt_1 = 0

    for i in range(len(s)):
      if i % 2 == 0:
        if s[i] == '1':
          cnt_0 += 1
        else:
          cnt_1 += 1
      else:
        if s[i] == '0':
          cnt_0 += 1
        else:
          cnt_1 += 1

    return min(cnt_0, cnt_1)


# Example 1:
s = "0100"
# Output: 1
ans = Solution().minOperations("0100")
print("output:1, ", ans)
