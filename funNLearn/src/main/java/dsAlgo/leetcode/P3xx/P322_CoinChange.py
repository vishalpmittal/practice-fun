"""
    Tag: dp, array, integer, recursive

    You are given coins of different denominations and a total amount 
    of money amount. Write a function to compute the fewest number of 
    coins that you need to make up that amount. If that amount of money 
    cannot be made up by any combination of the coins, return -1.

    Example 1: coins = [1, 2, 5], amount = 11
    Output: 3 
    Explanation: 11 = 5 + 5 + 1

    Example 2: coins = [2], amount = 3
    Output: -1

    Note:
    You may assume that you have an infinite number of each kind of coin.
"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # DP
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

    def coinChange_1(self, coins, amount):
        # recursive dfs
        coins.sort(reverse=True)
        lenc, self.res = len(coins), 2**31 - 1

        def dfs(pt, rem, count):
            if not rem:
                self.res = min(self.res, count)
            for i in range(pt, lenc):
                if coins[i] <= rem < coins[i] * (self.res - count):
                    dfs(i, rem - coins[i], count + 1)

        for i in range(lenc):
            dfs(i, amount, 0)
        return self.res if self.res < 2**31 - 1 else -1


assert Solution().coinChange([1, 2, 5], 11) == 3
print('Tests Passed!!')
