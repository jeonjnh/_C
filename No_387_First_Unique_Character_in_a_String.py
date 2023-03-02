"""
387. First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1
"""

class Solution:
  def firstUniqChar(self, s: str) -> int:
    map = {}
    for c in s:
      if c not in map:
          map[c] = 1
      else:
          map[c] += 1

    for i in range(len(s)):
      if(map[s[i]] == 1):
          return i

    return -1

s = "leetcode"
print("expected: 0, output: ", Solution().firstUniqChar(s))

s = "loveleetcode"
print("expected: 2, output: ", Solution().firstUniqChar(s))

s = "aabb"
print("expected: -1, output: ", Solution().firstUniqChar(s))