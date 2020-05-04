"""
    tag: graph, recursive, DAG

    You are given a DAG (directed acyclic grapk0 which may be disjointed. 
    The graph may represent, for instance, courses in a university that must be taken 
    in a particular order, but may represent different streams. 

    Write the code to read in an input file desaibing the graph, identify all nodes 
    with 0 in-degree, and for each such node, generate all possible paths that 
    originate from that node. 
    
    For example, for the following graph (all the edges are pointing downwards): 
            0       6
          /   \   / 
         1      2       4
       /  \   /
      3      5

    Here is an input file that describes it. 
    7
    0, 1
    0, 2
    1, 3 
    1, 5
    2, 5
    6, 2
    
    The first line is the total number of nodes. 
    Every subsequent line represents an edge between two nodes. 

    Given that graph, you should generate the following paths: 
    0->1->3
    0->1->5
    0->2->5
    4
    6->2->5
"""
import fileinput

# Using dictionary representation of a directed graph
# G = {0: {1, 2}, 1: {3, 5}, 2: {5}, 3: set(), 4: set(), 5: set(), 6: {2}}
G = {}

# set of nodes that can be starter nodes for a path
initiative_nodes = set()


def read_graph_from_stdin():
    c = 0
    for line in fileinput.input():
        if c == 0:
            # create base graph with all the nodes and no edges
            numb_of_nodes = int(line.strip())
            for i in range(numb_of_nodes):
                G[i] = set()
                initiative_nodes.add(i)
        else:
            # add edges to graph G and remove child nodes from the initiative_nodes
            edge = line.split(",")
            n1 = int(edge[0].strip())
            n2 = int(edge[1].strip())
            G[n1].add(n2)
            if n2 in initiative_nodes:
                initiative_nodes.remove(n2)
        c += 1
    return G


def create_graph_from_list_of_lines(list_of_lines):
    # create base graph with all the nodes and no edges
    numb_of_nodes = int(list_of_lines[0].strip())
    for i in range(numb_of_nodes):
        G[i] = set()
        initiative_nodes.add(i)

    for line in list_of_lines[1:]:
        # add edges to graph G and remove child nodes from the initiative_nodes
        edge = line.split(",")
        n1 = int(edge[0].strip())
        n2 = int(edge[1].strip())
        G[n1].add(n2)
        if n2 in initiative_nodes:
            initiative_nodes.remove(n2)

    return G


def get_all_paths():
    paths = []

    def helper(curr_node, path_so_far):
        if len(G[curr_node]) == 0:
            # no more children. leaf node. add to path and return
            paths.append(path_so_far + str(curr_node))
            return

        for path_node in G[curr_node]:
            # update path_so_far and continue with all child nodes
            helper(path_node, path_so_far + str(curr_node) + "->")

    # for all the starter nodes in the G, check for paths
    for node in initiative_nodes:
        helper(node, "")

    return paths


# read_graph_from_stdin()
create_graph_from_list_of_lines(["7", "0, 1", "0, 2", "1, 3", "1, 5", "2, 5", "6, 2"])
assert G == {0: {1, 2}, 1: {3, 5}, 2: {5}, 3: set(), 4: set(), 5: set(), 6: {2}}
assert initiative_nodes == {0, 4, 6}
assert get_all_paths() == ["0->1->3", "0->1->5", "0->2->5", "4", "6->2->5"]
print("Tests Passed!")
