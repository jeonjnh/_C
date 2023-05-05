"""
1456. Maximum Number of Vowels in a Substring of Given Length

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
"""


class Solution:

  def maxVowels(self, s: str, k: int) -> int:

    vowels = {'a', 'e', 'i', 'o', 'u'}

    count = 0
    for i in range(k):
      count += int(s[i] in vowels)
    answer = count

    for i in range(k, len(s)):

      count += int(s[i] in vowels)
      count -= int(s[i-k] in vowels)

      answer = max(answer, count)

    return answer

# Test Case
s = "abciiidef"
k = 3

ans = Solution().maxVowels(s,k)
print("expected: 3, ouput:",ans)