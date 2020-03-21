"""
    You are given coins of different denominations and a total amount of 
    money amount. Write a function to compute the fewest number of coins 
    that you need to make up that amount. If that amount of money cannot 
    be made up by any combination of the coins, return -1
  
    Ex: [1,2,5,10], 15
    for 15: output: [10 5]

    EX: [1,2,5,5,10], 18 
    output: [10 5 2 1]
    for 19 : 10 5 2 2

    we only have one of each 
"""

from typing import List

# CL = coin list, A = Amount
def coinChangeMinCoins(CL: List[int], A: int) -> List[int]:
    if not CL or not A or A == 0:
        return []
    CL.sort(reverse=True)

    def dfs(rcl, ra, ccl):
        if ra <= 0 or not rcl:
            return -1
        if rcl[0] == ra:
            ccl.append(rcl[0])
            return ccl
        if rcl[0] < ra:
            ccl.append(rcl[0])
            return dfs(rcl[1:], ra - rcl[0], ccl)
        elif rcl[0] > ra:
            return dfs(rcl[1:], ra, ccl)

    return dfs(CL, A, [])


# CL = coin list, A = Amount
def coinChangeMinCoins_dp(CL: List[int], A: int) -> List[int]:
    if not CL or not A or A == 0:
        return []

    dp = [[-1 for _ in range(A + 1)] for _ in range(len(CL) + 1)]
    print(dp)


print(coinChangeMinCoins_dp([1, 2, 3], 4))

# assert coinChangeMinCoins([1, 2, 3], 1) == [1]
# assert coinChangeMinCoins([1, 2, 3], 4) == [3, 1]
# assert coinChangeMinCoins([1, 2, 3], 5) == [3, 2]
# assert coinChangeMinCoins([1, 2, 3], 6) == [3, 2, 1]
# assert coinChangeMinCoins([1, 2, 3], 7) == -1
# assert coinChangeMinCoins([1, 2, 2, 5, 10], 19) == [10, 5, 2, 2]
# assert coinChangeMinCoins([1, 2, 5, 10, 10], 21) == [10, 10, 1]
# print("Tests Passed!")

