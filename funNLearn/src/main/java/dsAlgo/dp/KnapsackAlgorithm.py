"""
    Tag: dp, recursive, algo

    Knapsack problem
    Given a set of items, each with a weight and a value, determine 
    the number of each item to include in a collection so that the 
    total weight is less than or equal to a given limit and the total 
    value is as large as possible.


"""
from typing import List
from timeit import timeit


class Solution:
    def __init__(self, W: int = 0, n: int = 0):
        self.memo = [[None for x in range(W + 1)] for y in range(n + 1)]

    def knapsack_greedy(self, W: int, wl: List[int], vl: List[int]) -> int:
        """
            sort the items by (value/weight) in non-increasing order 
            basically calculate highest value per kg of weight            
            keep picking untill the weight is in limit. 
            In this solution we can partial pick (eg. 3 out of 5) the 
            last item we are picking

            W = total weight, wl = weight list, vl = value list
            v_to_w_l = value to weight list
        """
        if W < 0 or not wl or not vl or len(wl) != len(vl):
            return 0

        v_to_w_l = [(vl[i], wl[i]) for i in range(len(vl))]
        v_to_w_l.sort(key=lambda x: x[0] / x[1], reverse=True)

        tcw = 0  # total current weight
        tv = 0  # total value
        for v, w in v_to_w_l:
            w_to_consume = min(W - tcw, w)
            tcw += w_to_consume
            tv += w_to_consume * (v / w)
        return tv

    def knapsack_0_1_recursive(self, W: int, wt: List[int], val: List[int], n):
        """
            start from the last element, either chose the element or dont chose and 
            keep recursing. Time complexity is O(2^n)
        """
        if n == 0 or W == 0:
            return 0

        # If weight of the nth item is more than Knapsack of capacity
        # W, then this item cannot be included in the optimal solution
        if wt[n - 1] > W:
            return self.knapsack_0_1_recursive(W, wt, val, n - 1)

        # the maximum of two cases: (1) nth item included, (2) not included
        else:
            return max(
                val[n - 1] + self.knapsack_0_1_recursive(W - wt[n - 1], wt, val, n - 1),
                self.knapsack_0_1_recursive(W, wt, val, n - 1),
            )

    def knapsack_0_1_memoization(self, W: int, wt: List[int], val: List[int], n):
        """
        memorization 
        """
        if self.memo[n][W]:
            return self.memo[n][W]
        elif n == 0 or W == 0:
            result = 0
        elif wt[n - 1] > W:
            result = self.knapsack_0_1_memoization(W, wt, val, n - 1)
        else:
            result = max(
                val[n - 1]
                + self.knapsack_0_1_memoization(W - wt[n - 1], wt, val, n - 1),
                self.knapsack_0_1_memoization(W, wt, val, n - 1),
            )
        self.memo[n][W] = result
        return result

    def knapSack_dp(self, W: int, wt: List[int], val: List[int], n: int):
        K = [[0 for x in range(W + 1)] for x in range(n + 1)]

        # Build table K[][] in bottom up manner
        for i in range(n + 1):
            for w in range(W + 1):
                if i == 0 or w == 0:
                    K[i][w] = 0
                elif wt[i - 1] <= w:
                    K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
                else:
                    K[i][w] = K[i - 1][w]

        print(K)
        return K[n][W]


W = 15
val = [10, 5, 15, 7, 6, 18, 3]
wt = [2, 3, 5, 7, 1, 4, 1]
n = len(val)

# print(Solution().knapsack_greedy(W, wt, val))
# print(Solution().knapsack_0_1_recursive(W, wt, val, n))
# S = Solution(W, n)
# print(S.knapsack_0_1_memoization(W, wt, val, n))
# print(S.memo)

print(Solution().knapSack_dp(W, wt, val, n))
