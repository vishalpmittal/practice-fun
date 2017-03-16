"""
Course : Algorithmic Thinking (Part 1)
Instructor: Luay Nakhleh, Scott Rixner, Joe Warren
Project 1 - Degree distributions for graphs
Date: 09/13/2015
Author: Vishal Mittal
"""

EX_GRAPH0 ={0: set([1,2]),
            1: set([]),
            2: set([])}

EX_GRAPH1 ={0: set([1,4,5]),
            1: set([2,6]),
            2: set([3]),
            3: set([0]),
            4: set([1]),
            5: set([2]),
            6: set([])}

EX_GRAPH2 ={0: set([1,4,5]),
            1: set([2,6]),
            2: set([3,7]),
            3: set([7]),
            4: set([1]),
            5: set([2]),
            6: set([]),
            7: set([3]),
            8: set([1,2]),
            9: set([0,3,4,5,6,7])}

def make_complete_graph(num_nodes):
    """
    params: number of nodes
    return: a dictionary corresponding to a complete 
            directed graph with the specified number of nodes
    """
    graph={}
    
    # return a dictionary corresponding to the empty graph.
    if num_nodes<=0:
        return graph

    # for each node
    for node in range(0, num_nodes):
        node_set=set([])

        # add all the edges but itself
        for edge_to in range(0, num_nodes):
            if edge_to != node:
                node_set.add(edge_to)
        graph[node] = node_set

    return graph

def compute_in_degrees(digraph):
    """
    params: a directed graph
    return: a dictionary with the same set of keys (nodes) as digraph 
            whose corresponding values are the number of edges 
            whose head matches a particular node.
    """
    in_degree = {}
    if digraph == None:
        return in_degree

    for node in digraph:
        # add node to with 0 indegree if missing from in_degree
        if node not in in_degree:
            in_degree[node] = 0

        # for each node in the set update in value
        for in_node in digraph[node]:
            if in_node not in in_degree:
                in_degree[in_node] = 1
            else:
                in_degree[in_node] += 1

    return in_degree

def in_degree_distribution(digraph):
    """
    params: a directed graph
    return: a dictionary whose keys correspond to in-degrees 
            of nodes in the graph
    """
    indegree = compute_in_degrees(digraph)
    degree_dist = {}
    for degree in indegree:
        if indegree[degree] not in degree_dist:
            degree_dist[indegree[degree]] = 1
        else:
            degree_dist[indegree[degree]] += 1

    return degree_dist
