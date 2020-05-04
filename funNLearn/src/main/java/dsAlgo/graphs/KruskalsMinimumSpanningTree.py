"""
    tag: graph, spanning tree, algo, tree

    Spanning Tree: weighted graph where every node is connected and there are n-1 edges for n vertices
    
    Minimum Spanning Tree:
    - connect all the nodes
    - should not form a cycle
    - with minimum sum weight of the edges

    Brut force: 
    we can create combinations of each vertices and possible edges
    then calculate the minimum sum but it will be exponential run time

    Kruskals Minimum Spanning Tree Algo. 
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


def kruskals_spanning_tree(G):
    mst = {}
    edges = set()
    for from_vertex, to_vertices in G.items():
        for to_vertex in to_vertices:
            cost = G[from_vertex][to_vertex]
            if (cost, from_vertex, to_vertex) not in edges: 
                if (cost, to_vertex,from_vertex) not in edges:
                    edges.add((cost, from_vertex, to_vertex))
    sorted_edges = sorted(edges, key=lambda x: x[0])

    print(edges)

    for vertex in G.keys():
        mst[vertex] = {}

    for cost, from_v, to_v in sorted_edges:
        if to_v not in mst[from_v]:
            mst[from_v][to_v] = cost
            mst[to_v][from_v] = cost
    
    




    pass


example_graph = {
    "A": {"B": 2, "C": 3},
    "B": {"A": 2, "C": 1, "D": 1, "E": 4},
    "C": {"A": 3, "B": 1, "F": 5},
    "D": {"B": 1, "E": 1},
    "E": {"B": 4, "D": 1, "F": 1},
    "F": {"C": 5, "E": 1, "G": 1},
    "G": {"F": 1},
}
print(kruskals_spanning_tree(example_graph))
# {'A': {'B': 2}, 'B': {'C': 1, 'D': 1}, 'D': {'E': 1}, 'E': {'F': 1}, 'F': {'G': 1}}
