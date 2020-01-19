"""
    Tag: array, integer

    Given an integer array sorted in non-decreasing order, there is 
    exactly one integer in the array that occurs more than 25% of the time.
    Return that integer.

    Example 1: Input: arr = [1,2,2,6,6,6,6,7,10] Output: 6

    Constraints:
    1 <= arr.length <= 10^4
    0 <= arr[i] <= 10^5
"""
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        d, p25o = {}, len(arr) * 25 / 100
        for n in arr:
            d[n] = d.get(n, 0) + 1
            if d[n] > p25o:
                return n

    def findSpecialInteger(self, arr: List[int]) -> int:
        return Counter(arr).most_common(1)[0][0]


assert Solution().findSpecialInteger([1, 2, 2, 6, 6, 6, 6, 7, 10]) == 6
print('Tests Passed!!')
