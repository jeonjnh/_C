"""
338. Counting Bits

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
"""


class Solution:

  def countBits(self, n: int) -> list[int]:
    res = []

    for i in range(n + 1):
      s = str(bin(i))
      res.append(s.count('1'))

    return res


# Test Case
n = 2
ans = Solution().countBits(n)
print(ans)