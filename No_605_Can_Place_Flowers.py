"""
605. Can Place Flowers

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
"""


class Solution:

  def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
    cnt = 0
    for i in range(len(flowerbed)):
      if flowerbed[i] == 0:
        if i == 0 or flowerbed[i - 1] == 0:
          check_left = True
        else:
          check_left = False

        if i == (len(flowerbed) - 1) or flowerbed[i + 1] == 0:
          check_right = True
        else:
          check_right = False

        if check_left and check_right:
          flowerbed[i] = 1
          cnt += 1

    return cnt >= n

# Test Case 
flowerbed = [1,0,0,0,1]
n = 1
ans = Solution().canPlaceFlowers(flowerbed,n)
print("expected: True, ouput:",ans)
