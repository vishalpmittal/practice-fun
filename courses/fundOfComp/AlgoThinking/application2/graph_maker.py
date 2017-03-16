"""
Provides basic graphs for provided number of nodes
"""
import random

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

def make_unconnected_graph(num_nodes):
    """
    params: number of nodes
    return: a dictionary corresponding to a graph with only 
            nodes and no edges
    """
    graph={}
    
    # return a dictionary corresponding to the empty graph.
    if num_nodes<=0:
        return graph

    # for each node
    for node in range(0, num_nodes):
        node_set=set([])
        graph[node] = node_set
    return graph

def make_undirected_er_graph(num_nodes, probability):
    """
    params: number of nodes, probability for er creation
    return: a dictionary corresponding to a undirected 
            graph based on er algo
    """
    uer_graph = {key: set() for key in xrange(num_nodes)}

    temp_visited = {key: set() for key in xrange(num_nodes)}

    for i in xrange(num_nodes):
        for j in xrange(num_nodes):
            if i == j or j in temp_visited[i]:
                continue
            if random.random() < probability:
                uer_graph[i].add(j)
                uer_graph[j].add(i)

            temp_visited[i].add(j)
            temp_visited[j].add(i)

    return uer_graph
