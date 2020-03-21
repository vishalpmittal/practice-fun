""""
    tag: tree

    Given a list of Nodes find if all the nodes combine to make a one single binary tree. 
    The tree does not need to be BST, or symmetric or balanced. 
    It should be just one binary tree with no cycle
    Return the root node of the tree. 

    Eg: [D, C, A, E, G, F]
    Return A for following:    
            A
           /  \
          B    D
         / \    \
        C   E    G
           /
          F
        
    Return None for following:
            A               E          G
           /  \            /  \ 
          B    D          C    F   

    Return None for following:
            A
           /  \
          B    D
         / \    \\
        C   E    G
           //
          F
"""

from typing import List


class TN:
    def __init__(self, val):
        self.val = val
        self.left = left
        self.right = right


def find_if_single_BT(lon: List[TN]) -> TN:
    if not lon or len(lon) == 0:
        return None

    ns = set([x for x in lon])
    for x in lon:
        ns.remove(x.left)
        ns.remove(x.right)

    if len(ns) != 1:
        return None

    rn = ns.pop()
    q = [rn]
    visited = set()

    while len(q) > 0:
        cn = q.pop(0)
        if cn in visited:
            return None
        visited.add(cn)
        if cn.left:
            q.append(cn.left)
        if cn.right:
            q.append(cn.right)

    return rn if len(visited) == len(lon) else None
