"""
    tag: graph, bfs, dfs

    provided a graph, print it's BFS and DFS
"""

from queue import Queue


class Solution:
    def BFS(self, G, s):
        q = Queue()
        UVS = set(G.keys())  # unvisited vertices set
        q.put(s)
        UVS.remove(s)

        while not q.empty():
            cv = q.get()  # cv = current vertex
            print(cv, end=", ")
            for nv in G[cv]:  # nv = Neighbor vertex
                if nv in UVS:
                    q.put(nv)
                    UVS.remove(nv)
        print()

    def DFS(self, G, s):
        ST = []  # ST = stack
        UVS = set(G.keys())  # unvisited vertices set
        ST.append(s)
        UVS.remove(s)

        while len(ST) > 0:
            cv = ST.pop(len(ST) - 1)  # cv = current vertex
            print(cv, end=", ")
            for nv in G[cv]:  # nv = Neighbor vertex
                if nv in UVS:
                    ST.append(nv)
                    UVS.remove(nv)
        print()

    def DFS_Rec(self, G, s):
        def dfs_util(cv, UVS):
            UVS.remove(cv)
            print(cv, end=", ")

            for nv in G[cv]:
                if nv in UVS:
                    dfs_util(nv, UVS)

        UVS = set(G.keys())
        dfs_util(s, UVS)


G = {
    "B": {"A": 5, "D": 1, "G": 2},
    "A": {"B": 5, "D": 3, "E": 12, "F": 5},
    "D": {"B": 1, "G": 1, "E": 1, "A": 3},
    "G": {"B": 2, "D": 1, "C": 2},
    "C": {"G": 2, "E": 1, "F": 16},
    "E": {"A": 12, "D": 1, "C": 1, "F": 2},
    "F": {"A": 5, "E": 2, "C": 16},
}

G1 = {5: {0, 2}, 2: {3}, 0: {}, 3: {1}, 4: {0, 1}, 1: {}}

Solution().BFS(G1, 5)
Solution().BFS(G1, 4)
Solution().DFS(G1, 5)
Solution().DFS_Rec(G1, 5)
