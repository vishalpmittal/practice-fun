"""
    Tag: binary search

    A conveyor belt has packages that must be shipped from one port 
    to another within D days.
    The i-th package on the conveyor belt has a weight of weights[i].  
    Each day, we load the ship with packages on the conveyor belt 
    (in the order given by weights). We may not load more weight than 
    the maximum weight capacity of the ship.

    Return the least weight capacity of the ship that will result in all 
    the packages on the conveyor belt being shipped within D days.

    Example 1: Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5 Output: 15
    Explanation: 
    A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
    1st day: 1, 2, 3, 4, 5
    2nd day: 6, 7
    3rd day: 8
    4th day: 9
    5th day: 10

    Note that the cargo must be shipped in the order given, so using a ship 
    of capacity 14 and splitting the packages into parts like 
    (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed. 

    Example 2: Input: weights = [3,2,2,4,1,4], D = 3 Output: 6
    Explanation: 
    A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
    1st day: 3, 2
    2nd day: 2, 4
    3rd day: 1, 4

    Example 3: Input: weights = [1,2,3,1,1], D = 4 Output: 3
    Explanation: 
    1st day: 1
    2nd day: 2
    3rd day: 3
    4th day: 1, 1

    Note:
    -  1 <= D <= weights.length <= 50000
    -  1 <= weights[i] <= 500
"""
from typing import List


class Solution:
    def shipWithinDays(self, a: List[int], d: int) -> int:
        # To get to exactly D days and minimize the max sum of any partition, we
        # do binary search in the sum space which is bounded by [max(a), sum(a)]
        # One thing to note in Binary Search for this problem, is even if we
        # end up finding a weight, that gets us to D partitions, we still want
        # to continue the space on the minimum side, because, there could be a
        # better minimum sum that still passes <= D paritions.
        lo, hi = max(a), sum(a)
        while lo < hi:
            mid = (lo + hi) // 2
            tot, res = 0, 1
            for wt in a:
                if tot + wt > mid:
                    res += 1
                    tot = wt
                else:
                    tot += wt
            if res <= d:
                hi = mid
            else:
                lo = mid + 1
        return lo


assert Solution().shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 15
assert Solution().shipWithinDays([3, 2, 2, 4, 1, 4], 3) == 6
assert Solution().shipWithinDays([1, 2, 3, 1, 1], 4) == 3
print('Tests Passed!!')
