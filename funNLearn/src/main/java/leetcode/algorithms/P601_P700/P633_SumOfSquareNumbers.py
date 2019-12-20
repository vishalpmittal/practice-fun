"""
    Tag: math

    Given a non-negative integer c, your task is to decide whether there're 
    two integers a and b such that a^2 + b^2 = c.

    Example 1:   Input: 5,  Output: True 
    Explanation: 1 * 1 + 2 * 2 = 5
    
    Example 2:   Input: 3   Output: False
"""
from typing import List
import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        src = int(math.sqrt(c)) + 1
        ss = set()
        for i in range(0, src, 1):
            si = i**2
            if c - si in ss or si + si == c:
                return True
            else:
                ss.add(si)
        return False

    def judgeSquareSum_1(self, c: int) -> bool:
        def is_square(N):
            return int(math.sqrt(N))**2 == N

        return any(is_square(c - a*a) for a in range(int(math.sqrt(c)) + 1))


assert Solution().judgeSquareSum(5)
assert Solution().judgeSquareSum(2)
assert not Solution().judgeSquareSum(7)
assert Solution().judgeSquareSum(8)
assert Solution().judgeSquareSum(9)
assert Solution().judgeSquareSum(10)
assert not Solution().judgeSquareSum(11)
print('Tests Passed!!')
