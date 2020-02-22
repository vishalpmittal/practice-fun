"""
    Tag: string, array

    Given a string S of lowercase letters, a duplicate removal consists of 
    choosing two adjacent and equal letters, and removing them.
    We repeatedly make duplicate removals on S until we no longer can.

    Return the final string after all such duplicate removals have been 
    made.  It is guaranteed the answer is unique.

    Example 1: Input: "abbaca" Output: "ca"
    Explanation:  For example, in "abbaca" we could remove "bb" since the 
    letters are adjacent and equal, and this is the only possible move.  
    The result of this move is that the string is "aaca", of which only 
    "aa" is possible, so the final string is "ca".

    Note:
    -  1 <= S.length <= 20000
    -  S consists only of English lowercase letters.
"""
from typing import List


class Solution:
    def removeDuplicates(self, S: str) -> str:
        # Output limit exceeded on leetcode
        i, L = 0, len(S)-1
        while i < L:
            if S[i] == S[i+1]:
                S = S[:i] + S[i+2:]
                L = len(S)-1
                i = i-1 if i != 0 else 0
            else:
                i += 1
            print(i, S, L)
        return S

    def removeDuplicates_1(self, S: str) -> str:
        # generate 26 possible duplicates
        # {'aa, 'bb', ....}
        # O(n^2)
        duplicates = {2 * ch for ch in ascii_lowercase}

        prev_length = -1
        while prev_length != len(S):
            prev_length = len(S)
            for d in duplicates:
                S = S.replace(d, '')
        return S

    def removeDuplicates_2(self, S: str) -> str:
        # using a stack O(n)
        output = []
        for ch in S:
            if output and ch == output[-1]:
                output.pop()
            else:
                output.append(ch)
        return ''.join(output)


assert Solution().removeDuplicates("abbaca") == 'ca'
print('Tests Passed!!')
