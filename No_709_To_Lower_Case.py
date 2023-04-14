"""
709. To Lower Case

Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

Example 1:
Input: s = "Hello"
Output: "hello"

Example 2:
Input: s = "here"
Output: "here"

Example 3:
Input: s = "LOVELY"
Output: "lovely"
"""


class Solution:

  def toLowerCase(self, s: str) -> str:
    temp = list(s)
    for i, char in enumerate(temp):
      if (ord(char)) >= 65 and (ord(char)) <= 90:
        temp[i] = chr(ord(char) + 32)

    return "".join(temp)

# Test Case
s = "HELLO"
ans = Solution().toLowerCase(s)
print(ans)
