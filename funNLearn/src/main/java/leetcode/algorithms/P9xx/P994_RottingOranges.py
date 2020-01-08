"""
    Tag: matrix

    In a given grid, each cell can have one of three values:
    the value 0 representing an empty cell;
    the value 1 representing a fresh orange;
    the value 2 representing a rotten orange.

    Every minute, any fresh orange that is adjacent
    (4-directionally) to a rotten orange becomes rotten.
    Return the minimum number of minutes that must elapse until
    no cell has a fresh orange.
    If this is impossible, return -1 instead.

    Example 1: Input: [[2,1,1],[1,1,0],[0,1,1]] Output: 4

    Example 2: Input: [[2,1,1],[0,1,1],[1,0,1]] Output: -1
    Explanation:  The orange in the bottom left corner (row 2, column 0)
    is never rotten, because rotting only happens 4-directionally.

    Example 3: Input: [[0,2]]
    Output: 0
    Explanation:  Since there are already no fresh oranges at minute 0,
    the answer is just 0.

    Note:
    -  1 <= grid.length <= 10
    -  1 <= grid[0].length <= 10
    -  grid[i][j] is only 0, 1, or 2.
"""
from typing import List
import collections


class Solution:
    def orangesRotting(self, A: List[List[int]]) -> int:
        R, C = len(A), len(A[0])

        # queue - all starting cells with rotting oranges
        queue = collections.deque()
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                if val == 2:
                    queue.append((r, c, 0))

        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        d = 0
        while queue:
            r, c, d = queue.popleft()
            for nr, nc in neighbors(r, c):
                if A[nr][nc] == 1:
                    A[nr][nc] = 2
                    queue.append((nr, nc, d+1))

        if any(1 in row for row in A):
            return -1
        return d


assert Solution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
assert Solution().orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
assert Solution().orangesRotting([[0, 2]]) == 0
print('Tests Passed!!')
