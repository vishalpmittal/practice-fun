"""
    Tag: array, recursive

    Given a nested list of integers, return the sum of all integers in the list weighted by their depth.
    Each element is either an integer, or a list -- whose elements may also be integers or other lists.

    Example 1: Input: [[1,1],2,[1,1]]
    Output: 10,  Explanation: Four 1's at depth 2, one 2 at depth 1.

    Example 2:
    Input: [1,[4,[6]]]
    Output: 27, Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27.
"""

from typing import List, NestedInteger


class Solution:
    """
    :type nestedList: List[NestedInteger]
    :rtype: int
    """

    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def depthsum(nestedList: List[NestedInteger], level):
            if nestedList is None:
                return 0
            for n in nestedList:
                if n.isInteger():
                    self.res += (level + 1) * n.getInteger()
                else:
                    depthsum(n.getList(), level + 1)

        self.res = 0
        depthsum(nestedList, 0)
        return self.res


assert Solution().depthSum([1, [4, [6]]]) == 27
print("Tests Passed!!")
