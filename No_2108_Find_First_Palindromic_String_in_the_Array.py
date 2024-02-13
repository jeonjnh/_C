"""
2108. Find First Palindromic String in the Array

Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.

Example 1:
Input: words = ["abc","car","ada","racecar","cool"]
Output: "ada"
Explanation: The first string that is palindromic is "ada".
Note that "racecar" is also palindromic, but it is not the first.

Example 2:
Input: words = ["notapalindrome","racecar"]
Output: "racecar"
Explanation: The first and only string that is palindromic is "racecar".

Example 3:
Input: words = ["def","ghi"]
Output: ""
Explanation: There are no palindromic strings, so the empty string is returned.
"""
class Solution:

  def findPalindrome(self, word):
      n = len(word) // 2
      for i in range(n):
          if word[i] != word[len(word) - 1 - i]:
              return False
      return True
  
  
  def firstPalindrome(self, words: list[str]) -> str:
      for word in words:
          if self.findPalindrome(word):
              return word
      return ""

# Test Case 1
words = ["abc","car","ada","racecar","cool"]
ans = Solution().firstPalindrome(words)
Output="ada"
print(Output, ans)

# Test Case 2
words = ["notapalindrome","racecar"]
ans = Solution().firstPalindrome(words)
Output = "racecar"
print(Output, ans)