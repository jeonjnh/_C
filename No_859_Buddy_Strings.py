"""
859. Buddy Strings

Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
 
Example 1:

Input: s = "ab", goal = "ba"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.

Example 2:

Input: s = "ab", goal = "ab"
Output: false
Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.

Example 3:

Input: s = "aa", goal = "aa"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.
"""


class Solution:

  def buddyStrings(self, s: str, goal: str) -> bool:
    if len(s) != len(goal):
      return False

    if s == goal:
      freq = [0] * 26
      for ch in s:
        freq[ord(ch) - ord('a')] += 1
        if freq[ord(ch) - ord('a')] == 2:
          return True
      return False

    n = len(s)
    check = []
    for i in range(n):
      if s[i] != goal[i]:
        check.append(i)

    if len(check) == 0 or len(check) > 2:
      return False
    elif len(check) == 1:
      return False
    elif len(check) == 2:
      if s[check[0]] == goal[check[1]] and s[check[1]] == goal[check[0]]:
        return True
      else:
        return False

# Test Case
s = "ab"
goal = "ba"
ans = Solution().buddyStrings(s,goal)
print(ans)