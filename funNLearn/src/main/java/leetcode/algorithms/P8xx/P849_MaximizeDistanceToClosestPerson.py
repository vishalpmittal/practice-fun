"""
    Tag: dp, array

    In a row of seats, 1 represents a person sitting in that seat, 
    and 0 represents that the seat is empty. 
    There is at least one empty seat, and at least one person sitting.
    Alex wants to sit in the seat such that the distance between him 
    and the closest person to him is maximized. 

    Return that maximum distance to closest person.

    Example 1: Input: [1,0,0,0,1,0,1] Output: 2
    Explanation: 
    If Alex sits in the second open seat (seats[2]), then the closest 
    person has distance 2.
    If Alex sits in any other open seat, the closest person has distance 1.
    Thus, the maximum distance to the closest person is 2.

    Example 2: Input: [1,0,0,0] Output: 3
    Explanation: 
    If Alex sits in the last seat, the closest person is 3 seats away.
    This is the maximum distance possible, so the answer is 3.

    Note:
    -  1 <= seats.length <= 20000
    -  seats contains only 0s or 1s, at least one 0, and at least one 1.
"""
from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        ls = float('-inf')
        ld = [float('-inf')] * len(seats)
        for i, s in enumerate(seats):
            if s == 1:
                ls = i
                ld[i] = 0
            else:
                ld[i] = i - ls

        rs = float('inf')
        rd = [float('inf')] * len(seats)
        farthest = float('-inf')
        for i, s in reversed(list(enumerate(seats))):
            ls = float('inf')
            if s == 1:
                rs = i
                rd[i] = 0
            else:
                rd[i] = rs - i

            farthest = max(farthest, min(ld[i], rd[i]))
        return farthest

    def maxDistToClosest_1(self, seats: List[int]) -> int:
        # In a group of K adjacent empty seats between two people,
        # the answer is (K+1) / 2.
        ans = 0
        for seat, group in itertools.groupby(seats):
            if not seat:
                K = len(list(group))
                ans = max(ans, (K+1)/2)

        return max(ans, seats.index(1), seats[::-1].index(1))


assert Solution().maxDistToClosest([1, 0, 0, 0, 1, 0, 1]) == 2
assert Solution().maxDistToClosest([1, 0, 0, 0]) == 3
print('Tests Passed!!')
