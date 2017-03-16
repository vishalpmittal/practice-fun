"""
Student template code for Project 3
Student will implement five functions:

slow_closest_pair(cluster_list)
fast_closest_pair(cluster_list)
closest_pair_strip(cluster_list, horiz_center, half_width)
hierarchical_clustering(cluster_list, num_clusters)
kmeans_clustering(cluster_list, num_clusters, num_iterations)

where cluster_list is a 2D list of clusters in the plane

Course : Algorithmic Thinking (Part 2)
Instructor: Luay Nakhleh, Scott Rixner, Joe Warren
Project 3 - Closest pairs and clustering algorithms
Date: 10/18/2015
Author: Vishal Mittal
"""

import math
import alg_cluster
import random

def ver_cluster_indx_sort(index_list, cluster_list):
    """
    Orders the index list in order of their respective lists y component non descending order
    """
    if len(index_list) < 2:
        return index_list

    result, mid = [], int(len(index_list)/2)

    left = ver_cluster_indx_sort(index_list[:mid], cluster_list)
    right = ver_cluster_indx_sort(index_list[mid:], cluster_list)

    while (len(left) > 0) and (len(right) > 0):
            if cluster_list[left[0]].vert_center() > cluster_list[right[0]].vert_center():
                result.append(right.pop(0))   
            else:
                result.append(left.pop(0))

    result.extend(left+right)
    return result

######################################################
# Code for closest pairs of clusters

def pair_distance(cluster_list, idx1, idx2):
    """
    Helper function that computes Euclidean distance between two clusters in a list

    Input: cluster_list is list of clusters, idx1 and idx2 are integer indices for two clusters
    
    Output: tuple (dist, idx1, idx2) where dist is distance between
    cluster_list[idx1] and cluster_list[idx2]
    """
    return (cluster_list[idx1].distance(cluster_list[idx2]), min(idx1, idx2), max(idx1, idx2))


def slow_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (slow)

    Input: cluster_list is the list of clusters
    
    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.       
    """
    dist_tuple = (float("inf"), -1, -1)
    for outer in range(len(cluster_list)):
        for inner in range(len(cluster_list)):
            if inner == outer:
                continue
            curr_dist = pair_distance(cluster_list, outer, inner)
            if curr_dist[0] < dist_tuple[0]:
                dist_tuple = curr_dist
    return dist_tuple

def fast_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (fast)

    Input: cluster_list is list of clusters SORTED such that horizontal positions of their
    centers are in ascending order
    
    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.       
    """
    clus_len = len(cluster_list)
    min_dist_tuple = ()
    if clus_len <= 3:
        min_dist_tuple = slow_closest_pair(cluster_list)

    else:
        divider = int(clus_len/2)

        left_dist_tuple = fast_closest_pair(cluster_list[:divider])
        right_dist_tuple = fast_closest_pair(cluster_list[divider:])
        
        if (left_dist_tuple[0] < right_dist_tuple[0]):
            min_dist_tuple = (left_dist_tuple[0], left_dist_tuple[1], left_dist_tuple[2])
        else:
            min_dist_tuple = (right_dist_tuple[0], right_dist_tuple[1]+divider, right_dist_tuple[2]+divider)

        mid = (cluster_list[divider-1].horiz_center() + cluster_list[divider].horiz_center())/2
        cps_tuple = closest_pair_strip(cluster_list, mid, min_dist_tuple[0])

        if cps_tuple[0] < min_dist_tuple[0]:
            min_dist_tuple = cps_tuple

    return min_dist_tuple

def closest_pair_strip(cluster_list, horiz_center, half_width):
    """
    Helper function to compute the closest pair of clusters in a vertical strip
    
    Input: cluster_list is a list of clusters produced by fast_closest_pair
    horiz_center is the horizontal position of the strip's vertical center line
    half_width is the half the width of the strip (i.e; the maximum horizontal distance
    that a cluster can lie from the center line)

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] lie in the strip and have minimum distance dist.       
    """
    indexes = [dummy_idx for dummy_idx in range(0, len(cluster_list)) if math.fabs((cluster_list[dummy_idx].horiz_center())-horiz_center) < half_width ]
    indexes = ver_cluster_indx_sort(indexes, cluster_list)

    indx_len = len(indexes)

    dist_tuple = (float("inf"), -1, -1)
    for outer in range (0, indx_len-1):
        for inner in range(outer+1, (min(outer+3, indx_len-1)+1)):
            curr_dist = pair_distance(cluster_list, indexes[outer], indexes[inner])
            if dist_tuple[0] > curr_dist[0]:
                dist_tuple = curr_dist
    return dist_tuple
    
