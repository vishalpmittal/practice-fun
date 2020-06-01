"""
    tag: sort, graph, DAG

    Given a dependency graph, print the object in order of no dependent first 
    to most dependent last. 

    Topographical sorting

    each vertex is dependent on the vertexes it is pointing to. 
    So a vertex with no outdegree, but with only indegree has no dependency 

    vertices with similar dependency can appear in any order

    Make sure to check for multiple 
"""


from typing import List


def identify_depencies(G) -> List[str]:
    # add all the vertices to a set of UVV: Unvisited Vertices
    UVV = set()
    for vert, neighbors in G.items():
        UVV.add(vert)
        for nebr in neighbors:
            UVV.add(nebr)
    stack = []

    def depend_util(curr_vert, UVV, stack, curr_stack_callers):
        UVV.remove(curr_vert)

        if curr_vert in G.keys():
            for nv in G[curr_vert]:  # nv: neighbor vertex
                # check for circurlar graph
                # basically if neighbor's neighor exist in curr calling stack.
                if nv in G.keys():
                    for ntonv in G[nv]:
                        if ntonv in curr_stack_callers:
                            print("Circular graph, no topographical order")
                            exit()

                # else for all neighbors call recursively
                if nv in UVV:
                    curr_stack_callers.add(curr_vert)
                    depend_util(nv, UVV, stack, curr_stack_callers)

        stack.append(curr_vert)

    for vert in G.keys():
        if vert in UVV:
            depend_util(vert, UVV, stack, set([vert]))

    return stack


graph = {
    "vehicle": ["wheel", "engine", "window"],
    "wheel": ["tire", "rim"],
    "tire": ["rubber"],
    "rim": ["cast-metal", "bolts"],
    "engine": ["bolts", "cast-metal", "oil"],
    "window": ["glass"],
    "truck": ["wheel", "engine", "window"],
}
circular_graph = {
    "vehicle": ["wheel", "engine", "window"],
    "wheel": ["tire", "rim"],
    "tire": ["rubber"],
    "rim": ["cast-metal", "bolts"],
    "engine": ["bolts", "cast-metal", "oil"],
    "window": ["glass"],
    "truck": ["wheel", "engine", "window"],
    "bolts": ["wheel"],
}

print(identify_depencies(graph))
print(identify_depencies(circular_graph))
