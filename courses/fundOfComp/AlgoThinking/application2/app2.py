"""
Course : Algorithmic Thinking (Part 1)
Instructor: Luay Nakhleh, Scott Rixner, Joe Warren
Application 2 - Analysis of a computer network
Date: 10/04/2015
Author: Vishal Mittal
"""

# general imports
import urllib2
import random
import time
import math
import timeit

import matplotlib.pyplot as plt
import graph_maker
import upa
import project2

############################################
# Provided code

NETWORK_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_rf7.txt"

def copy_graph(graph):
    """
    Make a copy of a graph
    """ 
    new_graph = {}
    for node in graph:
        new_graph[node] = set(graph[node])
    return new_graph

def delete_node(ugraph, node):
    """
    Delete a node from an undirected graph
    """
    neighbors = ugraph[node]
    ugraph.pop(node)
    for neighbor in neighbors:
        ugraph[neighbor].remove(node)
    
def targeted_order(ugraph):
    """
    Compute a targeted attack order consisting
    of nodes of maximal degree
    
    Returns:
    A list of nodes
    """
    # copy the graph
    new_graph = copy_graph(ugraph)
    
    order = []    
    while len(new_graph) > 0:
        max_degree = -1
        for node in new_graph:
            if len(new_graph[node]) > max_degree:
                max_degree = len(new_graph[node])
                max_degree_node = node
        
        neighbors = new_graph[max_degree_node]
        new_graph.pop(max_degree_node)
        for neighbor in neighbors:
            new_graph[neighbor].remove(max_degree_node)

        order.append(max_degree_node)
    return order
    
##########################################################
# Code for loading computer network graph

def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print "Loaded graph with", len(graph_lines), "nodes"
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph

def random_order(ugraph):
    all_nodes = ugraph.keys()
    random.shuffle(all_nodes)
    return all_nodes

def get_num_nodes(ugraph):
    return len(ugraph.keys())

def get_num_edges(ugraph):
    temp_visited = {key: set() for key in ugraph.keys()}
    num_edges = 0

    for node in ugraph.keys():
        for conn_node in ugraph[node]:
            if conn_node not in temp_visited[node]:
                num_edges += 1

            temp_visited[node].add(conn_node)
            temp_visited[conn_node].add(node)

    return num_edges

def get_percent_resilience(res_list):
    total_len = len(res_list)
    per_res_list = [None]*total_len

    for i in range (0, total_len):
        per_res_list[i]=(res_list[i]*100)/(total_len - i)
    return per_res_list

def fast_targeted_order(ugraph):
    ugraph_copy = copy_graph(ugraph)
    len_graph = len(ugraph_copy)
    degree_sets = [set()] * len_graph
    for node, neighbors in ugraph_copy.iteritems():
        degree = len(neighbors)
        degree_sets[degree].add(node)
    order = []

    for k in range(len_graph - 1, -1, -1):
        while degree_sets[k]:
            u = degree_sets[k].pop()
            for neighbor in ugraph_copy[u]:
                d = len(ugraph_copy[neighbor])
                degree_sets[d].remove(neighbor)
                degree_sets[d - 1].add(neighbor)

            order.append(u)
            delete_node(ugraph_copy, u)
    return order

