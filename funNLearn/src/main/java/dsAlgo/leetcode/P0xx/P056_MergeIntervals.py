"""
    Tag: dp, array, integer

    Given a collection of intervals, merge all overlapping intervals.
    Example 1: [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

    Example 2: [[1,4],[4,5]]
    Output: [[1,5]]
    Explanation: Intervals [1,4] and [4,5] are considered overlapping.
    
    NOTE: input types have been changed on April 15, 2019. 
    Please reset to default code definition to get new method signature.
"""
from typing import List


class Solution:
    def merge(self, I: List[List[int]]) -> List[List[int]]:
        if not I or len(I) <= 1:
            return I

        I.sort(key=lambda x: x[0])
        ans, i, l, h = [], 1, I[0][0], I[0][1]
        while i < len(I):
            if h >= I[i][0]:
                h = max(h, I[i][1])
            else:
                ans.append([l, h])
                l, h = I[i][0], I[i][1]
            i += 1

        ans.append([l, h])
        return ans


assert Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6],
                                                                 [8, 10],
                                                                 [15, 18]]
assert Solution().merge([[1, 4], [4, 5]]) == [[1, 5]]
print('Tests Passed!!')
