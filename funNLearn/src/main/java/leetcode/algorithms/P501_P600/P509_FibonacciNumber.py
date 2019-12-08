"""
    Tag: math

    The Fibonacci numbers, commonly denoted F(n) form a sequence, called
    the Fibonacci sequence, such that each number is the sum of the two
    preceding ones, starting from 0 and 1. That is,

    F(0) = 0,   F(1) = 1
    F(N) = F(N - 1) + F(N - 2), for N > 1.

    Given N, calculate F(N).

    Example 1:
    Input: 2 Output: 1
    Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

    Example 2:
    Input: 3 Output: 2
    Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

    Example 3:
    Input: 4 Output: 3
    Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

    Note:
    0 ≤ N ≤ 30.
"""


def fib(N: int) -> int:
    # Recursive
    if N <= 1:
        return N
    return fib(N-1) + fib(N-2)


def fib_1(N: int) -> int:
    # Iterative approach
    if (N <= 1):
        return N
    if (N == 2):
        return 1
    current, prev1, prev2 = 0, 1, 1
    for i in range(3, N+1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    return current


class Solution:
    # Memoize technique
    def fib_2(self, N: int) -> int:
        if N <= 1:
            return N
        self.cache = {0: 0, 1: 1}
        return self.memoize(N)

    def memoize(self, N: int) -> {}:
        if N in self.cache.keys():
            return self.cache[N]
        self.cache[N] = self.memoize(N-1) + self.memoize(N-2)
        return self.memoize(N)


def test_code():
    assert fib(4) == 3
    print("Tests Passed!!")


test_code()
