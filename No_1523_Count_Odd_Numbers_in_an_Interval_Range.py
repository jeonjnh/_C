"""
1523. Count Odd Numbers in an Interval Range

Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

Example 1:
Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].

Example 2:
Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].
"""


class Solution:

  def countOdds(self, low: int, high: int) -> int:
    diff = high - low + 1

    if diff % 2 == 0:
      return diff // 2
    else:
      if low % 2 == 1:
        return diff // 2 + 1
      else:
        return diff // 2

#Test Case 1
low, high = 3, 7
ans = Solution().countOdds(low, high)
print("expected: 3, output:", ans)