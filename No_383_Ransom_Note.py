"""
383. Ransom Note

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
"""
from collections import Counter
class Solution:
  def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    note = Counter(ransomNote)
    mag = Counter(magazine)

    for k in note:
        if k in mag:
            if note[k] <= mag[k]:
                continue
            else:
                return False
        else:
            return False

    return True


# Test Case 1
ransomNote = "a"
magazine = "b"
print("expected: False, output:", Solution().canConstruct(ransomNote,magazine))

# Test Case 2
ransomNote = "aa"
magazine = "ab"
print("expected: False, output:", Solution().canConstruct(ransomNote,magazine))

# Test Case 3
ransomNote = "aa"
magazine = "aab"
print("expected: True, output:", Solution().canConstruct(ransomNote,magazine))