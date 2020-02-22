"""
    Tag: dp, array, integer, recursive

    You are given coins of different denominations and a total amount of money. 
    Write a function to compute the number of combinations that make up that amount. 
    You may assume that you have infinite number of each kind of coin.

    Example 1: amount = 5, coins = [1, 2, 5]
    Output: 4
    Explanation: there are four ways to make up the amount:
    5=5
    5=2+2+1
    5=2+1+1+1
    5=1+1+1+1+1

    Example 2: amount = 3, coins = [2]
    Output: 0
    Explanation: the amount of 3 cannot be made up just with coins of 2.

    Example 3: amount = 10, coins = [10] 
    Output: 1

    Note: You can assume that
    -  0 <= amount <= 5000
    -  1 <= coin <= 5000
    -  the number of coins is less than 500
    -  the answer is guaranteed to fit into signed 32-bit integer
"""
from typing import List


class Solution:
    def change_1(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        if amount < 0 or len(coins) == 0:
            return 0

        # Our solutions can be divided into two sets,
        #   1) Solutions that cointain the coin at the end of the coins array
        #   2) Solutions that don't contain that coin
        return self.change(amount - coins[-1], coins) + self.change(
            amount, coins[:-1])

    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        return dp[amount]


assert Solution().change(5, [1, 2, 5]) == 4
assert Solution().change(15, [1, 5, 10, 25, 50]) == 6
print('Tests Passed!!')
