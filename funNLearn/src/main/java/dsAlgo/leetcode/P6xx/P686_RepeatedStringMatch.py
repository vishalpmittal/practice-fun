"""
    Tag: string

    Given two strings A and B, find the minimum number of times A has to 
    be repeated such that B is a substring of it. If no such solution, return -1.

    For example, with A = "abcd" and B = "cdabcdab".
    Return 3, because by repeating A three times (“abcdabcdabcd”), B is a 
    substring of it; and B is not a substring of A repeated two times ("abcdabcd").

    Note:
    The length of A and B will be between 1 and 10000.
"""
from typing import List


class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        q = (len(B) - 1) // len(A) + 1
        for i in range(2):
            if B in A * (q+i):
                return q+i
        return -1


assert Solution().repeatedStringMatch("abcd", "cdabcdab") == 3
print('Tests Passed!!')
