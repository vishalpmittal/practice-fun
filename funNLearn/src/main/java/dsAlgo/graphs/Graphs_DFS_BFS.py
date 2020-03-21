"""
    tag: graph, bfs, dfs

    provided a graph, print it's BFS and DFS
"""

from queue import Queue


class Solution:
    def BFS(self, G):
        q = Queue()
        UVS = set(G.keys())  # unvisited vertices set
        q.put(UVS.pop())

        while not q.empty():
            cv = q.get()  # cv = current vertex
            print(cv, end=", ")
            for nv in G[cv]:  # nv = Neighbor vertex
                if nv in UVS:
                    q.put(nv)
                    UVS.remove(nv)
        print()


    def DFS(self, G):
        ST = []  # ST = stack
        UVS = set(G.keys())  # unvisited vertices set
        ST[0] = UVS.pop()

        while len(ST) > 0 :
            cv = q.get()  # cv = current vertex
            print(cv, end=", ")
            for nv in G[cv]:  # nv = Neighbor vertex
                if nv in UVS:
                    q.put(nv)
                    UVS.remove(nv)
        print()



graph = {
    "B": {"A": 5, "D": 1, "G": 2},
    "A": {"B": 5, "D": 3, "E": 12, "F": 5},
    "D": {"B": 1, "G": 1, "E": 1, "A": 3},
    "G": {"B": 2, "D": 1, "C": 2},
    "C": {"G": 2, "E": 1, "F": 16},
    "E": {"A": 12, "D": 1, "C": 1, "F": 2},
    "F": {"A": 5, "E": 2, "C": 16},
}

Solution().BFS(graph)
