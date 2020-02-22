"""
    Tag: array, bit

    Given an array A of 0s and 1s, consider N_i: the i-th subarray
    from A[0] to A[i] interpreted as a binary number (from
    most-significant-bit to least-significant-bit.)

    Return a list of booleans answer, where answer[i] is True
    if and only if N_i is divisible by 5.

    Example 1: Input: [0,1,1] Output: [True,False,False]
    Explanation:  The input numbers in binary are 0, 01, 011;
    which are 0, 1, and 3 in base-10.  Only the first number
    is divisible by 5, so answer[0] is True.

    Ex2: Ip: [1,1,1] Output: [False,False,False]
    Ex3: Ip: [0,1,1,1,1,1] Output: [True,False,False,False,True,False]
    Ex4: Ip: [1,1,1,0,1] Output: [False,False,False,False,False]

    Note:
    -  1 <= A.length <= 30000
    -  A[i] is 0 or 1
"""
from typing import List


class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        for i in range(1, len(A)):
            A[i] += A[i - 1] * 2
        return [x % 5 == 0 for x in A]

    def prefixesDivBy5_1(self, A: List[int]) -> List[bool]:
        # same as above but more efficient as we are only storing
        # reminders now
        for i in range(1, len(A)):
            A[i] += A[i - 1] * 2 % 5
        return [x % 5 == 0 for x in A]


assert Solution().prefixesDivBy5([0, 1, 1]) == [True, False, False]
assert Solution().prefixesDivBy5([1, 1, 1]) == [False, False, False]
assert Solution().prefixesDivBy5([0, 1, 1, 1, 1, 1]) == [
    True, False, False, False, True, False]
assert Solution().prefixesDivBy5([1, 1, 1, 0, 1]) == [
    False, False, False, False, False]
print('Tests Passed!!')
