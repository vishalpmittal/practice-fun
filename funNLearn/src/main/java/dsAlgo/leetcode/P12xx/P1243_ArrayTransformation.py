"""
    Tag: array, integer

    Given an initial array arr, every day you produce a new 
    array using the array of the previous day.
    On the i-th day, you do the following operations on the 
    array of day i-1 to produce the array of day i:

    -  If an element is smaller than both its left neighbor and its right neighbor, 
    then this element is incremented.
    -  If an element is bigger than both its left neighbor and its right neighbor, 
    then this element is decremented.
    -  The first and last elements never change.

    After some days, the array does not change. Return that final array.

    Example 1: Input: arr = [6,2,3,4] Output: [6,3,3,4]
    Explanation: On the first day, the array is changed from [6,2,3,4] to [6,3,3,4].
    No more operations can be done to this array.

    Example 2: Input: arr = [1,6,3,4,3,5] Output: [1,4,4,4,4,5]
    Explanation: 
    On the first day, the array is changed from [1,6,3,4,3,5] to [1,5,4,3,4,5].
    On the second day, the array is changed from [1,5,4,3,4,5] to [1,4,4,4,4,5].
    No more operations can be done to this array.

    Constraints:
    1 <= arr.length <= 100
    1 <= arr[i] <= 100
"""
from typing import List


class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        oper = 1
        while oper > 0:
            oper, arr1 = 0, arr.copy()
            for i in range(1, len(arr)-1):
                if arr1[i] > arr1[i-1] and arr1[i] > arr1[i+1]:
                    arr[i], oper = arr[i]-1, oper + 1
                elif arr1[i] < arr1[i-1] and arr1[i] < arr1[i+1]:
                    arr[i], oper = arr[i]+1, oper + 1
        return arr

    def transformArray_short(self, arr: List[int], change: bool = True) -> List[int]:
        while change:
            new = arr[:1] + [b + (a > b < c) - (a < b > c)
                             for a, b, c in zip(arr, arr[1:], arr[2:])] + arr[-1:]
            arr, change = new, arr != new
        return arr


assert Solution().transformArray([6, 2, 3, 4]) == [6, 3, 3, 4]
assert Solution().transformArray([1, 6, 3, 4, 3, 5]) == [1, 4, 4, 4, 4, 5]
assert Solution().transformArray(
    [2, 1, 2, 1, 1, 2, 2, 1]) == [2, 2, 1, 1, 1, 2, 2, 1]

print('Tests Passed!!')
