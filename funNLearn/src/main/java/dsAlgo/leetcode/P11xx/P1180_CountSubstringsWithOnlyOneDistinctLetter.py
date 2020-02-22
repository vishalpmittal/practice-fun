"""
    Tag: string

    Given a string S, return the number of substrings 
    that have only one distinct letter.

    Example 1: Input: S = "aaaba" Output: 8
    Explanation: The substrings with one distinct letter 
    are "aaa", "aa", "a", "b".
    "aaa" occurs 1 time.
    "aa" occurs 2 times.
    "a" occurs 4 times.
    "b" occurs 1 time.
    So the answer is 1 + 2 + 4 + 1 = 8.

    Example 2: Input: S = "aaaaaaaaaa" Output: 55

    Constraints:
    -  1 <= S.length <= 1000
    -  S[i] consists of only lowercase English letters.
"""
from typing import List
from math import factorial as f


class Solution:
    def countLetters_0(self, S: str) -> int:
        rep_ss, cl = [], 1   # repeated substrings, current length
        for i in range(0, len(S)-1):
            if S[i] == S[i+1]:
                cl += 1
            else:
                rep_ss.append(cl)
                cl = 1
        rep_ss.append(cl)

        return sum([n*(n+1)//2 for n in rep_ss])

    def countLetters(self, S: str) -> int:
        total_ss, cl = 0, 1   # total substrings, current length
        for i in range(0, len(S)-1):
            if S[i] == S[i+1]:
                cl += 1
            else:
                total_ss += cl*(cl+1)//2
                cl = 1
        total_ss += cl*(cl+1)//2
        return total_ss


assert Solution().countLetters("aaaba") == 8
assert Solution().countLetters("aaaaaaaaaa") == 55
print('Tests Passed!!')
