"""
    Tag: math

    The Tribonacci sequence Tn is defined as follows: 
    T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
    Given n, return the value of Tn.

    Example 1: Input: n = 4 Output: 4
    Explanation: 
    T_3 = 0 + 1 + 1 = 2 
    T_4 = 1 + 1 + 2 = 4

    Example 2: Input: n = 25 Output: 1389537

    Constraints:
    -  0 <= n <= 37
    -  The answer is guaranteed to fit within a 32-bit integer, 
    ie. answer <= 2^31 - 1.
"""
from typing import List


class Solution:
    def tribonacci(self, n: int) -> int:
        a = [0, 1, 1]
        if n < 3:
            return a[n]
        c, s = 2, 0
        while c < n:
            s = sum(a)
            a[0], a[1], a[2] = a[1], a[2], s
            c += 1
        return s

    def tribonacci_1(self, n):
        a, b, c = 1, 0, 0
        for _ in range(n):
            a, b, c = b, c, a + b + c
        return c


assert Solution().tribonacci(4) == 4
assert Solution().tribonacci_1(25) == 1389537
print('Tests Passed!!')
