"""
345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
Input: s = "hello"
Output: "holle"

Example 2:
Input: s = "leetcode"
Output: "leotcede"
"""


class Solution:

  def reverseVowels(self, s: str) -> str:
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    s = list(s)
    start, end = 0, len(s) - 1

    while start < end:
      if s[start] in vowel and s[end] in vowel:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1

      if not s[start] in vowel:
        start += 1
      if not s[end] in vowel:
        end -= 1

    return "".join(s)

# Test Case
s = "hello"
ans = Solution().reverseVowels(s)
print("expected: holle, ouput:",ans)

# Test Case
s = "aA"
ans = Solution().reverseVowels(s)
print("expected: Aa, ouput:",ans)
