"""
459. Repeated Substring Pattern

Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

Example 1:
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Example 2:
Input: s = "aba"
Output: false

Example 3:
Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
"""


class Solution:

  def repeatedSubstringPattern(self, s: str) -> bool:
    r = 0
    if len(s) == 1:
      return False

    for i in range(1, len(s)):
      if s[i] == s[0]:
        r = i
        break

    repeat = s[:r]

    for i in range(0, len(s), r):
      if repeat != s[i:i + r]:
        return False

    return True

# Test Case
s = "abab"
ans = Solution().repeatedSubstringPattern(s)
print("expected: True, ouput:",ans)

# Test Case
s = "aba"
ans = Solution().repeatedSubstringPattern(s)
print("expected: False, ouput:",ans)

# Test Case
s = "abcabcabcabc"
ans = Solution().repeatedSubstringPattern(s)
print("expected: True, ouput:",ans)

# Test Case --> fail
s = "abaababaab"
ans = Solution().repeatedSubstringPattern(s)
print("expected: True, ouput:",ans)