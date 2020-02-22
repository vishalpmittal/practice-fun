"""
    Tag: TO-DO, tree

    Given a non-empty binary search tree and a target value, find k values 
    in the BST that are closest to the target.
    
    Note:
    -  Given target value is a floating point.
    -  You may assume k is always valid, that is: k ≤ total nodes.
    -  You are guaranteed to have only one unique set of k values in 
       the BST that are closest to the target.
    
    Example: root = [4,2,5,1,3], target = 3.714286, and k = 2
        4
       / \
      2   5
     / \
    1   3
    
    Output: [4,3]
    
    Follow up:
    Assume that the BST is balanced, could you solve it in less than O(n) 
    runtime (where n = total nodes)?
"""
from typing import List
import heapq


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def closestKValues_1(self, root: TreeNode, target: float, k: int) -> List[int]:
        if not root or k <= 0:
            return []

        pq = []
        heapq.heapify(pq)

        def dfs(cn: TreeNode):
            if not cn:
                return
            heapq.heappush(pq, (abs(target - cn.val), cn.val))
            dfs(cn.left)
            dfs(cn.right)

        dfs(root)
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(pq)[1])
        return ans

    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        # Approach1:
        # collect all nodes in order in an array. array will be sorted as it's BST
        # then binary search value closest to target
        # span out from there to find k values

        pass


T = TreeNode
rn = T(4)
rn.left, rn.right = T(2), T(5)
rn.left.left, rn.left.right = T(1), T(3)

rn1 = T(1)

assert Solution().closestKValues_1(rn, 3.71, 2) == [4, 3]
assert Solution().closestKValues_1(rn1, 0.0, 1) == [1]
print("Tests Passed!!")
