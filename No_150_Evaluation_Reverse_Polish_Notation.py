"""
150. Evaluate Reverse Polish Notation

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:
The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.

Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""


class Solution:

  def cal(self, a, b, operator):
    if operator == '+':
      return a + b
    elif operator == '-':
      return a - b
    elif operator == '*':
      return a * b
    elif operator == '/':
      return int(a / b)

  def evalRPN(self, tokens: list[str]) -> int:
    stack = []

    for t in tokens:
      if t in ['+', '-', '*', '/']:
        num2 = stack.pop()
        num1 = stack.pop()
        ans = self.cal(num1, num2, t)
        stack.append(ans)
      else:
        stack.append(int(t))

    return stack[-1]

# Example 1:
tokens = ["2","1","+","3","*"]
ans = Solution().evalRPN(tokens)
ouput = 9
print(ouput, ans)

# Example 2:
tokens = ["4","13","5","/","+"]
ans = Solution().evalRPN(tokens)
ouput = 6
print(ouput, ans)