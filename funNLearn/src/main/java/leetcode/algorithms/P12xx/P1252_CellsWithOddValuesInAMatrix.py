"""
    Tag: matrix

    Given n and m which are the dimensions of a matrix initialized 
    by zeros and given an array indices where indices[i] = [ri, ci]. 
    For each pair of [ri, ci] you have to increment all cells in 
    row ri and column ci by 1.

    Return the number of cells with odd values in the matrix after 
    applying the increment to all indices.

    Example 1: Input: n = 2, m = 3, indices = [[0,1],[1,1]] Output: 6
    Explanation: Initial matrix = [[0,0,0],[0,0,0]].
    After applying first increment it becomes [[1,2,1],[0,1,0]].
    The final matrix will be [[1,3,1],[1,3,1]] which contains 6 odd numbers.

    Example 2: Input: n = 2, m = 2, indices = [[1,1],[0,0]] Output: 0
    Explanation: Final matrix = [[2,2],[2,2]]. There is no odd number 
    in the final matrix.

    Constraints:
    -  1 <= n <= 50
    -  1 <= m <= 50
    -  1 <= indices.length <= 100
    -  0 <= indices[i][0] < n
    -  0 <= indices[i][1] < m
"""
from typing import List


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        def st(a, b):
            return str(a) + '_' + str(b)
        D = {}
        for i, j in indices:
            for x in range(n):
                D[st(x, j)] = D.get(st(x, j), 0) + 1
            for y in range(m):
                D[st(i, y)] = D.get(st(i, y), 0) + 1
        return sum([v % 2 != 0 for v in D.values()])

    def oddCells_matrix(self, n: int, m: int, indices: List[List[int]]) -> int:
        D = [[0 for _ in range(m)] for _ in range(n)]
        for i, j in indices:
            for x in range(n):
                D[x][j] = D[x][j] + 1
            for y in range(m):
                D[i][y] = D[i][y] + 1
        return sum([D[i][j] % 2 != 0 for i in range(n) for j in range(m)])


assert Solution().oddCells_matrix(n=2, m=3, indices=[[0, 1], [1, 1]]) == 6
assert Solution().oddCells_matrix(n=2, m=2, indices=[[1, 1], [0, 0]]) == 0
print('Tests Passed!!')