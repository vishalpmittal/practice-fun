"""
    Tag: math

    You have a list of points in the plane. Return the area of the largest 
    triangle that can be formed by any 3 of the points.

    Example: Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]  Output: 2
    Explanation:   The five points are show in the figure below. 
    The red triangle is the largest.
    https://leetcode.com/problems/largest-triangle-area/

    Notes:
    -  3 <= points.length <= 50.
    -  No points will be duplicated.
    -   -50 <= points[i][j] <= 50.
    -  Answers within 10^-6 of the true value will be accepted as correct.
"""
from typing import List
import itertools


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(p, q, r):
            return .5 * abs(p[0]*q[1]+q[0]*r[1]+r[0]*p[1]
                            - p[1]*q[0]-q[1]*r[0]-r[1]*p[0])

        return max(area(*triangle)
                   for triangle in itertools.combinations(points, 3))


assert Solution().largestTriangleArea(
    [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]) == 2
print('Tests Passed!!')
