"""
884. Uncommon Words from Two Sentences

A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

Example 1:

Input: s1 = "this apple is sweet", s2 = "this apple is sour"

Output: ["sweet","sour"]

Explanation:

The word "sweet" appears only in s1, while the word "sour" appears only in s2.

Example 2:

Input: s1 = "apple apple", s2 = "banana"

Output: ["banana"]
"""
from typing import List

class Solution:

  def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
    s1_word = s1.split()
    s2_word = s2.split()

    res = {}
    for s1_w in s1_word:
      if s1_w not in res:
        res[s1_w] = 1
      else:
        res[s1_w] += 1
    for s2_w in s2_word:
      if s2_w not in res:
        res[s2_w] = 1
      else:
        res[s2_w] += 1
    ans = []
    for i in res.items():
      if i[1] == 1:
        ans.append(i[0])

    return ans

# Example 1
s1 = "this apple is sweet"
s2 = "this apple is sour"
Output = ["sweet","sour"]
ans = Solution().uncommonFromSentences(s1, s2)
print("ans = ", ans, " Output = ", Output)
