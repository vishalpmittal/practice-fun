"""
    Tag: graph, sort, list, DAG

    Given a DAG (Directed Acrylic Graph) print the graph in topographical order. 

    Topographical order is the one where we print the vertex with 
    no out degree (no dependency) first. then dependent on it and dependent on those
    and then so on. 
    Basically start with no dependency and then go to last one. 

    Eg:
        5 -----> 0 <------ 4
        |                  |
        |                  |
        v                  v
        2 -----> 3 ------> 1

    wrong  : 5 2 3 1 0 4
    correct: 0 1 3 2 5 4
"""
from typing import List


def topologicalSort(G: dict) -> List[str]:
    def util(curr_vert, stack, UVV):
        UVV.remove(curr_vert)

        for nebr_vert in G[curr_vert]:
            if nebr_vert in UVV:
                util(nebr_vert, stack, UVV)

        stack.append(curr_vert)

    stack = []
    UVV = set(G.keys())  # unvisited vertices

    for vert in G.keys():
        if vert in UVV:
            util(vert, stack, UVV)

    return stack


G1 = {5: {0, 2}, 2: {3}, 0: {}, 3: {1}, 4: {0, 1}, 1: {}}
print(topologicalSort(G1))
