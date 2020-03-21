"""
    Tag: array, binary search

    A peak element is an element that is greater than its neighbors.
    Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
    The array may contain multiple peaks, in that case return 
    the index to any one of the peaks is fine.

    You may imagine that nums[-1] = nums[n] = -∞.

    Example 1: nums = [1,2,3,1]
    Output: 2
    Explanation: 3 is a peak element and your function should return the index number 2.

    Example 2: nums = [1,2,1,3,5,6,4]
    Output: 1 or 5 
    Explanation: Your function can return either index number 1 where the 
    peak element is 2, or index number 5 where the peak element is 6.
    
    Note:
    Your solution should be in logarithmic complexity.
"""
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def findPeakUtil(arr, low, high, n):
            mid = low + (high - low) // 2

            if (mid == 0 or arr[mid - 1] <= arr[mid]) and (
                mid == n - 1 or arr[mid + 1] <= arr[mid]
            ):
                return mid

            elif mid > 0 and arr[mid - 1] > arr[mid]:
                return findPeakUtil(arr, low, (mid - 1), n)

            else:
                return findPeakUtil(arr, (mid + 1), high, n)

        return findPeakUtil(nums, 0, len(nums) - 1, len(nums))


assert Solution().findPeakElement([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) in range(10)
assert Solution().findPeakElement([1, 2, 3, 1]) == 2
assert Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4]) in [1, 5]
print("Tests Passed!!!")

