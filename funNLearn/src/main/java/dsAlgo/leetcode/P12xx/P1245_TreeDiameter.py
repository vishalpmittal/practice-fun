"""
    tag: graph, tree, dfs, bfs

    Given an undirected tree, return its diameter: 
    the number of edges in a longest path in that tree.

    The tree is given as an array of edges where edges[i] = [u, v] is 
    a bidirectional edge between nodes u and v.  
    Each node has labels in the set {0, 1, ..., edges.length}.

    Example 1: edges = [[0,1],[0,2]]
    Output: 2
    Explanation: A longest path of the tree is the path 1 - 0 - 2.

    Example 2: edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
    Output: 4
    Explanation: A longest path of the tree is the path 3 - 2 - 1 - 4 - 5.
 
    Constraints:
    - 0 <= edges.length < 10^4
    - edges[i][0] != edges[i][1]
    - 0 <= edges[i][j] <= edges.length
    - The given edges form an undirected tree.
"""
from typing import List
from collections import deque, defaultdict


class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        """
            -  Choose any point to dfs to get the farthest point
            -  Than this farthest found point should be one side of the diameter
            -  do another dfs to get another end point of the diameter
        """

        # do dfs from vertex vert, update maxlength and end point.
        def dfs(vert, prev, length):
            # Check if end point and is farther end point
            if (
                len(graph[vert]) == 1
                and graph[vert][0] == prev
                and length > farthest_vert[0]
            ):
                farthest_vert[0] = length
                farthest_vert[1] = vert
            for y in graph[vert]:
                # since it is acyclic, thus just avoid x->y->x will avoid duplicate visit.
                if y != prev:
                    dfs(y, vert, length + 1)

        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        farthest_vert = [0, None]  # [maxlen,endNode]
        dfs(edges[0][0], None, 0)
        dfs(farthest_vert[1], None, 0)
        return farthest_vert[0]


assert Solution().treeDiameter([[0, 1], [1, 2], [2, 3], [1, 4], [4, 5]]) == 4
print("Tests Passed!!")

