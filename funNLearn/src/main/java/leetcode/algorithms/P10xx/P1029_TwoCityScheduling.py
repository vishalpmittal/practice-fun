"""
    Tag: array, algo

    There are 2N people a company is planning to interview. 
    The cost of flying the i-th person to city A is costs[i][0], 
    and the cost of flying the i-th person to city B is costs[i][1].

    Return the minimum cost to fly every person to a city such 
    that exactly N people arrive in each city.

    Example 1: Input: [[10,20],[30,200],[400,50],[30,20]] Output: 110
    Explanation: 
    -  The first person goes to city A for a cost of 10.
    -  The second person goes to city A for a cost of 30.
    -  The third person goes to city B for a cost of 50.
    -  The fourth person goes to city B for a cost of 20.

    The total minimum cost is 10 + 30 + 50 + 20 = 110 to have 
    half the people interviewing in each city.
    
    Note:
    -  1 <= costs.length <= 100
    -  It is guaranteed that costs.length is even.
    -  1 <= costs[i][0], costs[i][1] <= 1000


    Approach: Greedy Algorithm
    The company would pay anyway : price_A to send a person to the city A, 
    or price_B to send a person to the city B. By sending the person to the 
    city A, the company would lose price_A - price_B, 
    which could negative or positive.

    To optimize the total costs, let's sort the persons by 
    price_A - price_B and then send the first n persons to the city A, 
    and the others to the city B, because this way the company costs are minimal.
"""
from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # Sort by a gain which company has
        # by sending a person to city A and not to city B
        costs.sort(key=lambda x: x[0] - x[1])

        total = 0
        n = len(costs) // 2
        # To optimize the company expenses,
        # send the first n persons to the city A
        # and the others to the city B
        for i in range(n):
            total += costs[i][0] + costs[i + n][1]
        return total


assert Solution().twoCitySchedCost(
    [[10, 20], [30, 200], [400, 50], [30, 20]]) == 110
print('Tests Passed!!')
