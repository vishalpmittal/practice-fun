/** 
 * Tag: tree
 * 
 * ---------------------------------------------
 * You are given a binary tree in which each node contains an integer value.
 * Find the number of paths that sum to a given value.
 * 
 * -  The path does not need to start or end at the root or a leaf, but it must 
 * ...go downwards (traveling only from parent nodes to child nodes).
 * 
 * -  The tree has no more than 1,000 nodes and the values are in the 
 * range -1,000,000 to 1,000,000.
 * 
 * Example:
 * root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
 * 
 * ......10
 * ...../..\
 * ....5...-3
 * .../.\....\
 * ..3...2...11
 * ./.\...\
 * 3..-2...1
 * 
 * Return 3. The paths that sum to 8 are:
 * 1.  5 -> 3
 * 2.  5 -> 2 -> 1
 * 3. -3 -> 11
 * --------------------------------------------- */

package dsAlgo.leetcode.P4xx;

import dsAlgo.leetcode.dependencies.TreeNode;

public class P437_PathSumIII {
    int count = 0;

    /**
     * Solution by anubhavjindal
     * https://leetcode.com/problems/path-sum-iii/discuss/428690/JAVA-I-call-it-DFSception
     * 
     * Its basically DFS treating each node as root node like recursion in recursion
     * In an alternate solution a stack can be used to do the first recursion
     */
    public int pathSum(TreeNode root, int sum) {
        if (root == null)
            return 0;
        dfs(root, 0, sum);
        pathSum(root.right, sum);
        pathSum(root.left, sum);
        return count;
    }

    public void dfs(TreeNode root, int current, int target) {
        if (root == null)
            return;
        if (current + root.val == target)
            count++;
        dfs(root.right, current + root.val, target);
        dfs(root.left, current + root.val, target);
    }

    public static void main(String[] args) {
        System.out.println("All Tests passed");
    }
}
