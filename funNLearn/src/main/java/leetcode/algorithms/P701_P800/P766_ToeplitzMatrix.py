"""
    Tag: matrix

    A matrix is Toeplitz if every diagonal from top-left to bottom-right 
    has the same element.
    Now given an M x N matrix, return True if and only if the matrix is Toeplitz.

    Example 1:Input:       Output: True
            matrix = [
            [1,2,3,4],
            [5,1,2,3],
            [9,5,1,2]
            ]
    Explanation: In the above grid, the diagonals are:
    "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
    In each diagonal all elements are the same, so the answer is True.

    Example 2: Input:      Output: False
            matrix = [
            [1,2],
            [2,2]
            ]
    Explanation: The diagonal "[1, 2]" has different elements.

    Note:
    -  matrix will be a 2D array of integers.
    -  matrix will have a number of rows and columns in range [1, 20].
    -  matrix[i][j] will be integers in range [0, 99].

    Follow up:
    -  What if the matrix is stored on disk, and the memory is limited such that you 
    can only load at most one row of the matrix into the memory at once?
    -  What if the matrix is so large that you can only load up a partial row 
    into the memory at once?
"""
from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # two coordinates are on the same diagonal if and only if r1 - c1 == r2 - c2.
        groups = {}
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r-c not in groups:
                    groups[r-c] = val
                elif groups[r-c] != val:
                    return False
        return True


assert Solution().isToeplitzMatrix([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]])
assert not Solution().isToeplitzMatrix([[1, 2], [2, 2]])
print('Tests Passed!!')
