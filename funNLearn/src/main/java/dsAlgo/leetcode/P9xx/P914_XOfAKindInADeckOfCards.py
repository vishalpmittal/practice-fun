"""
    Tag: array, math

    In a deck of cards, each card has an integer written on it.
    Return true if and only if you can choose X >= 2 such that it is 
    possible to split the entire deck into 1 or more groups of cards, where:
    Each group has exactly X cards.
    All the cards in each group have the same integer.
    
    Example 1: Input: [1,2,3,4,4,3,2,1] Output: true
    Explanation: Possible partition [1,1],[2,2],[3,3],[4,4]

    Example 2: Input: [1,1,1,2,2,2,3,3] Output: false
    Explanation: No possible partition.

    Example 3: Input: [1] Output: false
    Explanation: No possible partition.

    Example 4: Input: [1,1] Output: true
    Explanation: Possible partition [1,1]

    Example 5: Input: [1,1,2,2,2,2] Output: true
    Explanation: Possible partition [1,1],[2,2],[2,2]

    Note:
    -  1 <= deck.length <= 10000
    -  0 <= deck[i] < 10000
"""
from typing import List
import collections
from math import gcd
from functools import reduce


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        # dividing N cards into K piles of X cards each, thus N%K == 0
        # Each type of card count should also be C % K == 0
        count = collections.Counter(deck)
        N = len(deck)
        for X in range(2, N+1):
            if N % X == 0:
                if all(v % X == 0 for v in count.values()):
                    return True
        return False

    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        # Greatest common divisor
        vals = collections.Counter(deck).values()
        return reduce(gcd, vals) >= 2


assert Solution().hasGroupsSizeX([1, 2, 3, 4, 4, 3, 2, 1])
assert not Solution().hasGroupsSizeX([1, 1, 1, 2, 2, 2, 3, 3])
assert not Solution().hasGroupsSizeX([1])
assert Solution().hasGroupsSizeX([1, 1])
assert Solution().hasGroupsSizeX([1, 1, 2, 2, 2, 2])
print('Tests Passed!!')
