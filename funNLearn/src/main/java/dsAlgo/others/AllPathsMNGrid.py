"""
    Tag: matrix, recursive

    Given a grid of size m by n, write an algorithm that computes all 
    paths from 0,0 to m,n such that you can always step horizontally 
    or vertically but cannot reverse.
"""
from typing import List, Tuple


class Solution:
    def getAllPaths(self, m: int, n: int) -> List[List[List[int]]]:
        self.paths = list()
        if m < 0 or n < 0:
            return self.paths

        def helper(curr_path: List[List[int]]):
            if not curr_path or len(curr_path) == 0:
                return

            cx, cy = curr_path[-1][0], curr_path[-1][1]

            if cx > m - 1 or cy > n - 1:
                return
            if cx == m - 1 and cy == n - 1:
                self.paths.append(curr_path)
                return

            if cx < m - 1:
                down = curr_path.copy()
                down.append([cx + 1, cy])
                helper(down)

            if cy < n - 1:
                right = curr_path.copy()
                right.append([cx, cy + 1])
                helper(right)

        helper([[0, 0]])
        return self.paths


# print(Solution().getAllPaths(3, 2))
#[[[0, 0], [1, 0], [2, 0], [2, 1]], [[0, 0], [1, 0], [1, 1], [2, 1]], [[0, 0], [0, 1], [1, 1], [2, 1]]]
print(Solution().getAllPaths(4, 3))
print(Solution().getAllPaths(5, 2))
print('Tests Passed!!')
