"""
    Tag: matrix, array, math

    On a N * N grid, we place some 1 * 1 * 1 cubes.
    Each value v = grid[i][j] represents a tower of v cubes 
    placed on top of grid cell (i, j).

    Return the total surface area of the resulting shapes.

    Ex1: Input: [[2]] Output: 10
    Ex2: Input: [[1,2],[3,4]] Output: 34
    Ex3: Input: [[1,0],[0,2]] Output: 16
    Ex4: Input: [[1,1,1],[1,0,1],[1,1,1]] Output: 32
    Ex5: Input: [[2,2,2],[2,1,2],[2,2,2]] Output: 46

    Note:
    -  1 <= N <= 50
    -  0 <= grid[i][j] <= 50
"""
from typing import List


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        N = len(grid)

        ans = 0
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    ans += 2
                    for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                        if 0 <= nr < N and 0 <= nc < N:
                            nval = grid[nr][nc]
                        else:
                            nval = 0

                        ans += max(grid[r][c] - nval, 0)
        return ans


assert Solution().surfaceArea([[2]]) == 10
assert Solution().surfaceArea([[1, 2], [3, 4]]) == 34
assert Solution().surfaceArea([[1, 0], [0, 2]]) == 16
assert Solution().surfaceArea([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == 32
assert Solution().surfaceArea([[2, 2, 2], [2, 1, 2], [2, 2, 2]]) == 46

print('Tests Passed!!')
