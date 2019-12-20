"""
    Tag: dp, array

    Suppose you have a long flowerbed in which some of the plots are planted 
    and some are not. However, flowers cannot be planted in adjacent plots - 
    they would compete for water and both would die.

    Given a flowerbed (represented as an array containing 0 and 1, where 0 means 
    empty and 1 means not empty), and a number n, return if n new flowers can be
    planted in it without violating the no-adjacent-flowers rule.

    Example 1: Input: flowerbed = [1,0,0,0,1], n = 1    Output: True
    Example 2: Input: flowerbed = [1,0,0,0,1], n = 2    Output: False

    Note:
    -  The input array won't violate no-adjacent-flowers rule.
    -  The input array size is in the range of [1, 20000].
    -  n is a non-negative integer which won't exceed the input array size.
"""
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # add a 0 in the front and end and then count whenever you find 3 straight zeros.
        # if found, place a 1 there and move ahead.
        count = 0
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
                flowerbed[i] = 1
                count += 1
        return count >= n


assert Solution().canPlaceFlowers([1, 0, 0, 0, 1], 1)
assert not Solution().canPlaceFlowers([1, 0, 0, 0, 1], 2)
print('Tests Passed!!')
