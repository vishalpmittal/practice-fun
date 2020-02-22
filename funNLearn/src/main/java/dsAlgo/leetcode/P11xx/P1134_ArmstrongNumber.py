"""
    Tag: integer, math

    The k-digit number N is an Armstrong number if and only 
    if the k-th power of each digit sums to N. Given a positive integer N, 
    return true if and only if it is an Armstrong number.

    Example 1: Input: 153 Output: true
    Explanation: 153 is a 3-digit number, and 153 = 1^3 + 5^3 + 3^3.

    Example 2: Input: 123 Output: false
    Explanation: 123 is a 3-digit number, and 123 != 1^3 + 2^3 + 3^3 = 36.

    Note: 1 <= N <= 10^8
"""
from typing import List


class Solution:
    def isArmstrong(self, N: int) -> bool:
        A = [int(x) for x in str(N)]
        return N == sum([a**len(A) for a in A])


assert Solution().isArmstrong(153)
assert not Solution().isArmstrong(123)
print('Tests Passed!!')
