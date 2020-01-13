"""
    Tag: integer

    Given a year Y and a month M, return how many days there are 
    in that month.

    Ex1: I: Y = 1992, M = 7; O: 31
    Ex2: I: Y = 2000, M = 2; O: 29
    Ex3: I: Y = 1900, M = 2; O: 28

    Note:
    -  1583 <= Y <= 2100
    -  1 <= M <= 12
"""
from typing import List


class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:
        C = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
             7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        LY = (Y % 400 == 0) or (Y % 4 == 0 and Y % 100 != 0)
        return 29 if M == 2 and LY else C[M]

    def numberOfDays_1(self, Y: int, M: int) -> int:
        # Faster and more logical
        if M in {1, 3, 5, 7, 8, 10, 12}:
            return 31
        elif M != 2:
            return 30
        else:
            return 28 + (Y % 4 == 0 and Y % 100 != 0 or Y % 400 == 0)


assert Solution().numberOfDays(1992, 7) == 31
assert Solution().numberOfDays(2000, 2) == 29
assert Solution().numberOfDays(1900, 2) == 28
print('Tests Passed!!')
