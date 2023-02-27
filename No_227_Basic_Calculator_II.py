"""
227. Basic Calculator II

Given a string s which represents an expression, evaluate this expression and return its value. 
The integer division should truncate toward zero.
You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:
Input: s = "3+2*2"
Output: 7

Example 2:
Input: s = " 3/2 "
Output: 1

Example 3:

Input: s = " 3+5 / 2 "
Output: 5
"""


class Solution:

  def calculate(self, s: str) -> int:
    result = []
    operator = '+'
    curr_num = 0

    for c in s + '+':
      #print(result)
      if c.isdigit():
        curr_num = curr_num * 10 + int(c)

      if not c.isdigit() and c != ' ':
        if operator == '+':
          result.append(curr_num)
        elif operator == '-':
          result.append(-curr_num)
        elif operator == '*':
          result.append(result.pop() * curr_num)

        elif operator == '/':
          result.append(int(result.pop() / curr_num))

        curr_num = 0
        operator = c

    return sum(result)


s = "14-3/2"
ans = Solution().calculate(s)
print(ans)
