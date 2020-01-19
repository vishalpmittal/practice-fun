"""
    Tag: matrix

    Given a 2D grid of size m x n and an integer k. 
    You need to shift the grid k times.

    In one shift operation:
    -  Element at grid[i][j] moves to grid[i][j + 1].
    -  Element at grid[i][n - 1] moves to grid[i + 1][0].
    -  Element at grid[m - 1][n - 1] moves to grid[0][0].

    Return the 2D grid after applying shift operation k times.

    Example 1: Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1 
    Output: [[9,1,2],[3,4,5],[6,7,8]]

    Example 2: Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
    Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]

    Example 3: Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
    Output: [[1,2,3],[4,5,6],[7,8,9]]

    Constraints:
    -  m == grid.length
    -  n == grid[i].length
    -  1 <= m <= 50
    -  1 <= n <= 50
    -  -1000 <= grid[i][j] <= 1000
    -  0 <= k <= 100
"""
from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        self.x, self.y = 0, -1

        def get_next():
            self.y = self.y+1
            if self.y >= n:
                self.x, self.y = self.x+1, 0
            if self.x >= m:
                self.x, self.y = 0, 0
            return self.x, self.y

        # in order traversed grid
        iotg = [grid[i][j] for i in range(m) for j in range(n)]
        for _ in range(k):
            iotg.insert(0, iotg.pop())

        for v in iotg:
            i, j = get_next()
            grid[i][j] = v

        return grid

    def shiftGrid_faster(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        self.x, self.y = 0, -1

        def get_next():
            self.y = self.y+1
            if self.y >= n:
                self.x, self.y = self.x+1, 0
            if self.x >= m:
                self.x, self.y = 0, 0
            return self.x, self.y

        wq = []
        for _ in range(k):
            i, j = get_next()
            wq.insert(0, grid[i][j])

        for _ in range(m*n):
            i, j = get_next()
            wq.insert(0, grid[i][j])
            grid[i][j] = wq.pop()

        return grid


assert Solution().shiftGrid_faster([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1) == [
    [9, 1, 2], [3, 4, 5], [6, 7, 8]]
print('Tests Passed!!')
