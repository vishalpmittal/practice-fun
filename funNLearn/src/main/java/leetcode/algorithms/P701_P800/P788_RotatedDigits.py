"""
    Tag: array, integer

    X is a good number if after rotating each digit individually by 180 degrees,
    we get a valid number that is different from X.  Each digit must be rotated
    - we cannot choose to leave it alone.

    A number is valid if each digit remains a digit after rotation. 0, 1, and 8
    rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other,
    and the rest of the numbers do not rotate to any other number and become invalid.

    Now given a positive number N, how many numbers X from 1 to N are good?

    Example: Input: 10 Output: 4
    Explanation:  There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
    Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.

    Note: N  will be in range [1, 10000].
"""
from typing import List


class Solution:
    def rotatedDigits(self, N: int) -> int:
        """
            Rotation means rotating digits clockwise, eg. 21958 after rotation is 51628
            since 0, 1 and 8 rotate to themselves, numbers that contains only those digits
            are will remain same even after rotation.
            rd = {0: 0, 1: 1, 2: 5, 5: 2, 6: 9, 8: 8, 9: 6}

            For each X from 1 to N, let's analyze whether X is good.
            -  If X has a digit that does not have a valid rotation (3, 4, or 7),
            then it can't be good.
            -  If X doesn't have a digit that rotates to a different digit (2, 5, 6, or 9),
            it can't be good because X will be the same after rotation.
            -  Otherwise, X will successfully rotate to a valid different number.
        """
        ans = 0
        # For each x in [1, N], check whether it's good
        for x in range(1, N+1):
            S = str(x)
            # Each x has only rotateable digits, and one of them
            # rotates to a different digit
            ans += (all(d not in '347' for d in S)
                    and any(d in '2569' for d in S))
        return ans


assert Solution().rotatedDigits(10) == 4
print('Tests Passed!!')
