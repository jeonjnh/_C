"""
1035. Uncrossed Lines

You are given two integer arrays nums1 and nums2. We write the integers of nums1 and nums2 (in the order they are given) on two separate horizontal lines.

We may draw connecting lines: a straight line connecting two numbers nums1[i] and nums2[j] such that:

nums1[i] == nums2[j], and
the line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting line cannot intersect even at the endpoints (i.e., each number can only belong to one connecting line).

Return the maximum number of connecting lines we can draw in this way.

Example 1:
Input: nums1 = [1,4,2], nums2 = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from nums1[1] = 4 to nums2[2] = 4 will intersect the line from nums1[2]=2 to nums2[1]=2.

Example 2:
Input: nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
Output: 3

Example 3:
Input: nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]
Output: 2
"""


class Solution:

  def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:
    n1 = len(nums1)
    n2 = len(nums2)

    map = {}

    def solve(i, j):
      if i == 0 or j == 0:
        return 0

      if (i, j) in map:
        return map[(i, j)]

      if nums1[i - 1] == nums2[j - 1]:
        map[(i, j)] = 1 + solve(i - 1, j - 1)
      else:
        map[(i, j)] = max(solve(i - 1, j), solve(i, j - 1))
        
      return map[(i,j)]
    
    return solve(n1, n2)

# Test Case 1
nums1 = [1,4,2]
nums2 = [1,2,4]
ans = Solution().maxUncrossedLines(nums1, nums2)
print("expected: 2, ouput:",ans)

# Test Case 2
nums1 = [2,5,1,2,5]
nums2 = [10,5,2,1,5,2]
ans = Solution().maxUncrossedLines(nums1, nums2)
print("expected: 3, ouput:",ans)