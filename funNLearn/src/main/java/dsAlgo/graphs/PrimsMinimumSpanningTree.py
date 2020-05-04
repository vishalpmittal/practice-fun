"""
    tag: graph, spanning tree, algo, tree

    Spanning Tree: weighted graph where every node is connected and there are n-1 edges for n vertices
    
    Prims Minimum Spanning Tree:
    - connect all the nodes
    - should not form a cycle
    - with minimum sum weight of the edges

    Brut force: 
    we can create combinations of each vertices and possible edges
    then calculate the minimum sum but it will be exponential run time

    Prims Minimum Spanning Tree Algo. 
    1. pick a starting vertex
    2. add all the edges of starting vertex to a binary heap (priority queue)
    3. pull an edge from the heap, this will be the smallest edge of the starting vertex
    4. add the other end vertex (to_vertex) of the edge to the MST
    5. add to_vertex to visited
    6. add all edges to non-visited vertices from to_vertex into the heap
    7. repeat steps 3,4,5,6 until the queue is empty
"""
from collections import defaultdict
import heapq


def create_spanning_tree(G, starting_vertex):  # 1
    mst = defaultdict()
    visited = set([starting_vertex])
    edges = [
        (cost, starting_vertex, to) for to, cost in G[starting_vertex].items()
    ]  # 2
    heapq.heapify(edges)  # edges = [(2, 'A', 'B'), (3, 'A', 'C')]

    while edges:
        cost, frm, to = heapq.heappop(edges)  # 3
        if to not in visited:
            mst[frm] = mst.get(frm, {})
            mst[frm][to] = cost  # 4

            visited.add(to)  # 5
            for to_next, cost in G[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (cost, to, to_next))  # 6
    return mst


example_graph = {
    "A": {"B": 2, "C": 3},
    "B": {"A": 2, "C": 1, "D": 1, "E": 4},
    "C": {"A": 3, "B": 1, "F": 5},
    "D": {"B": 1, "E": 1},
    "E": {"B": 4, "D": 1, "F": 1},
    "F": {"C": 5, "E": 1, "G": 1},
    "G": {"F": 1},
}
print(dict(create_spanning_tree(example_graph, "A")))
# {'A': {'B': 2}, 'B': {'C': 1, 'D': 1}, 'D': {'E': 1}, 'E': {'F': 1}, 'F': {'G': 1}}
