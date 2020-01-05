"""
    Tag: string

    Given two strings S and T, return if they are equal when both are typed 
    into empty text editors. # means a backspace character.

    Example 1: Input: S = "ab#c", T = "ad#c" Output: true
    Explanation: Both S and T become "ac".

    Example 2: Input: S = "ab##", T = "c#d#" Output: true
    Explanation: Both S and T become "".

    Example 3: Input: S = "a##c", T = "#a#c" Output: true
    Explanation: Both S and T become "c".

    Example 4: Input: S = "a#c", T = "b" Output: false
    Explanation: S becomes "c" while T becomes "b".

    Note:
    -  1 <= S.length <= 200
    -  1 <= T.length <= 200
    -  S and T only contain lowercase letters and '#' characters.

    Follow up: Can you solve it in O(N) time and O(1) space?
"""
from typing import List


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def build(S: str) -> bool:
            ans = []
            for c in S:
                if c != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)
        return build(S) == build(T)

    def backspaceCompare_1(self, S: str, T: str) -> bool:
        def F(S: str):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.izip_longest(F(S), F(T)))


assert Solution().backspaceCompare(S="ab#c", T="ad#c")
assert Solution().backspaceCompare(S="ab##", T="c#d#")
assert Solution().backspaceCompare(S="a##c", T="#a#c")
assert not Solution().backspaceCompare(S="a#c", T="b")
print('Tests Passed!!')
