"""
1491. Average Salary Excluding the Minimum and Maximum Salary

You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.

Example 1:
Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500

Example 2:
Input: salary = [1000,2000,3000]
Output: 2000.00000
Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
Average salary excluding minimum and maximum salary is (2000) / 1 = 2000
"""


class Solution:

  def average(self, salary: list[int]) -> float:
    sum = 0
    max_salary = float('-inf')
    min_salary = float('inf')

    for emp in salary:
      sum += emp
      max_salary = max(max_salary, emp)
      min_salary = min(min_salary, emp)

    return (sum - max_salary - min_salary) / (len(salary) - 2)

# Test Case 1
salary = [4000,3000,1000,2000]
ans = Solution().average(salary)
print("expected: 2500.00000, output:", ans)

# Test Case 2
salary = [1000,2000,3000]
ans = Solution().average(salary)
print("expected: 2000.00000, output:", ans)