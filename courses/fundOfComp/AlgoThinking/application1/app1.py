"""
Course : Algorithmic Thinking (Part 1)
Instructor: Luay Nakhleh, Scott Rixner, Joe Warren
Assignment 1 Q1- Citation Graphs
Date: 09/19/2015
Author: Vishal Mittal
"""
import project1
from provided_load_graph import load_graph_from_file
import matplotlib.pyplot as plt
import random
import dpa

def normalize_in_degree_distribution(dist_graph):
    # Calculate sum of all the values, i.e. total #nodes
    total_val_count = float(sum(dist_graph.itervalues()))

    norm_ind_dist = {}
    for key, value in dist_graph.iteritems():
        norm_ind_dist[key] = value/total_val_count

    return norm_ind_dist

def ER_algo_dgraph(n, p):
    graph = {key: set() for key in xrange(n)}
    for i in xrange(n):
        for j in xrange(n):
            if i == j:
                continue
            if random.random() < p:
                graph[i].add(j)
            if random.random() < p:
                graph[j].add(i)
    return graph

def avg_out_degree(graph):
    # total nodes in the graph
    N = float(len(graph))

    # for each node calculate length of its subset
    # sum all the lengths and devide by N
    return sum(len(x) for x in graph.itervalues()) / N

def ques1():
    citation_graph = load_graph_from_file("alg_phys-cite.txt")
    citation_degree_dist = project1.in_degree_distribution(citation_graph)
    citation_norm_dist = normalize_in_degree_distribution(citation_degree_dist)

    plt.plot(citation_norm_dist.keys(), citation_norm_dist.values(), 'o', ms=4.0)
    plt.loglog()
    plt.title('Normalized InDegree Distribution of Citation Data')
    plt.xlabel('log(In Degree)', fontsize=14, color='blue')
    plt.ylabel('log(Normalized Distribution)', fontsize=14, color='blue')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("ques1_plot.png")

def ques2():
    er_graph = ER_algo_dgraph(3000, 0.3)
    ind_er_graph = project1.in_degree_distribution(er_graph)
    norm_ind_er_graph = normalize_in_degree_distribution(ind_er_graph)
   
    plt.plot(norm_ind_er_graph.keys(), norm_ind_er_graph.values(), 'o', ms=2.0)
    plt.loglog()
    plt.title('Normalized InDegree Distribution of Random Graph based on ER Algorithm')
    plt.xlabel('log(In Degree)', fontsize=12, color='blue')
    plt.ylabel('log(Normalized Distribution)', fontsize=12, color='blue')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("ques2_plot.png")

def ques3():
    # find out average out degree of citation graph
    citation_graph = load_graph_from_file("alg_phys-cite.txt")
    print "n: " + str(len(citation_graph))
    print "m: " + str(avg_out_degree(citation_graph))

def ques4():
    dpa_graph = dpa.dpa_graph(28000,13)
    ind_dpa_graph = project1.in_degree_distribution(dpa_graph)
    norm_ind_dpa_graph = normalize_in_degree_distribution(ind_dpa_graph)

    plt.plot(norm_ind_dpa_graph.keys(), norm_ind_dpa_graph.values(), 'o', ms=2.0)
    plt.loglog()
    plt.title('Normalized InDegree Distribution of Graph based on DPA Algorithm')
    plt.xlabel('log(In Degree)', fontsize=12, color='blue')
    plt.ylabel('log(Normalized Distribution)', fontsize=12, color='blue')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("ques4_plot.png")
    
def main():
    # ques1()
    # ques2()
    ques3()
    ques4()

if __name__ == '__main__':
    main()
