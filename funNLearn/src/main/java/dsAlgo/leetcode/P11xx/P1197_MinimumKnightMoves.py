"""
    tag: matrix, dp, recursion, game, memoization

    In an infinite chess board with coordinates from -infinity to +infinity, 
    you have a knight at square [0, 0].

    A knight has 8 possible moves it can make, as illustrated below. Each move 
    is two squares in a cardinal direction, then one square in an orthogonal direction.

    Return the minimum number of steps needed to move the knight to the 
    square [x, y].  It is guaranteed the answer exists.

    Example 1: x = 2, y = 1, Output: 1
    Explanation: [0, 0] → [2, 1]

    Example 2: x = 5, y = 5, Output: 4
    Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
 
    Constraints: |x| + |y| <= 300
"""


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        cache = {(0, 0): 0, (1, 0): 3, (0, 1): 3}

        def dfs(x, y):
            if (x, y) in cache:
                return cache[(x, y)]
            res = min(dfs(abs(x - 1), abs(y - 2)), dfs(abs(x - 2), abs(y - 1))) + 1
            cache[(x, y)] = res
            return res

        return dfs(abs(x), abs(y))


assert Solution().minKnightMoves(5, 5) == 4
print("Tests Passed!")
