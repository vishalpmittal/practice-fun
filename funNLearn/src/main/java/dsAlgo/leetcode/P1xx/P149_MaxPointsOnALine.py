"""
    Tag: math

    Given n points on a 2D plane, find the maximum number of points 
    that lie on the duplicates straight line.
    
    Example 1: [[1,1],[2,2],[3,3]]; Output: 3
    Explanation:
    ^
    |
    |        o
    |     o
    |  o  
    +------------->
    0  1  2  3  4
    
    Example 2: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]; Output: 4
    Explanation:
    ^
    |
    |  o
    |     o        o
    |        o
    |  o        o
    +------------------->
    0  1  2  3  4  5  6
    
    NOTE: input types have been changed on April 15, 2019. 
    Please reset to default code definition to get new method signature.
"""
from typing import List


class Solution:
    def gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    def calc_slope(self, p1, p2):
        dy = p2[1] - p1[1]
        dx = p2[0] - p1[0]
        divisor = self.gcd(dx, dy)
        return (dx / divisor, dy / divisor)

    def maxPoints(self, points: List[List[int]]) -> int:
        """
            for each point get the slope with every other point
            Use a combination of dy and dx as key to store in dictionary
            in the dictionary get the point with highest number of points in one slope
        """
        if points == None:
            return 0
        if len(points) <= 2:
            return len(points)

        max_points = 0
        for i in range(len(points)):
            slopes, dups = {}, 1

            for j in range(i + 1, len(points)):
                if points[i] == points[j]:
                    dups += 1
                    continue
                slope = self.calc_slope(points[i], points[j])
                slopes[slope] = slopes.get(slope, 0) + 1

            max_points = max(max_points, dups)

            for slope in slopes:
                max_points = max(max_points, slopes[slope] + dups)
        return max_points


assert Solution().maxPoints([[1, 1], [2, 2], [3, 3]]) == 3
assert Solution().maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]) == 4
print("Tests Passed!!")
