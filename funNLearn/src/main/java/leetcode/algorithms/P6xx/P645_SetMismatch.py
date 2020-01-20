"""
    Tag: array, math

    The set S originally contains numbers from 1 to n. 
    But unfortunately, due to the data error, one of the numbers in the 
    set got duplicated to another number in the set, which results in repetition 
    of one number and loss of another number.

    Given an array nums representing the data status of this set after 
    the error. Your task is to firstly find the number occurs twice and 
    then find the number that is missing. Return them in the form of an array.

    Example 1:  Input: nums = [1,2,2,4]   Output: [2,3]

    Note:
    -  The given array size will in the range [2, 10000].
    -  The given array's numbers won't have any order.
"""
from typing import List


class Solution:
    def findErrorNums(self, A: List[int]) -> List[int]:
        N = len(A)
        count = [0] * (N+1)
        for x in A:
            count[x] += 1
        for x in range(1, len(A)+1):
            if count[x] == 2:
                twice = x
            if count[x] == 0:
                never = x
        return [twice, never]

    def findErrorNums(self, A: List[int]) -> List[int]:
        '''
            Say (x, y) is the desired answer. 
            We know sum(A) - x + y = sum([1, 2, ..., N]), and 
            sum(x*x for x in A) - x*x + y*y = sum([1*1, 2*2, ..., N*N]). 
            So we know x-y and x*x-y*y. 
            Dividing the latter by x-y, we know x+y. Hence, we know x and y.
        '''
        N = len(A)
        alpha = sum(A) - N*(N+1)/2
        beta = (sum(x*x for x in A) - N*(N+1)*(2*N+1)/6) / alpha
        return [(alpha + beta) / 2, (beta - alpha) / 2]


assert Solution().findErrorNums([1, 2, 2, 4]) == [2, 3]
print('Tests Passed!!')
