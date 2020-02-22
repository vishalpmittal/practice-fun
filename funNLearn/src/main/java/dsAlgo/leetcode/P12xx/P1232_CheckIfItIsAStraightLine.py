"""
    Tag: math

    You are given an array coordinates, coordinates[i] = [x, y], where [x, y] 
    represents the coordinate of a point. 
    Check if these points make a straight line in the XY plane.

    Ex1: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]] Out: true
    Ex2: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]] Out: false

    Constraints:
    -  2 <= coordinates.length <= 1000
    -  coordinates[i].length == 2
    -  -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
    -  coordinates contains no duplicate point.
"""
from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # The slope for a line through any 2 points (x0, y0) and (x1, y1)
        # is (y1 - y0) / (x1 - x0); Therefore, for any given 3 points
        # (denote the 3rd point as (x, y)), if they are in a straight line,
        # the slopes of the lines from the 3rd point to the 2nd point and
        # the 2nd point to the 1st point must be equal:
        (x0, y0), (x1, y1) = coordinates[: 2]
        return all((x1 - x0) * (y - y1) == (x - x1) * (y1 - y0) for x, y in coordinates)


assert Solution().checkStraightLine(
    [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]])
assert not Solution().checkStraightLine(
    [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]])
print('Tests Passed!!')
