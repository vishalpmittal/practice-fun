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

- Directed Graph
- Undirected Graph

- Hamiltonian Graphs

  - traverse graph but visit each NODE exactly once
  - A hamiltonian graph is a on where there is some sequence of the vertex that
    contains each vertex exactly once and such that consecutive vertices in the
    sequence are connected by an edge in the graph.
  - i.e. to visit all vertexes each vertex should be visited only once. No repeatition of any vertex

