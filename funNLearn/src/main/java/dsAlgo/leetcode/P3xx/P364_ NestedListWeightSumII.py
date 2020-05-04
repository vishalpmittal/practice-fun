"""
    tag: list, recursive

    Given a nested list of integers, return the sum of all integers in the 
    list weighted by their depth.

    Each element is either an integer, or a list -- whose elements may 
    also be integers or other lists.

    Different from the previous question where weight is increasing from root 
    to leaf, now the weight is defined from bottom up. i.e., the leaf level 
    integers have weight 1, and the root level integers have the largest weight.

    Example 1: [[1,1],2,[1,1]]
    Output: 8 
    Explanation: Four 1's at depth 1, one 2 at depth 2.

    Example 2: [1,[4,[6]]]
    Output: 17 
    Explanation: One 1 at depth 3, one 4 at depth 2, and one 6 at 
    depth 1; 1*3 + 4*2 + 6*1 = 17.

"""
from typing import List


class Solution:
    def depthSumInverse(self, nestedList) -> int:
        dsd = {0: 0}
        global total_levels
        total_levels = 0

        def dsi(nl, level) -> int:
            global total_levels
            if not nl:
                return

            total_levels = max(level + 1, total_levels)

            for x in nl:
                if isinstance(x, int):
                    dsd[level] = dsd.get(level, 0) + x
                else:
                    dsi(x, level + 1)

        dsi(nestedList, 0)
        print(dsd)
        return sum([(total_levels - l) * s for l, s in dsd.items()])


assert Solution().depthSumInverse([[1, 1], 2, [1, 1]]) == 8
assert Solution().depthSumInverse([1, [4, [6]]]) == 17
print("Tests Passed!!!")
