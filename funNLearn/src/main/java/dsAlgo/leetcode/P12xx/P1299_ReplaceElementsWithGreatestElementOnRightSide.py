"""
    Tag: array, integer

    Given an array arr, replace every element in that array with 
    the greatest element among the elements to its right, 
    and replace the last element with -1.
    After doing so, return the array.

    Example 1: Input: arr = [17,18,5,4,6,1]
    Output: [18,6,6,6,1,-1]

    Constraints:
    -  1 <= arr.length <= 10^4
    -  1 <= arr[i] <= 10^5
"""
from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr[-1], mx = -1, arr[-1]
        for i in range(len(arr)-2, -1, -1):
            mx, arr[i] = max(mx, arr[i]), mx
        return arr


assert Solution().replaceElements([17, 18, 5, 4, 6, 1]) == [18, 6, 6, 6, 1, -1]
print('Tests Passed!!')
