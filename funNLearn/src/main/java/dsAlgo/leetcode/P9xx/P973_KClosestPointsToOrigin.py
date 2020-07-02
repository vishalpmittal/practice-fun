"""
    tag: math

    We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
    (Here, the distance between two points on a plane is the Euclidean distance.)

    You may return the answer in any order.  
    The answer is guaranteed to be unique (except for the order that it is in.)

    Example 1: points = [[1,3],[-2,2]], K = 1
    Output: [[-2,2]]
    Explanation: 
    The distance between (1, 3) and the origin is sqrt(10).
    The distance between (-2, 2) and the origin is sqrt(8).
    Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
    We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

    Example 2: points = [[3,3],[5,-1],[-2,4]], K = 2
    Output: [[3,3],[-2,4]]
    (The answer [[-2,4],[3,3]] would also be accepted.)
 
    Note:
    -  1 <= K <= points.length <= 10000
    -  -10000 < points[i][0] < 10000
    -  -10000 < points[i][1] < 10000
"""
from typing import List
from queue import PriorityQueue


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if len(points) <= K:
            return points
        points = sorted(points, key=lambda x: x[0] ** 2 + x[1] ** 2)
        return points[:K]

    def kClosest1(self, points: List[List[int]], K: int) -> List[List[int]]:
        pq = PriorityQueue(maxsize=K)
        print(pq)
        for n in points:
            dist = n[0] ** 2 + n[1] ** 2
            pq.put((dist, n[0], n[1]))
        print(pq)


Solution().kClosest([[3, 3], [5, -1], [-2, 4]], 2) == [[-2, 4], [3, 3]]
Solution().kClosest([[1, 3], [-2, 2]], 1) == [[-2, 2]]
Solution().kClosest1([[3, 3], [5, -1], [-2, 4]], 2) == [[-2, 4], [3, 3]]


print("Tests Passed!!")
