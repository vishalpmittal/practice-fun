"""
    Tag: array, integer

    There are some chips, and the i-th chip is at position chips[i].
    You can perform any of the two following types of moves any number 
    of times (possibly zero) on any chip:
    -  Move the i-th chip by 2 units to the left or to the right with a cost of 0.
    -  Move the i-th chip by 1 unit to the left or to the right with a cost of 1.
    There can be two or more chips at the same position initially.

    Return the minimum cost needed to move all the chips to the same 
    position (any position).

    Example 1: Input: chips = [1,2,3] Output: 1
    Explanation: Second chip will be moved to positon 3 with cost 1. 
    First chip will be moved to position 3 with cost 0. Total cost is 1.

    Example 2: Input: chips = [2,2,2,3,3] Output: 2
    Explanation: Both fourth and fifth chip will be moved to position 
    two with cost 1. Total minimum cost will be 2.
    
    Constraints:
    -  1 <= chips.length <= 100
    -  1 <= chips[i] <= 10^9

    Approach by Hai_dee on leetcode:
    The key observation here is that it's free to move a chip from 
    an even number to another even number, and it is free to move a chip 
    from an odd number to another odd number. It only costs to move an 
    even to an odd, or an odd to an even. 
    Therefore, we want to minimise such moves.

    All chips must be on the same position once we're done, which is 
    either even or odd. Therefore, we want to calculate whether it is 
    cheaper to move all the odd chips to even or all the even chips 
    to odd. This will simply come down to how many even chips we start 
    with, and how many odd chips. Each chip that has to be moved will 
    cost exactly 1.

    To determine the cost, we need to count how many are even, and how 
    many are odd, and then take the minimum of these two values.

    The cost is O(n) because we are looking at each chip in 
    isolation, and we are using O(1) extra space because we only have 
    a few variables to keep the counts in.
"""
from typing import List


class Solution:

    def minCostToMoveChips(self, chips: List[int]) -> int:
        even_parity = 0
        odd_parity = 0
        for chip in chips:
            if chip % 2 == 0:
                even_parity += 1
            else:
                odd_parity += 1
        return min(even_parity, odd_parity)

    def minCostToMoveChips_shorter(self, chips: List[int]) -> int:
        odds = sum(x % 2 for x in chips)
        return min(odds, len(chips) - odds)


assert Solution().minCostToMoveChips([1, 2, 3]) == 1
assert Solution().minCostToMoveChips([2, 2, 2, 3, 3]) == 2
print('Tests Passed!!')
