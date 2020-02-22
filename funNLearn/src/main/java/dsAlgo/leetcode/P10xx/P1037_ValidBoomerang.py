"""
    Tag: math

    A boomerang is a set of 3 points that are all distinct 
    and not in a straight line. Given a list of three points in 
    the plane, return whether these points are a boomerang.

    Example 1: Input: [[1,1],[2,3],[3,2]] Output: true
    Example 2: Input: [[1,1],[2,2],[3,3]] Output: false

    Note:
    -  points.length == 3
    -  points[i].length == 2
    -  0 <= points[i][j] <= 100
"""
from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        # Assuming three points are A, B, C.
        # The other idea is to calculate the slope of AB and AC.
        # K_AB = (p[0][0] - p[1][0]) / (p[0][1] - p[1][1])
        # K_AC = (p[0][0] - p[2][0]) / (p[0][1] - p[2][1])
        # We check if K_AB != K_AC, instead of calculate a fraction.
        return (p[2][1]-p[1][1])*(p[1][0]-p[0][0]) != (p[2][0]-p[1][0])*(p[1][1]-p[0][1])

# Another way is to check if it's a valid triagle.
# find out all three sides of the triagle sqrt((x2-x1)^2 + (y2-y1)^2)
# verify sum of any two sides is greater than the third side


assert Solution().isBoomerang([[1, 1], [2, 3], [3, 2]])
assert not Solution().isBoomerang([[1, 1], [2, 2], [3, 3]])
print('Tests Passed!!')
