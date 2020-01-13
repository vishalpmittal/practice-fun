"""
    Tag: array, integer, game

    Three stones are on a number line at positions a, b, and c.
    Each turn, you pick up a stone at an endpoint (ie., either 
    the lowest or highest position stone), and move it to an 
    unoccupied position between those endpoints.  Formally, let's 
    say the stones are currently at positions x, y, z with x < y < z.
    You pick up the stone at either position x or position z, and move 
    that stone to an integer position k, with x < k < z and k != y.

    The game ends when you cannot make any more moves, 
    ie. the stones are in consecutive positions.

    When the game ends, what is the minimum and maximum number of 
    moves that you could have made?  Return the answer as an 
    length 2 array: answer = [minimum_moves, maximum_moves]

    Example 1: Input: a = 1, b = 2, c = 5 Output: [1,2]
    Explanation: Move the stone from 5 to 3, or move the stone from 5 to 4 to 3.

    Example 2: Input: a = 4, b = 3, c = 2 Output: [0,0]
    Explanation: We cannot make any moves.

    Example 3: Input: a = 3, b = 5, c = 1 Output: [1,2]
    Explanation: Move the stone from 1 to 4; or move the stone from 1 to 2 to 4.
    
    Note:
    -  1 <= a <= 100
    -  1 <= b <= 100
    -  1 <= c <= 100
    -  a != b, b != c, c != a

    Approach:
    The maximum number of moves would be the total number of empty 
    spots between the stones.

    The minimum number of moves can be obtained by analyzing the following 4 cases:
    -  If the number of empty spots between any one of the pairs of 
    successive stones is 1, e.g. [1, 3, 5], and [3, 5, 10], then 
    only 1 move is required which fills the empty spot between the
    pair of stones.
    -  If there are no empty spots between both the successive pair of 
    stones, e.g. [1, 2, 3], then no move is required.
    -  If there is no empty spot between any one of the pairs of successive 
    stones, e.g. [2, 10, 11] or [2, 3, 10], then only 1 move is required.
    -  For all the other possible configurations, at least 2 moves are 
    required.
"""
from typing import List


class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        stones = sorted([a, b, c])
        max_moves = (stones[1] - stones[0] - 1) + (stones[2] -
                                                   stones[1] - 1)  # points between the stones

        # add cases for min_moves
        if stones[1] - stones[0] == 2 or stones[2] - stones[1] == 2:
            min_moves = 1            # [1, 3, 5]
        elif stones[1] - stones[0] == 1 and stones[2] - stones[1] == 1:
            min_moves = 0             # [1, 2, 3]
        elif stones[1] - stones[0] == 1 or stones[2] - stones[1] == 1:
            min_moves = 1            # [2, 10, 11] or [2, 3, 10]
        else:
            min_moves = 2            # all other cases

        return [min_moves, max_moves]


assert Solution().numMovesStones(1, 2, 5) == [1, 2]
assert Solution().numMovesStones(4, 3, 2) == [0, 0]
assert Solution().numMovesStones(3, 5, 1) == [1, 2]
print('Tests Passed!!')
