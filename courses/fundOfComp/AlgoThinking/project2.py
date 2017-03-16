"""
Course : Algorithmic Thinking (Part 1)
Instructor: Luay Nakhleh, Scott Rixner, Joe Warren
Project 2 - Connected components and graph resilience
Date: 10/1/2015
Author: Vishal Mittal
"""
import random
import alg_module2_graphs as tgs
from collections import deque

def bfs_visited(ugraph, start_node):
    """
    params: Undirected graph g=(V,E); source node i
    return: Visited; set of all nodes visited.
    """
    # initialize Q to an empty queue;
    # enqueue (Q,i);
    gque = deque()
    gque.appendleft(start_node)

    # Visited <- {i};
    visited = set([start_node])

    # while Q is not empty do
    while len(gque) > 0:
        # j <- dequeue(Q);
        curr_node = gque.pop()

        # foreach neighbor h of j do
        for neighbor in ugraph[curr_node]:
            # if h NOT in Visited then
            if neighbor not in visited:
                # Visited <- Visited U {h};
                visited.add(neighbor)
                # enqueue(Q,h);
                gque.appendleft(neighbor)

    # return Visited;
    return visited

def cc_visited(ugraph):
    """
    params: Undirected graph g=(V,E);
    return: CC; the set of connected components of graph g
    """
    # RemainingNodes <- V;
    remaining_nodes = ugraph.keys()

    # CC <- None;
    conn_comp = []

    # while RemainingNodes != None do
    while len(remaining_nodes) != 0:
        # Let i be an arbitrary node in Remaining Nodes;
        # W <- bfs_visited(ugraph, i)
        visited = bfs_visited(ugraph, random.choice(remaining_nodes))
        # CC <- CC U {W};
        conn_comp.append(visited)
        # RemainingNodes <- RemainingNodes - W;
        remaining_nodes = [ x for x in remaining_nodes if x not in visited]
    
    # return CC;
    return conn_comp

def largest_cc_size(ugraph):
    """
    params: Undirected graph g=(V,E);
    return: the size (an integer) of the largest connected 
            component in ugraph
    """
    conn_comp = cc_visited(ugraph)
    largest = -1
    for compo in conn_comp:
        if len(compo) > largest: 
            largest = len(compo)
    return largest

def compute_resilience(ugraph, attack_order):
    """
    params: Undirected graph g=(V,E); a list of nodes
    return:  a list whose k+1th entry is the size of the largest 
            connected component in the graph after the removal of 
            the first k nodes in attack_order
    """
    resilience = [largest_cc_size(ugraph)]

    # remove one node at a time
    for node in attack_order:
        if len(ugraph.keys())==1:
            resilience.append(0)
            break

        node_conns = ugraph[node]
        del ugraph[node]
        
        for dep_node in node_conns:
            ugraph[dep_node] = ugraph[dep_node] - set([node])
        
        # use largest_cc_size to compute the size of the largest
        #   connected component in the resulting graphs
        resilience.append(largest_cc_size(ugraph))
    return resilience
