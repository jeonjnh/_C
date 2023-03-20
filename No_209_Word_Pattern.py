"""
290. Word Pattern

Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
"""


class Solution:

  def wordPattern(self, pattern: str, s: str) -> bool:
    hmap = {}
    ss = s.split()

    if len(pattern) != len(ss):
      return False

    for i, p in enumerate(pattern):
      if not p in hmap:
        hmap[p] = ss[i]
      else:
        if hmap[p] != ss[i]:
          return False

    return True if (len(set(hmap.values())) == len(hmap)) else False


# Test Case 1
pattern = "abba"
s = "dog dog dog dog"
ans = Solution().wordPattern(pattern, s)
print("expected: False, ouput:", ans)

# Test Case 2
pattern = "aaa"
s = "aa aa aa aa"
ans = Solution().wordPattern(pattern, s)
print("expected: False, ouput:", ans)
