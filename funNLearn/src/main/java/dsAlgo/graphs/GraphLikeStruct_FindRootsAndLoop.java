
package dsAlgo.graphs;

import java.util.*;

class Node {
  // guaranteed to be unique
  public final int id;

  // items are unique and non-null
  public final List<Node> children = new LinkedList<Node>();

  public Node(int id) {
    this.id = id;
  }

  /*
   * 0) Returns the number of Nodes in the input allNodes that qualify as "root"s
   * (see next) 1) "root" = A Node that is not in the "children" list of any Node
   * 2) *All* Nodes are in "allNodes". Items are unique and non-null
   */
  public static int countRoots(Node[] allNodes) {
    HashSet<Node> hs = new HashSet<Node>();
    for (Node node : allNodes) {
      hs.add(node);
    }

    for (Node node : allNodes) {
      for (Node child : node.children) {
        hs.remove(child);
      }
    }

    return hs.size();
  }

  /*
   * 0) Returns true/false, whether the input allNodes contains a "loop" (see *
   * next) 1) "loop" = following child nodes leads back to self 2) *All* Nodes are
   * in "allNodes". Nodes are unique and non-null
   */
  public static boolean containsLoop(Node[] allNodes) {
    HashSet<Node> processed_set = new HashSet<Node>(); // 1, 2
    
    for (Node node: allNodes){
      if (processed_set.contains(node))
        continue;
     
      HashSet<Node> considered = new HashSet<Node>();
      LinkedList<Node> ll  = new LinkedList<Node>();
      ll.add(node);
      
      while (ll.size() > 0){
        curr_node = ll.pop_front();    
        if considered.contains(curr_node){
          return true;
        }
        considered.add(curr_node);
        ll.addAll(curr_node.children);
        processed_set.add(curr_node);
      }
      
    }
    return false;
  }
}
