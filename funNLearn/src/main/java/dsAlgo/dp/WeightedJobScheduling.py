"""
    tag: array, dp

    given a list of interval start time, stop time and cost. 
    find the subset that no two intervals overlap and the cost is maximum

    eg: [0,1,5],[1,3,10],[2,5,20],[4,6,30],[7,9,10]
    answer: [0,1,5],[1,3,10],[4,6,30],[7,9,10]

    eg: [0,1,5],[1,3,10],[2,5,20],[4,6,5],[7,9,10]
    answer: [0,1,5],[2,5,20],[7,9,10]

    LIC = [[1,3,5],[2,5,6],[4,6,5],[6,7,4],[5,8,11],[7,9,2]]
    C = [5, 6, 5, 4, 11, 2]
    Final C = [5, 6, 10, 14, 17, 16]
"""


def findNonOverlappingIntervalMaxCost(LIC):
    # LIC = List of intervals and costs
    if not LIC:
        return []

    # sort by non-decreasing finish time
    LIC = sorted(LIC, key=lambda x: x[1])

    # list containing the costs of each interval
    C = [x[2] for x in LIC]

    for i in range(1, len(C)):  # for every i from 1 to n-1
        for j in range(0, i):  # for every j from 0 to i
            if LIC[j][1] <= LIC[i][0]:  # if no overlap
                # get max cost till j + cost of i , and keep the max
                C[i] = max(C[i], C[j] + LIC[i][2])
    return max(C)


LIC = [[1, 3, 5], [2, 5, 6], [4, 6, 5], [6, 7, 4], [5, 8, 11], [7, 9, 2]]
assert findNonOverlappingIntervalMaxCost(LIC) == 17
