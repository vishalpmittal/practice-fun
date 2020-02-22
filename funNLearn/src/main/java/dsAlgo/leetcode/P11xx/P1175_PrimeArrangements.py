"""
    Tag: math

    Return the number of permutations of 1 to n so that 
    prime numbers are at prime indices (1-indexed.)

    (Recall that an integer is prime if and only if it is 
    greater than 1, and cannot be written as a product of two 
    positive integers both smaller than it.)

    Since the answer may be large, return the answer modulo 10^9 + 7.

    Example 1: Input: n = 5 Output: 12
    Explanation: For example [1,2,5,4,3] is a valid permutation, 
    but [5,2,3,4,1] is not because the prime number 5 is at index 1.

    Example 2: Input: n = 100 Output: 682289015

    Constraints: 1 <= n <= 100
"""
from typing import List
import math


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def countPrimes(n):
            is_prime = [False]*2 + [True]*(n-2)
            for i in range(2, int(n ** 0.5)+1):
                if is_prime[i]:
                    is_prime[i*i:n:i] = [False] * len(is_prime[i*i:n:i])
            return sum(is_prime)
        c = countPrimes(n+1)

        # permutations to arrange primes * permutations to arrange other nums
        ans = math.factorial(c) * math.factorial(n-c)
        return ans % (10**9+7)


assert Solution().numPrimeArrangements(5) == 12
assert Solution().numPrimeArrangements(100) == 682289015
print('Tests Passed!!')
