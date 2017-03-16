"""
Course : Algorithmic Thinking (Part 1)
Instructor: Luay Nakhleh, Scott Rixner, Joe Warren
Application 3 - Comparison of clustering algorithms
Date: 10/24/2015
Author: Vishal Mittal
"""
from random import random
from timeit import timeit
import matplotlib.pyplot as plt

from alg_cluster import Cluster as CL
from alg_project3_viz import load_data_table
from alg_clusters_matplotlib import plot_clusters

from project3 import slow_closest_pair as SCP
from project3 import fast_closest_pair as FCP
from project3 import hierarchical_clustering
from project3 import kmeans_clustering

def gen_random_clusters(num_clusters):
    def generate(_):
        x = random()*2 -1
        y = random()*2 -1
        return CL(set(['1']), x, y, 1, 1)

    return map(generate, range(0, num_clusters))

def visualize(datafile, output, cluster_func):
    print "Loading data from file: " + str(datafile)
    data_table = load_data_table(datafile)
    clusters = [CL(set([x[0]]), x[1], x[2], x[3], x[4]) for x in data_table]
    print "Calling clustering function: "+ str(cluster_func)
    clusters = cluster_func(clusters)
    print "Displaying", len(clusters), "clusters"
    # plot_clusters(data_table, clusters, True, output)
    plot_clusters(data_table, clusters, True)
    return clusters

def ques1():
    len_range = range(2, 201)
    fast_time, slow_time = [0]*201, [0]*201

    for cluster_len in len_range:
        clusters = gen_random_clusters(cluster_len)
        fast_time[cluster_len] = timeit(lambda: FCP(clusters), number=1)
        slow_time[cluster_len] = timeit(lambda: SCP(clusters), number=1)

    plt_xrange = range(0, 201)

    plt.plot(plt_xrange, fast_time, '-r', label='fast_closest_pair')
    plt.plot(plt_xrange, slow_time, '-b', label='slow_closest_pair')
    plt.title('Running time of closest_pair functions (Desktop Python 2.7.10)')
    plt.xlabel('Number of initial clusters', fontsize=12, color='blue')
    plt.ylabel('Running time, seconds', fontsize=12, color='blue')
    plt.legend(loc='upper left', prop={'size':10}, title='Legend')
    plt.tight_layout()
    plt.grid(True)

    plt.savefig("graphs/ques1.png")
    print('Saved plot to ques1.png')

def ques2():
    visualize('data/unifiedCancerData_3108.csv', "graphs/ques2.png", lambda x: hierarchical_clustering(x, 15))

def ques3():
    visualize('data/unifiedCancerData_3108.csv', "graphs/ques2.png", lambda x: kmeans_clustering(x, 15, 5))

def ques5():
    visualize('data/unifiedCancerData_111.csv', "graphs/ques5.png", lambda x: hierarchical_clustering(x, 9))

def ques6():
    visualize('data/unifiedCancerData_111.csv', "graphs/ques6.png", lambda x: kmeans_clustering(x, 9, 5))

def compute_distortion(datafile, cluster_func):
    print "Loading data from file: " + str(datafile)
    data_table = load_data_table(datafile)
    clusters = [CL(set([x[0]]), x[1], x[2], x[3], x[4]) for x in data_table]
    print "Calling clustering function: "+ str(cluster_func)
    clusters = cluster_func(clusters)
    dist = sum([x.cluster_error(data_table) for x in clusters])
    print('Distortion = %f (%s)' % (dist, dist))
    return dist

def ques7():
    compute_distortion('data/unifiedCancerData_111.csv', lambda x:hierarchical_clustering(x, 9))
    # compute_distortion('data/unifiedCancerData_290.csv', lambda x:hierarchical_clustering(x, 16))
    compute_distortion('data/unifiedCancerData_111.csv', lambda x:kmeans_clustering(x, 9, 5))
    # compute_distortion('data/unifiedCancerData_290.csv', lambda x:kmeans_clustering(x, 16, 5))

def create_dis_graph(datafile, filename):
    print "Loading data from file: " + str(datafile)
    data_table = load_data_table(datafile)
    clusters = [CL(set([x[0]]), x[1], x[2], x[3], x[4]) for x in data_table]
    
    xs = range(6, 21)
    ys_hier = []
    ys_kmeans = []

    for num_clusters in xs:
        hier_out_clust = hierarchical_clustering(clusters, num_clusters)
        hier_dist = sum([x.cluster_error(data_table) for x in hier_out_clust])
        ys_hier.append(hier_dist)        

    for num_clusters in xs:
        kmean_out_clust = kmeans_clustering(clusters, num_clusters, 5)
        kmean_dist = sum([x.cluster_error(data_table) for x in kmean_out_clust])
        ys_kmeans.append(kmean_dist)        

    print xs
    print len(xs)
    print ys_hier
    print len(ys_hier)
    print ys_kmeans
    print len(ys_kmeans)

    plt.cla()
    plt.plot(xs, ys_hier, '-r', label='Hierarchical clustering distortion')
    plt.plot(xs, ys_kmeans, '-b', label='K-means clustering distortion')
    plt.title('Clustering distortion (%s)' % datafile)
    plt.xlabel('Num of output clusters', fontsize=12, color='blue')
    plt.ylabel('Associated Distortion', fontsize=12, color='blue')
    plt.legend(loc='upper right', prop={'size':10}, title='Legend')
    plt.tight_layout()
    plt.grid(True)
    plt.savefig(filename)
    print('Saved plot to %s' % filename)

def ques10():
    # create_dis_graph('data/unifiedCancerData_111.csv', 'graphs/ques10-111.png')
    # create_dis_graph('data/unifiedCancerData_290.csv', 'graphs/ques10-290.png')
    create_dis_graph('data/unifiedCancerData_896.csv', 'graphs/ques10-896.png')


def main():
    # ques1()
    # ques2()
    # ques3()
    # ques5()
    # ques6()
    # ques7()
    ques10()

if __name__ == '__main__':
    main()
