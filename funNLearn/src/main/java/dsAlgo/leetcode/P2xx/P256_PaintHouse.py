"""
    Tag: dp, array, matrix,

    There are a row of n houses, each house can be painted with one of the 
    three colors: red, blue or green. The cost of painting each house with a certain 
    color is different. You have to paint all the houses such that no two adjacent 
    houses have the same color.

    The cost of painting each house with a certain color is represented by
    a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 
    with color red; costs[1][2] is the cost of painting house 1 with color green, 
    and so on... Find the minimum cost to paint all houses.

    Note:
    All costs are positive integers.

    Example:
    Input: [[17,2,17],
            [16,16,5],
            [14,3,19]]
    Output: 10
    Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. 
    Minimum cost: 2 + 5 + 3 = 10.
"""

def minCost(costs):
    """
    :type costs: List[List[int]]
    :rtype: int
    """
    if not costs or len(costs)==0:
        return 0
    
    # red cost, blue cost and green costs of house 0
    rc, bc, gc = costs[0][0], costs[0][1], costs[0][2]
    min_cost = min(rc, bc, gc)
    house = 1

    while house < len(costs):
        nrc = costs[house][0] + min(bc, gc)
        nbc = costs[house][1] + min(rc, gc)
        ngc = costs[house][2] + min(rc, bc)
        rc, bc, gc = nrc, nbc, ngc
        min_cost = min(rc, bc, gc)
        house += 1
    return min_cost

def test_code():
    assert minCost([[17,2,17], [16,16,5], [14,3,19]]) == 10
    assert minCost([[17,17,2], [16,16,5], [14,3,19]]) == 21
    print ("Tests Passed!")

test_code()