def ques1(ques):
    cn_graph=load_graph(NETWORK_URL)
    num_cn_nodes = get_num_nodes(cn_graph)
    num_cn_edges = get_num_edges(cn_graph)
    print "=========cn========="
    print num_cn_nodes
    print num_cn_edges
    cn_attack_order = random_order(cn_graph)
    cn_resilience = project2.compute_resilience(cn_graph, cn_attack_order)
    cn_per_resl= get_percent_resilience(cn_resilience)

    upa_cg_nodes = 2
    upa_graph = upa.get_upa_graph(num_cn_nodes, upa_cg_nodes)
    num_upa_nodes = get_num_nodes(upa_graph)
    num_upa_edges = get_num_edges(upa_graph)
    print "=========upa========="
    print num_upa_nodes
    print num_upa_edges
    upa_attack_order = random_order(upa_graph)
    upa_resilience = project2.compute_resilience(upa_graph, upa_attack_order)
    upa_per_resl= get_percent_resilience(upa_resilience)

    er_prob = 0.004
    er_graph = graph_maker.make_undirected_er_graph(num_cn_nodes, er_prob)
    num_er_nodes = get_num_nodes(er_graph)
    num_er_edges = get_num_edges(er_graph)
    print "=========er========="
    print num_er_nodes
    print num_er_edges
    er_attack_order = random_order(er_graph)
    er_resilience = project2.compute_resilience(er_graph, er_attack_order)
    er_per_resl= get_percent_resilience(er_resilience)

    x_range=[x for x in range (0, len(cn_resilience))]
    if ques == 1:
        plt.plot(x_range, cn_resilience, '-b', label="ComputerNetworks=(V:%s, E:%s)" % (str(num_cn_nodes), str(num_cn_edges)))
        plt.plot(x_range, er_resilience, '-r', label="ER Graph=(V:%s, E:%s), Probability(p):%s" % (str(num_er_nodes), str(num_er_edges), str(er_prob)))
        plt.plot(x_range, upa_resilience, '-g', label="UPA Graph=(V:%s, E:%s), ComplGraphNodes(m): %s" % (str(num_upa_nodes), str(num_upa_edges), str(upa_cg_nodes)))
        plt.ylabel('Size of the largest connect component', fontsize=14, color='blue')
    if ques == 2:
        plt.plot(x_range, cn_per_resl, '-b', label="ComputerNetworks=(V:%s, E:%s)" % (str(num_cn_nodes), str(num_cn_edges)))
        plt.plot(x_range, er_per_resl, '-r', label="ER Graph=(V:%s, E:%s), Probability(p):%s" % (str(num_er_nodes), str(num_er_edges), str(er_prob)))
        plt.plot(x_range, upa_per_resl, '-g', label="UPA Graph=(V:%s, E:%s), ComplGraphNodes(m): %s" % (str(num_upa_nodes), str(num_upa_edges), str(upa_cg_nodes)))
        plt.ylabel('Perc Components Connected of remaining Nodes', fontsize=14, color='blue')

    plt.legend(loc='upper right', prop={'size':10}, title='Desktop Python 2.7.10')
    plt.title('Resilience Plot (Random Order of Removal)')
    plt.xlabel('Num of Nodes removed', fontsize=14, color='blue')

    plt.grid(True)
    plt.tight_layout()
    if ques == 1:
        plt.savefig("app2_q1.png")
    elif ques == 2:
        plt.savefig("app2_q2.png")

def ques3():
    x_range = range(10, 1000, 10)
    m = 5
    ys_tagreted=[]
    ys_fast_targeted = []

    for n in x_range:
        upa_graph = upa.get_upa_graph(n, m)
        ft_upa_graph = copy_graph(upa_graph)
        
        ys_tagreted.append(timeit.timeit(lambda: targeted_order(upa_graph), number=1))
        ys_fast_targeted.append(timeit.timeit(lambda: fast_targeted_order(ft_upa_graph), number=1))

    plt.plot(x_range, ys_tagreted, '-b', label="Targeted Order time")
    plt.plot(x_range, ys_fast_targeted, '-r', label="Fast Targeted Order time")
    plt.ylabel('Time', fontsize=14, color='blue')

    plt.legend(loc='upper left', prop={'size':10}, title='Desktop Python 2.7.10')
    plt.title('Time comparison of order Algorithms')
    plt.xlabel('Num of Nodes in UPA graph', fontsize=14, color='blue')

    plt.grid(True)
    plt.tight_layout()
    plt.savefig("app2_q3.png")
    
