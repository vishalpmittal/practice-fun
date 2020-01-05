"""
    Tag: array, integer

    An array is monotonic if it is either monotone increasing or monotone decreasing.

    An array A is monotone increasing if for all i <= j, A[i] <= A[j].  
    An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

    Return true if and only if the given array A is monotonic.

    Ex 1: Ip: [1,2,2,3]     Op: true
    Ex 2: Ip: [6,5,4,4]     Op: true
    Ex 3: Ip: [1,3,2]     Op: false
    Ex 4: Ip: [1,2,4,5]     Op: true
    Ex 5: Ip: [1,1,1]     Op: true
    
    Note:
    -  1 <= A.length <= 50000
    -  -100000 <= A[i] <= 100000
"""
from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        # Slower two pass
        return all([A[i] <= A[i+1] for i in range(len(A)-1)]) or all([A[i] >= A[i+1] for i in range(len(A)-1)])

    def isMonotonic_1(self, A: List[int]) -> bool:
        # Faster One Pass
        increasing = decreasing = True

        for i in xrange(len(A) - 1):
            if A[i] > A[i+1]:
                increasing = False
            if A[i] < A[i+1]:
                decreasing = False

        return increasing or decreasing


assert Solution().isMonotonic([1, 2, 2, 3])
assert Solution().isMonotonic([6, 5, 4, 4])
assert not Solution().isMonotonic([1, 3, 2])
assert Solution().isMonotonic([1, 2, 4, 5])
assert Solution().isMonotonic([1, 1, 1])
print('Tests Passed!!')
