"""
    Tag: matrix

    We are given a matrix with R rows and C columns has cells with 
    integer coordinates (r, c), where 0 <= r < R and 0 <= c < C.
    Additionally, we are given a cell in that matrix with coordinates (r0, c0).

    Return the coordinates of all cells in the matrix, sorted by 
    their distance from (r0, c0) from smallest distance to largest distance.  
    Here, the distance between two cells (r1, c1) and (r2, c2) is the 
    Manhattan distance, |r1 - r2| + |c1 - c2|.  
    (You may return the answer in any order that satisfies this condition.)

    Example 1: Input: R = 1, C = 2, r0 = 0, c0 = 0 Output: [[0,0],[0,1]]
    Explanation: The distances from (r0, c0) to other cells are: [0,1]

    Example 2: Input: R = 2, C = 2, r0 = 0, c0 = 1 Output: [[0,1],[0,0],[1,1],[1,0]]
    Explanation: The distances from (r0, c0) to other cells are: [0,1,1,2]
    The answer [[0,1],[1,1],[0,0],[1,0]] would also be accepted as correct.

    Example 3: Input: R = 2, C = 3, r0 = 1, c0 = 2 Output: [[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
    Explanation: The distances from (r0, c0) to other cells are: [0,1,1,2,2,3]
    There are other answers that would also be accepted as correct, 
    such as [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]].

    Note:
    -  1 <= R <= 100
    -  1 <= C <= 100
    -  0 <= r0 < R
    -  0 <= c0 < C
"""
from typing import List


class Solution:
    def allCellsDistOrder_0(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        # Slow method. Find the distance for each coordinate and then sort and then add
        dist = [[abs(r-r0)+abs(c-c0), r, c]
                for r in range(R) for c in range(C)]
        dist.sort()
        return [[item[1], item[2]] for item in dist]

    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        # faster bfs solution. Start at the r0,c0 index and spawn out
        bfs, res, seen = [[r0, c0]], [], {(r0, c0)}
        while bfs:
            res += bfs
            new = []
            for i, j in bfs:
                for x, y in (i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1):
                    if 0 <= x < R and 0 <= y < C and (x, y) not in seen:
                        seen.add((x, y))
                        new.append([x, y])
            bfs = new
        return res


assert Solution().allCellsDistOrder(R=1, C=2, r0=0, c0=0) == [[0, 0], [0, 1]]
assert Solution().allCellsDistOrder(R=2, C=2, r0=0, c0=1) == [
    [0, 1], [0, 0], [1, 1], [1, 0]]
assert Solution().allCellsDistOrder(R=2, C=3, r0=1, c0=2) == [
    [1, 2], [0, 2], [1, 1], [0, 1], [1, 0], [0, 0]]
print('Tests Passed!!')