def bigo_notation_plots():
    x_range = range(10, 1000, 10)

    ys_linear = [x for x in x_range]
    ys_square = [x*x for x in x_range]
    ys_cube = [(x*x*x) for x in x_range]
    ys_log = [(math.log(x)) for x in x_range]

    plt.plot(x_range, ys_linear, '-b', label="ys_linear")
    plt.plot(x_range, ys_square, '-r', label="ys_square")
    plt.plot(x_range, ys_cube, '-g', label="ys_cube")
    plt.plot(x_range, ys_log, '-y', label="ys_log")
    plt.ylabel('Time', fontsize=14, color='blue')

    plt.legend(loc='upper right', prop={'size':10}, title='Desktop Python 2.7.10')
    plt.title('Time comparison of Algorithms')
    plt.xlabel('n Rnage', fontsize=14, color='blue')

    plt.grid(True)
    plt.tight_layout()
    plt.savefig("bigo_notation_plots.png")

def ques4(ques):
    cn_graph=load_graph(NETWORK_URL)
    num_cn_nodes = get_num_nodes(cn_graph)
    num_cn_edges = get_num_edges(cn_graph)

    cn_attack_order = targeted_order(cn_graph)
    cn_resilience = project2.compute_resilience(cn_graph, cn_attack_order)
    cn_per_resl= get_percent_resilience(cn_resilience)

    upa_cg_nodes = 2
    upa_graph = upa.get_upa_graph(num_cn_nodes, upa_cg_nodes)
    num_upa_nodes = get_num_nodes(upa_graph)
    num_upa_edges = get_num_edges(upa_graph)
    upa_attack_order = targeted_order(upa_graph)
    upa_resilience = project2.compute_resilience(upa_graph, upa_attack_order)
    upa_per_resl= get_percent_resilience(upa_resilience)

    er_prob = 0.004
    er_graph = graph_maker.make_undirected_er_graph(num_cn_nodes, er_prob)
    num_er_nodes = get_num_nodes(er_graph)
    num_er_edges = get_num_edges(er_graph)
    er_attack_order = targeted_order(er_graph)
    er_resilience = project2.compute_resilience(er_graph, er_attack_order)
    er_per_resl= get_percent_resilience(er_resilience)

    x_range=[x for x in range (0, len(cn_resilience))]
    if ques == 4:
        plt.plot(x_range, cn_resilience, '-b', label="ComputerNetworks=(V:%s, E:%s)" % (str(num_cn_nodes), str(num_cn_edges)))
        plt.plot(x_range, er_resilience, '-r', label="ER Graph=(V:%s, E:%s), Probability(p):%s" % (str(num_er_nodes), str(num_er_edges), str(er_prob)))
        plt.plot(x_range, upa_resilience, '-g', label="UPA Graph=(V:%s, E:%s), ComplGraphNodes(m): %s" % (str(num_upa_nodes), str(num_upa_edges), str(upa_cg_nodes)))
        plt.ylabel('Size of the largest connect component', fontsize=14, color='blue')
    elif ques == 5:
        plt.plot(x_range, cn_per_resl, '-b', label="ComputerNetworks=(V:%s, E:%s)" % (str(num_cn_nodes), str(num_cn_edges)))
        plt.plot(x_range, er_per_resl, '-r', label="ER Graph=(V:%s, E:%s), Probability(p):%s" % (str(num_er_nodes), str(num_er_edges), str(er_prob)))
        plt.plot(x_range, upa_per_resl, '-g', label="UPA Graph=(V:%s, E:%s), ComplGraphNodes(m): %s" % (str(num_upa_nodes), str(num_upa_edges), str(upa_cg_nodes)))
        plt.ylabel('Perc Components Connected of remaining Nodes', fontsize=14, color='blue')

    plt.legend(loc='upper right', prop={'size':10}, title='Desktop Python 2.7.10')
    plt.title('Resilience Plot (Targeted Order of Removal)')
    plt.xlabel('Num of Nodes removed', fontsize=14, color='blue')

    plt.grid(True)
    plt.tight_layout()
    if ques == 4:
        plt.savefig("app2_q4.png")
    elif ques == 5:
        plt.savefig("app2_q5.png")

def main():
    # ques1(1)
    # plt.clf()
    # ques1(2)
    # plt.clf()
    ques3()
    plt.clf()
    # ques4(4)
    # plt.clf()
    # ques4(5)

    # bigo_notation_plots()

if __name__ == '__main__':
    main()
