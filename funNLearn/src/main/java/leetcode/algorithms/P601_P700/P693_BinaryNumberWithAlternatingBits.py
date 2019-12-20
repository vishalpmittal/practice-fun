"""
    Tag: bit

    Given a positive integer, check whether it has alternating bits: 
    namely, if two adjacent bits will always have different values.

    Example 1: Input: 5 Output: True
    Explanation: The binary representation of 5 is: 101

    Example 2: Input: 7 Output: False
    Explanation: The binary representation of 7 is: 111.

    Example 3: Input: 11 Output: False
    Explanation: The binary representation of 11 is: 1011.

    Example 4: Input: 10  Output: True
    Explanation: The binary representation of 10 is: 1010.
"""
from typing import List


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # Convert to string
        bits = bin(n)
        return all(bits[i] != bits[i+1] for i in range(len(bits) - 1))

    def hasAlternatingBits_2(self, n: int) -> bool:
        # Devide by two
        n, cur = divmod(n, 2)
        while n:
            if cur == n % 2:
                return False
            n, cur = divmod(n, 2)
        return True

    def hasAlternatingBits_x(self, n: int) -> bool:
        comp = n & 1
        while n > 0:
            if (n & 1) != comp:
                return False
            # right shift number by 1 digit
            n = n >> 1
            # swap between 0 and 1
            comp = (comp+1) & 1
        return True


assert Solution().hasAlternatingBits_x(5)
assert not Solution().hasAlternatingBits_x(7)
assert Solution().hasAlternatingBits_x(10)
assert not Solution().hasAlternatingBits_x(11)
print('Tests Passed!!')
