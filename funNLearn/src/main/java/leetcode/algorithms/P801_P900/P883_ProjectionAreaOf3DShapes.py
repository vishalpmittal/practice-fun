"""
    Tag: matrix, array, math

    On a N * N grid, we place some 1 * 1 * 1 cubes that are 
    axis-aligned with the x, y, and z axes.

    Each value v = grid[i][j] represents a tower of v cubes placed on 
    top of grid cell (i, j). Now we view the projection of these cubes 
    onto the xy, yz, and zx planes. A projection is like a shadow, that 
    maps our 3 dimensional figure to a 2 dimensional plane. 
    Here, we are viewing the "shadow" when looking at the cubes 
    from the top, the front, and the side.

    Return the total area of all three projections.

    Example 1: Input: [[2]] Output: 5
    Example 2: Input: [[1,2],[3,4]] Output: 17
    Explanation: 
    Here are the three projections ("shadows") of the shape made 
    with each axis-aligned plane.

    Example 3: Input: [[1,0],[0,2]] Output: 8
    Example 4: Input: [[1,1,1],[1,0,1],[1,1,1]] Output: 14
    Example 5: Input: [[2,2,2],[2,1,2],[2,2,2]] Output: 21
    
    Note:
    -  1 <= grid.length = grid[0].length <= 50
    -  0 <= grid[i][j] <= 50

    Approach:
    -  From the top, the shadow made by the shape will be 1 square 
       for each non-zero value.
    -  From the side, the shadow made by the shape will be the 
       largest value for each row in the grid.
    -  From the front, the shadow made by the shape will be the 
       largest value for each column in the grid.
"""
from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        N = len(grid)
        ans = 0

        for i in range(N):
            best_row = 0  # max of grid[i][j]
            best_col = 0  # max of grid[j][i]
            for j in range(N):
                if grid[i][j]:
                    ans += 1  # top shadow
                best_row = max(best_row, grid[i][j])
                best_col = max(best_col, grid[j][i])
            ans += best_row + best_col

        return ans


assert Solution().projectionArea([[2]]) == 5
assert Solution().projectionArea([[1, 2], [3, 4]]) == 17
assert Solution().projectionArea([[1, 0], [0, 2]]) == 8
assert Solution().projectionArea([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == 14
assert Solution().projectionArea([[2, 2, 2], [2, 1, 2], [2, 2, 2]]) == 21
print('Tests Passed!!')
