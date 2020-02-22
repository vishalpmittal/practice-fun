"""
    Tag: array, game

    In a town, there are N people labelled from 1 to N. 
    There is a rumor that one of these people is secretly the town judge.

    If the town judge exists, then:
    1. The town judge trusts nobody.
    2. Everybody (except for the town judge) trusts the town judge.
    3. There is exactly one person that satisfies properties 1 and 2.

    You are given trust, an array of pairs trust[i] = [a, b] 
    representing that the person labelled a trusts the person labelled b.

    If the town judge exists and can be identified, return the label of 
    the town judge.  Otherwise, return -1.

    Ex1: Ip: N = 2, trust = [[1,2]] Op: 2
    Ex2: Ip: N = 3, trust = [[1,3],[2,3]] Op: 3
    Ex3: Ip: N = 3, trust = [[1,3],[2,3],[3,1]] Op: -1
    Ex4: Ip: N = 3, trust = [[1,2],[2,3]] Op: -1
    Ex5: Ip: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]] Op: 3

    Note:
    -  1 <= N <= 1000
    -  trust.length <= 10000
    -  trust[i] are all different
    -  trust[i][0] != trust[i][1]
    -  1 <= trust[i][0], trust[i][1] <= N
"""
from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        TM = {}             # Trust Map {x: y}, x trusts y
        for t in trust:
            if t[0] not in TM:
                TM[t[0]] = set()
            TM[t[0]].add(t[1])

        print(TM)
        for v in range(1, N+1):            # for every villager
            if v in TM:
                continue

            # trustees list
            tl = [x for x in range(1, v)] + [x for x in range(v+1, N+1)]
            vtc = 0                   # Villager trustees count
            for x in tl:
                if v in TM.get(x, set()):
                    vtc += 1
            if vtc == N-1:
                return v
        return -1

    def findJudge_1(self, N: int, trust: List[List[int]]) -> int:
        # Faster way
        trusted = [0] * (N+1)
        for a, b in trust:
            trusted[a] -= 1
            trusted[b] += 1

        for i in range(1, N+1):
            if trusted[i] == N-1:
                return i
        return -1


assert Solution().findJudge(2, [[1, 2]]) == 2
assert Solution().findJudge(3, [[1, 3], [2, 3]]) == 3
assert Solution().findJudge(3, [[1, 3], [2, 3], [3, 1]]) == -1
assert Solution().findJudge(3, [[1, 2], [2, 3]]) == -1
assert Solution().findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]) == 3

print('Tests Passed!!')
