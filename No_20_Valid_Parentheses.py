"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
"""

class Solution:
  def isValid(self, s: str) -> bool:
    if len(s)%2 != 0:
      return False

    check = []

    for char in s:
      #print(check)
      if char == '(' or char == '[' or char == '{':
        check.append(char)

      elif char == ')':
        if not check:
          return False
        c = check.pop()
        if c != '(':
          return False
      elif char == ']':
        if not check:
          return False
        c = check.pop()
        if c != '[':
          return False
      elif char == '}':
        if not check:
          return False
        c = check.pop()
        if c != '{':
          return False
    #print(check)
    result = False
    if not check:
      result = True

    return result

# Test Case 1
s = ")("
print("expected: False, output: ",Solution().isValid(s))

# Test Case 2
s = "()[]{}"
print("expected: True, output: ",Solution().isValid(s))

# Test Case 3
s = "()"
print("expected: True, output: ",Solution().isValid(s))