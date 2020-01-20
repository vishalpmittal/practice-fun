"""
    Tag: string

    We are given two strings, A and B.
    A shift on A consists of taking string A and moving the leftmost character
    to the rightmost position. For example, if A = 'abcde', then it will be
    'bcdea' after one shift on A. Return True if and only if A can become B
    after some number of shifts on A.

    Example 1: Input: A = 'abcde', B = 'cdeab'  Output: true
    Example 2: Input: A = 'abcde', B = 'abced' Output: false

    Note: A and B will have length at most 100.
"""
from typing import List
from collections import Counter


class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        # For each rotation of A, let's check if it equals B
        if len(A) != len(B):
            return False
        if len(A) == 0:
            return True
        for s in range(len(A)):
            if all(A[(s+i) % len(A)] == B[i] for i in range(len(A))):
                return True
        return False

    def rotateString_1(self, A: str, B: str) -> bool:
        # if B is in A+A
        return len(A) == len(B) and B in A+A

    def rotateString_2(self, A: str, B: str) -> bool:
        # save each char pair count in dictionary and then compare
        # eg: A=abcde then d= {'ab': 1, 'bc': 1, 'cd': 1, 'de': 1, 'ea': 1}
        if len(A) != len(B):
            return False
        if len(A) == 0:
            return True

        A, B, d = A+A[0], B+B[0], {}
        for i in range(0, len(A)-1):
            ss = A[i]+''+A[i+1]
            d[ss] = 1 if ss not in d else d[ss] + 1

        for j in range(0, len(B)-1):
            ss = B[j] + '' + B[j+1]
            if ss not in d:
                return False
            d[ss] -= 1
            if d[ss] == 0:
                del d[ss]
        return d == {}


assert Solution().rotateString_2('abcde', 'cdeab')
assert not Solution().rotateString_2('abcde', 'cdeba')
assert Solution().rotateString_2("clrwmpkwru", "wmpkwruclr")
print('Tests Passed!!')
