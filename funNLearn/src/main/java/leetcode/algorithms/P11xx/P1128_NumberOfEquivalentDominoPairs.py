"""
    Tag: array, game, math

    Given a list of dominoes, dominoes[i] = [a, b] is equivalent 
    to dominoes[j] = [c, d] if and only if either (a==c and b==d), 
    or (a==d and b==c) - that is, one domino can be rotated to be 
    equal to another domino.

    Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, 
    and dominoes[i] is equivalent to dominoes[j].

    Example 1: Input: dominoes = [[1,2],[2,1],[3,4],[5,6]] Output: 1

    Constraints:
    -  1 <= dominoes.length <= 40000
    -  1 <= dominoes[i][j] <= 9
"""
from typing import List
import collections


class Solution:
    def numEquivDominoPairs(self, D: List[List[int]]) -> int:
        # count of pairs are always n*(n-1) / 2
        for i, x in enumerate(D):
            D[i] = min(x[0], x[1]) * 10 + max(x[0], x[1])

        return sum([(v * (v-1))//2 for v in collections.Counter(D).values()])


assert Solution().numEquivDominoPairs([[1, 2], [2, 1], [3, 4], [5, 6]]) == 1
assert Solution().numEquivDominoPairs(
    [[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]) == 3
print('Tests Passed!!')