######################################################################
# Code for hierarchical clustering


def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters
    Note: the function may mutate cluster_list
    
    Input: List of clusters, integer number of clusters
    Output: List of clusters whose length is num_clusters
    """
    clusters = [clus.copy() for clus in cluster_list]

    while len(clusters) > num_clusters:
        min_dist = float("inf")
        clus_one = None
        clus_two = None
        
        for outer in range (0, len(clusters)):
            for inner in range (0, len(clusters)):
                if outer == inner:
                    continue
                curr_dist = clusters[outer].distance(clusters[inner])
                if curr_dist < min_dist:
                    min_dist = curr_dist
                    clus_one = clusters[outer]
                    clus_two = clusters[inner]

        clusters.remove(clus_one)
        clusters.remove(clus_two)

        new_cluster = clus_one.merge_clusters(clus_two)
        clusters.append(new_cluster)
    return clusters

######################################################################
# Code for k-means clustering

def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Compute the k-means clustering of a set of clusters
    Note: the function may not mutate cluster_list
    
    Input: List of clusters, integers number of clusters and number of iterations
    Output: List of clusters whose length is num_clusters
    """
    kclusters = []
    comp_clus_centers = []
    total_clusters = len(cluster_list)
    for tot_clus in range (0, total_clusters):
        kclusters.append(cluster_list[tot_clus].copy())

    kclusters.sort(key = lambda cluster: cluster.total_population())

    for index in range (1, num_clusters+1):
        comp_clus_centers.append((kclusters[index*(-1)]).copy())
    kclusters = []

    for index in range (1, num_iterations+1):
        # initiaze num_clusters empty clusters
        kclusters = [alg_cluster.Cluster(set([]), 0.0, 0.0, 0, 0) for dummy_idx in range (1, num_clusters+1)]

        # for each point in the whole cluster list
        for clust_indx in range(0, total_clusters):
            least_center_dist = float("inf")
            least_center_indx = -1
            
            # find the closest center by comparing all centers
            for cntr_indx in range (0, num_clusters):
                curr_center_dist = cluster_list[clust_indx].distance(comp_clus_centers[cntr_indx])
                if curr_center_dist < least_center_dist:
                    least_center_dist = curr_center_dist
                    least_center_indx = cntr_indx

            # Combine it to our kclusters list on that index
            kclusters[least_center_indx].merge_clusters(cluster_list[clust_indx].copy())

        for new_cntr_indx in range(0, num_clusters):
            comp_clus_centers[new_cntr_indx] = kclusters[new_cntr_indx]

    return kclusters

# my_cl_list=[alg_cluster.Cluster(set([1]), 5.0, 2.0, 1, 1), alg_cluster.Cluster(set([2]), 6.0, 4.0, 2, 1), alg_cluster.Cluster(set([3]), 5.0, 5.0, 3, 1), alg_cluster.Cluster(set([4]), 2.2, 5.3, 4, 1), alg_cluster.Cluster(set([5]), 2.5, 6.0, 5, 1), alg_cluster.Cluster(set([6]), 6.0, 5.0, 6, 1), alg_cluster.Cluster(set([7]), 1.0, 6.0, 7, 1), alg_cluster.Cluster(set([8]), 2.0, 1.0, 8, 1), alg_cluster.Cluster(set([9]), 5.0, 4.0, 9, 1), alg_cluster.Cluster(set([10]), 1.5, 5.0, 10, 1), alg_cluster.Cluster(set([11]), 1.5, 6.0, 11, 1)]

# print kmeans_clustering(my_cl_list, 4, 6)