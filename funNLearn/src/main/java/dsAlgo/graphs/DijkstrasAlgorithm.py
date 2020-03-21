"""
    Tag: graph, algo

    Dijkstras Algorithm
"""

import sys

from typing import Dict


class Solution:
    def dijkstras_shortest_path(self, G, S):
        if not G or not S:
            return {}

        # initialize the distance to all vertex is infinite but to source is 0
        dist = {}
        for vertex in G.keys():
            dist[vertex] = float("inf")
        dist[S] = 0

        next_to_visit = set()
        visited = set()
        cv = S  # cv = current vertex
        next_to_visit.add(S)

        while cv:
            next_to_visit.remove(cv)
            visited.add(cv)

            # for each of cv's neighboring nodes update the disctance from source node
            for nv in G[cv].keys():  # nv = neighbor vertex
                if nv not in visited:
                    nv_dist = dist[cv] + G[cv][nv]  # nv_dist = neighbor vertex distance
                    dist[nv] = min(dist[nv], nv_dist)
                    next_to_visit.add(nv)

            # find vertex to consider next, pick the one which is:
            # - Not yet picked
            # - is neighbors atleast one of the previously picked
            # - next shortest distance in list
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
