"""
1249. Minimum Remove to Make Valid Parentheses

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:
Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
"""
class Solution:
  def minRemoveToMakeValid(self, s: str) -> str:
    list_s = list(s)
    stack_s = []

    for i in range(len(list_s)):
      if s[i] == '(':
        stack_s.append(i)
      elif s[i] == ')':
        if stack_s:
          stack_s.pop()
        else:
          list_s[i] = ""
          
    # print(list_s)
    # print(stack_s)
    # print(''.join(list_s))
    for i in stack_s:
      list_s[i] = ""
    return ''.join(list_s)

# Test Case 1
s = "lee(t(c)o)de)"
ans = Solution().minRemoveToMakeValid(s)
print("Test Case 1")
print("expected: lee(t(c)o)de, ouput:",ans)

# Test Case 2
s = "a)b(c)d"
ans = Solution().minRemoveToMakeValid(s)
print("Test Case 2")
print("expected: ab(c)d, ouput:",ans)