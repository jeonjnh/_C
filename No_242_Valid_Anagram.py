"""
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""
from collections import Counter

class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    s_counter = Counter(s)
    t_counter = Counter(t)
    if s_counter == t_counter:
      return True
    else:
      return False

#Example 1
s = "anagram"
t = "nagaram"
print("expected: True, output: ",Solution().isAnagram(s,t))

#Example 2
s = "rat"
t = "car"
print("expected: False, output: ",Solution().isAnagram(s,t))