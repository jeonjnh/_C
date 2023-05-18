"""
392. Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
"""


class Solution:

  def isSubsequence(self, s: str, t: str) -> bool:
    s_len = len(s)
    t_len = len(t)
    s_idx, t_idx = 0, 0

    if s_len == 0:
      return True

    while (s_idx < s_len and t_idx < t_len):
      if s[s_idx] == t[t_idx]:
        if s_idx == s_len - 1:
          return True
        else:
          s_idx += 1
          t_idx += 1
      else:
        t_idx += 1

    return False


s = "abc"
t = "ahbgdc"
ans = Solution().isSubsequence(s, t)
print("expected: True, ouput:", ans)
