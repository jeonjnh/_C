"""
4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""


class Solution:

  def findMedianSortedArrays(self, nums1: list[int],
                             nums2: list[int]) -> float:
    mergedList = []
    len_nums1 = len(nums1)
    len_nums2 = len(nums2)

    i, j = 0, 0

    while i < len_nums1 or j < len_nums2:
      if i == len_nums1:
        mergedList.append(nums2[j])
        j += 1
      elif j == len_nums2:
        mergedList.append(nums1[i])
        i += 1
      elif nums1[i] < nums2[j]:
        mergedList.append(nums1[i])
        i += 1
      else:
        mergedList.append(nums2[j])
        j += 1

    if (len_nums1 + len_nums2) % 2 != 0:
      return mergedList[(len_nums1 + len_nums2) // 2]
    else:
      return (mergedList[(len_nums1 + len_nums2) // 2 - 1] +
              mergedList[(len_nums1 + len_nums2) // 2]) / 2

# Test Case 1
nums1 = [1,3]
nums2 = [2]
ans = Solution().findMedianSortedArrays(nums1,nums2)
print(ans)

# Test Case 2
nums1 = [1,3]
nums2 = [2,4]
ans = Solution().findMedianSortedArrays(nums1,nums2)
print(ans)