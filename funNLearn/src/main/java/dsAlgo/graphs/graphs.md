# Graphs

## Components

- Vertex (nodes)
- Edges (arc)

## Presentations

1. Adjacency Matrix
    - Pros:
      - easy to implement
      - removing edge takes O(1) time
      - edge query are O(1)
    - Cons:
      - consumes more space O(V^2)
      - add a vertex is O(V^2)

2. Adjacency List
    - Pros:
      - Saves space O(|V|+|E|)
      - Adding vertex is easier
    - edge queries takes O(V)

3. Dictionary of Dictionaries

  ```python
  nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
  distances = {
      'B': {'A': 5, 'D': 1, 'G': 2},
      'A': {'B': 5, 'D': 3, 'E': 12, 'F' :5},
      'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
      'G': {'B': 2, 'D': 1, 'C': 2},
      'C': {'G': 2, 'E': 1, 'F': 16},
      'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
      'F': {'A': 5, 'E': 2, 'C': 16}
  }
  ```

## Types


### Directed Graph
--------------------
* each edge has a direction and written in tuple notation rather than set notation 
* edge from 0 to 1 is written as (0 , 1), it can not be written as (1, 0)
* Node 0 has InDegree = 0 and OutDegree = 1
* Node 1 has InDegree = 3 and outDegree = 0
* Path: there is a path from 0 to 1, 3 to 1, 2 to 1
* there is NO path from 1 to 0

```
G = ( V, E )
V = {  0 , 1, 2, 3 }
E = { (0,1 ) , ( 3,1 ) , (2,1 ) }
where, 
	G: graph, V: vertices, E: edges
```

### Undirected Graph
--------------------
* Graphs with no direction
* V can be in any order no ordering 
* Represented in set notations
* Node 0 has degree 2
* Node 1 has degree 2, and all has the same
* Path: there is a path from 0 to 2, 2 to 3, 2 to 0 etc.
* distance between 0 and 2 is 2 and there are 2 such paths 
  
```
  G = ( V, E )
  V = {  0 , 1, 2, 3 }
  E = { { 0,1 } , { 1,2 } , { 2,3 } , { 3,4 } }
  where, 
    G: graph, V: vertices, E: edges
```
* Maximum possible degree of a node in G is (n-1)
* Maximum possible number of edges in g is n(n-1)/2

### Hamiltonian Graphs
----------------------
* traverse graph but visit each NODE exactly once
* A hamiltonian graph is a on where there is some sequence of the vertex that
  contains each vertex exactly once and such that consecutive vertices in the
  sequence are connected by an edge in the graph.
* i.e. to visit all vertexes each vertex should be visited only once. No
  repetition of any vertex

