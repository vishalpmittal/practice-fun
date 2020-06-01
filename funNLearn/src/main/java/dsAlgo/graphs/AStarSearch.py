"""
    Tag: graph, algo, TO-DO
    A Star Algorithm: find path from start to every other vertex

"""

import sys

from typing import Dict


class Solution:
    def a_star_(self, G, S):  # G: graph, S: start vertex

        if not G or not S:
            return {}

        # by default all vertex are at infinite distance and
        # self is at 0 distance
        dist = {}
        for vertex in G.keys():
            dist[vertex] = float("inf")
        dist[S] = 0

        next_to_visit = set()  # store non visited neighbors
        visited = set()  # visited vertices
        cv = S  # cv = current vertex
        next_to_visit.add(S)

        while cv:
            next_to_visit.remove(cv)
            visited.add(cv)

            # find distance to all neighbors, min of existing and distance via current vertex
            for nv in G[cv].keys():  # nv = neighbor vertex
                if nv not in visited:
                    nv_dist = dist[cv] + G[cv][nv]  # nv_dist = neighbor vertex distance
                    dist[nv] = min(dist[nv], nv_dist)
                    next_to_visit.add(nv)

            # find the next vertex to visit, closest one
            cv = None
            md = float("inf")  # minimum distance
            for ntv_v in next_to_visit:  # ntv_v = next to visit vertex
                if ntv_v not in visited:
                    if dist[ntv_v] < md:
                        md = dist[ntv_v]
                        cv = ntv_v

        return dist


graph = {
    "B": {"A": 5, "D": 1, "G": 2},
    "A": {"B": 5, "D": 3, "E": 12, "F": 5},
    "D": {"B": 1, "G": 1, "E": 1, "A": 3},
    "G": {"B": 2, "D": 1, "C": 2},
    "C": {"G": 2, "E": 1, "F": 16},
    "E": {"A": 12, "D": 1, "C": 1, "F": 2},
    "F": {"A": 5, "E": 2, "C": 16},
}

assert Solution().dijkstras_shortest_path(graph, "B") == {
    "B": 0,
    "A": 4,
    "D": 1,
    "G": 2,
    "C": 3,
    "E": 2,
    "F": 4,
}
print("Tests Passed")
