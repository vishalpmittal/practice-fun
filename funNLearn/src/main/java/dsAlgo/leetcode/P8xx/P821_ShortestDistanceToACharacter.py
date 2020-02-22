"""
    Tag: array

    Given a string S and a character C, return an array of integers
    representing the shortest distance from the character C in the string.

    Example 1: Input: S = "loveleetcode", C = 'e'
    Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

    Note:
    -  S string length is in [1, 10000].
    -  C is a single character, and guaranteed to be in string S.
    -  All letters in S and C are lowercase.
"""
from typing import List


class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        # iterate once and get all C's locations in a set
        # iterate over string again and find min for all C's positions
        ans = []
        c_pos = {i for i in range(len(S)) if S[i] == C}
        for si in range(len(S)):
            ans.append(min([abs(si - p) for p in c_pos]))
        return ans

    def shortestToChar(self, S: str, C: str) -> List[int]:
        # iterate left to right once and remember the distance from nearest left C
        # iterate from right to left and remember the distance from nearest right C
        # answer is the min of the two.
        prev = float('-inf')
        ans = []
        for i, x in enumerate(S):
            if x == C:
                prev = i
            ans.append(i - prev)

        prev = float('inf')
        for i in range(len(S) - 1, -1, -1):
            if S[i] == C:
                prev = i
            ans[i] = min(ans[i], prev - i)

        return ans


assert Solution().shortestToChar(S="loveleetcode", C='e') == [
    3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
print('Tests Passed!!')
