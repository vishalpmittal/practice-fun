/**
 * Tag: tree, recursive, stack
 * 
 * ---------------------------------------------
 * Find the sum of all left leaves in a given binary tree.
 * 
 * Example:
 * 
 * ....3
 * .../.\
 * ..9..20
 * ..../..\
 * ...15...7
 * 
 * There are two left leaves in the binary tree,
 * with values 9 and 15 respectively. Return 24.
 * ---------------------------------------------
 */

 package leetcode.algorithms.P4xx;

import static org.junit.Assert.assertTrue;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

import leetcode.dependencies.TreeNode;

public class P404_SumOfLeftLeaves {

    /* ---------------------------------------------
     * Recursive without helper method
     * --------------------------------------------- */
    public static int sumOfLeftLeaves_0(TreeNode root) {
        if (root == null)
            return 0;
        int l = 0;
        if (root.left != null)
            l = root.left.left == null && root.left.right == null ? root.left.val
                    : sumOfLeftLeaves(root.left);
        return l + sumOfLeftLeaves(root.right);
    }

    /* ---------------------------------------------
     * Recursive with helper method
     * --------------------------------------------- */
    public static int sumOfLeftLeaves_1(TreeNode root) {
        return sumOfLeftLeavesHelper(root, false);
    }

    public static int sumOfLeftLeavesHelper(TreeNode root, boolean b) {
        if (root == null)
            return 0;
        if (root.left == null && root.right == null) {
            if (b)
                return root.val;
            else
                return 0;
        }
        return sumOfLeftLeavesHelper(root.left, true)
                + sumOfLeftLeavesHelper(root.right, false);
    }

    /* ---------------------------------------------
     * Iterative Using a Stack
     * --------------------------------------------- */
    public static int sumOfLeftLeaves_2(TreeNode root) {
        int res = 0;

        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);

        while (!stack.isEmpty()) {
            TreeNode node = stack.pop();
            if (node != null) {
                if (node.left != null && node.left.left == null
                        && node.left.right == null)
                    res += node.left.val;
                stack.push(node.left);
                stack.push(node.right);
            }
        }
        return res;
    }

    /* ---------------------------------------------
     * Iterative Using a Queue
     * --------------------------------------------- */
    public static int sumOfLeftLeaves_3(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<>();
        int res = 0;
        TreeNode node = root;
        queue.offer(node);
        while (queue.size() != 0) {
            TreeNode head = queue.poll();
            if (head != null) {
                if (head.left != null && head.left.left == null
                        && head.left.right == null) {
                    res += head.left.val;
                }
                queue.offer(head.left);
                queue.offer(head.right);
            }
        }

        return res;
    }

    public static int sumOfLeftLeaves(TreeNode root) {
        return sumOfLeftLeaves_0(root);
    }

    public static void main(String[] args) {
        int[] nodes = new int[] { 3, 9, 20, 15, 7 };
        int[][] locations = new int[][] { new int[] { 1, 2 },
                new int[] { -1, -1 }, new int[] { 3, 4 } };

        TreeNode rn = TreeNode.makeMeATree(nodes, locations);
        assertTrue("Test1", sumOfLeftLeaves(rn) == 24);
        System.out.println("All Tests passed");
    }
}
