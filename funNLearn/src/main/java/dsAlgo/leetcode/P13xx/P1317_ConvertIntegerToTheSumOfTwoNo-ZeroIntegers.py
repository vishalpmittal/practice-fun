"""
    Tag: integer

    Given an integer n. No-Zero integer is a positive integer which doesn't 
    contain any 0 in its decimal representation. Return a list of two 
    integers [A, B] where: 
        -  A and B are No-Zero integers.
        -  A + B = n

    It's guarateed that there is at least one valid solution. 
    If there are many valid solutions you can return any of them.

    Ex1: i/p: n = 2; o/p: [1,1]
    Explanation: A = 1, B = 1. A + B = n and both A and B don't contain 
    any 0 in their decimal representation.

    Ex2: i/p: n = 11; o/p: [2,9]
    Ex3: i/p: n = 10000; o/p: [1,9999]
    Ex4: i/p: n = 69; o/p: [1,68]
    Ex5: i/p: n = 1010; o/p: [11,999]

    Constraints:
    -  2 <= n <= 10^4
"""
from typing import List


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for a in range(n):
            if '0' not in f'{a}{n-a}':
                return [a, n-a]


assert Solution().getNoZeroIntegers(2) == [1, 1]
assert Solution().getNoZeroIntegers(11) == [2, 9]
assert Solution().getNoZeroIntegers(10000) == [1, 9999]
assert Solution().getNoZeroIntegers(69) == [1, 68]
assert Solution().getNoZeroIntegers(1010) == [11, 999]
print('Tests Passed!!')
