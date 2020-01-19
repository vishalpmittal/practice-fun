"""
    Tag: TO-DO, string, dp, array, integer, bit, linked list
    Tag: tree, sort, math, matrix, regex, recursive
    Tag: design ds (design data structure), dfs, binary search, algo, game

    Balanced strings are those who have equal quantity of 'L' and 'R' characters.
    Given a balanced string s split it in the maximum amount of balanced strings.
    Return the maximum amount of splitted balanced strings.

    Example 1: Input: s = "RLRRLLRLRL" Output: 4
    Explanation: s can be split into "RL", "RRLL", "RL", "RL", each 
    substring contains same number of 'L' and 'R'.

    Example 2: Input: s = "RLLLLRRRLR" Output: 3
    Explanation: s can be split into "RL", "LLLRRR", "LR", each 
    substring contains same number of 'L' and 'R'.

    Example 3: Input: s = "LLLLRRRR" Output: 1 
    Explanation: s can be split into "LLLLRRRR".

    Example 4: Input: s = "RLRRRLLRLL" Output: 2
    Explanation: s can be split into "RL", "RRRLLRLL", since 
    each substring contains an equal number of 'L' and 'R'
    
    Constraints:
    -  1 <= s.length <= 1000
    -  s[i] = 'L' or 'R'
"""
from typing import List


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        C, ans = {'R': 1, 'L': -1}, 0
        c = C[s[0]]
        for x in s[1:]:
            c += C[x]
            if c == 0:
                ans += 1
        return ans

    def balancedStringSplit_1liner(self, s: str) -> int:
        return list(acc(1 if c == 'L' else -1 for c in s)).count(0)


assert Solution().balancedStringSplit("RLRRLLRLRL") == 4
assert Solution().balancedStringSplit("RLLLLRRRLR") == 3
assert Solution().balancedStringSplit("LLLLRRRR") == 1
assert Solution().balancedStringSplit("RLRRRLLRLL") == 2
print('Tests Passed!!')
