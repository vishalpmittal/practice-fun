"""
    Tag: dp, array, algo

    You have N gardens, labelled 1 to N.  In each garden, 
    you want to plant one of 4 types of flowers.

    paths[i] = [x, y] describes the existence of a 
    bidirectional path from garden x to garden y. Also, there is 
    no garden that has more than 3 paths coming into or leaving it.

    Your task is to choose a flower type for each garden such that, 
    for any two gardens connected by a path, they have different 
    types of flowers.

    Return any such a choice as an array answer, where answer[i] is 
    the type of flower planted in the (i+1)-th garden.  The flower 
    types are denoted 1, 2, 3, or 4.  It is guaranteed an answer exists.

    Ex1: Ip: N = 3, paths = [[1,2],[2,3],[3,1]] Output: [1,2,3]
    Ex2: Ip: N = 4, paths = [[1,2],[3,4]] Output: [1,2,1,2]
    Ex3: Ip: N = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]] Output: [1,2,3,4]

    Note:
    -  1 <= N <= 10000
    -  0 <= paths.size <= 20000
    -  No garden has 4 or more paths coming into or leaving it.
    -  It is guaranteed an answer exists.

    Approach:
    Greedy Algorithm. Get all connected and then from superset delete the connected
    nodes and pop the first from remaining. 
"""
from typing import List


class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        res = [0] * N
        G = [[] for i in range(N)]
        for x, y in paths:
            G[x - 1].append(y - 1)
            G[y - 1].append(x - 1)
        for i in range(N):
            res[i] = ({1, 2, 3, 4} - {res[j] for j in G[i]}).pop()
        return res

    def gardenNoAdj_1(self, N: int, paths: List[List[int]]) -> List[int]:
        # Same as above but difference Data structure for garden paths.
        res = [0] * N
        GP = {x: set() for x in N}  # garden paths
        for x, y in paths:
            GP[x].add(y)
            GP[y].add(x)

        for i in range(N):
            res[i] = ({1, 2, 3, 4} - {res[j] for j in GP[i]}).pop()
        return res


assert Solution().gardenNoAdj(3, [[1, 2], [2, 3], [3, 1]]) == [1, 2, 3]
assert Solution().gardenNoAdj(4, [[1, 2], [3, 4]]) == [1, 2, 1, 2]
assert Solution().gardenNoAdj(
    4, [[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]]) == [1, 2, 3, 4]
print('Tests Passed!!')
