"""
    Tag: math

    You have a total of n coins that you want to form in a staircase shape, 
    where every k-th row must have exactly k coins.
    Given n, find the total number of full staircase rows that can be formed.

    n is a non-negative integer and fits within the range of a 32-bit signed integer.

    Example 1: n = 5
    The coins can form the following rows:
    ¤
    ¤ ¤
    ¤ ¤
    Because the 3rd row is incomplete, we return 2.

    Example 2: n = 8
    The coins can form the following rows:
    ¤
    ¤ ¤
    ¤ ¤ ¤
    ¤ ¤
    Because the 4th row is incomplete, we return 3.
"""
import math


def arrangeCoins(n: int) -> int:
    s = 1
    steps = 0
    while s <= n:
        steps += 1
        s += steps+1
    return steps


def arrangeCoins_1(n: int) -> int:
    '''
    The number of coins in k steps is 1+2+...+k = k(k+1)/2. Now solve for k in terms of n.
    '''
    return math.floor((-1 + math.sqrt(1 + 8 * n))/2)


def test_code():
    assert arrangeCoins(8) == 3
    assert arrangeCoins(0) == 0
    assert arrangeCoins(10) == 4
    assert arrangeCoins(5) == 2
    print("Tests Passed!!")


test_code()
