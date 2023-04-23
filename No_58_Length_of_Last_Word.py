"""
58. Length of Last Word

Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
"""


class Solution:

  def lengthOfLastWord(self, s: str) -> int:
    cnt = 0
    i = len(s) - 1

    while i >= 0 and s[i] == ' ':
      i -= 1

    for n in range(i, -1, -1):
      if s[n] != ' ':
        cnt += 1
      elif s[n] == ' ':
        return cnt
    return cnt

# Test Case 
s = "   fly me   to   the moon  "
ans = Solution().lengthOfLastWord(s)
print("expected: 4, ouput:", ans)