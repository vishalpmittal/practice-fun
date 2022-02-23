"""
    tag: graph, bfs

    Have the function  ShortestPath(strArr) take strArr which will be an array of strings which models 
    a non-looping Graph. The structure of the array will be as follows: The first element in the array 
    will be the number of nodes N (points) in the array as a string. The next N elements will be the 
    nodes which can be anything (A, B, C .. Brick Street, Main Street .. etc.). Then after the Nth element, 
    the rest of the elements in the array will be the connections between all of the nodes. They will look 
    like this: (A-B, B-C .. Brick Street-Main Street .. etc.). Although, there may exist no connections at all. 

    An example of strArr may be: 
    ["4","A","B","C","D","A-B","B-D","B-C","C-D"]. Your program should return the shortest path from the 
    first Node to the last Node in the array separated by dashes. So in the example above the output 
    should be A-B-D. Here is another example with strArr being 
    ["7","A","B","C","D","E","F","G","A-B","A-E","B-C","C-D","D-F","E-D","F-G"]. 
    The output for this array should be A-E-D-F-G. There will only ever be one shortest path for the array. 
    If no path between the first and last node exists, return -1. The array will at minimum have two nodes. 
    Also, the connection A-B for example, means that A can get to B and B can get to A.
"""

from queue import Queue

def ShortestPath(strArr):
  # parse the array and create a graph
  num_of_nodes = int(strArr[0])
  G = {}
  for x in range(1, num_of_nodes +1):
    G[strArr[x]] = set()
  
  for edge in strArr[num_of_nodes + 1:]:
    elements = edge.split('-')
    G[elements[0]].add(elements[1])
    G[elements[1]].add(elements[0])

  start_node = strArr[1]
  end_node = strArr[num_of_nodes]
  print(G, start_node, end_node)

  # start the BFS on the created graph
  q = Queue()
  unvisited = set(G.keys())
  q.put((start_node, ''))   # add a tuple of current node and path so far in the queue
  unvisited.remove(start_node)

  while not q.empty():
    curr_tuple = q.get()
    curr_node = curr_tuple[0]
    curr_path = curr_tuple[1]

    if curr_node == end_node:
      return curr_path + curr_node
      break

    for neighbor in G[curr_node]:
      if neighbor in unvisited:
        q.put((neighbor, curr_path + curr_node +'-'))
        unvisited.remove(neighbor)

  return '-1'


assert(ShortestPath(["5","A","B","C","D","F","A-B","A-C","B-C","C-D","D-F"]) == 'A-C-D-F')
assert(ShortestPath(["4","X","Y","Z","W","X-Y","Y-Z","X-W"]) == 'X-W')
assert(ShortestPath(["4","X","Y","Z","W","X-Y","Y-Z","X-Z"]) == '-1')

print('Tests Passed')
