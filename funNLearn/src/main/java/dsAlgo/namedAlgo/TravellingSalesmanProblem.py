"""
    Tag: algo, TO-DO

    -  Traveling Salesperson Problem (TSP)
    -  Problem: 
        -  travel the cities of world with minimum cost
        -  All the cities are connected to all other cities
        -  these cities and flights between them is a fully connected graph with weightage edges
        -  After visiting all the cities you have to come back at the origin

    -  Approach : Brute Force
        -  Find all the paths
        -  For each path calculate the cost using weights
        -  Pick the one with lowest cost
        -  O(n) = n!

    -  Approach : Greedy algorithm (Nearest Neighbor)
        -  At every node pick the next node connected with lowest weight
        -  Might not provide the best solution
        -  O(n) = n^2

    -  Approach : NP Hard
    -  Heuristics and Approximation Algorithms
"""