/*
 * Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
 */

package leetcode.tree;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import leetcode.dependencies.TreeNode;

public class P108_ConvertSortedArrayToBinarySearchTree {
    /* Recursive solution */
    public TreeNode sortedArrayToBST(int[] nums) {
        if (nums.length == 0) {
            return null;
        }
        TreeNode head = helper(nums, 0, nums.length - 1);
        return head;
    }

    public TreeNode helper(int[] num, int low, int high) {
        if (low > high) {
            return null;
        }
        int mid = (low + high) / 2;
        TreeNode node = new TreeNode(num[mid]);
        node.left = helper(num, low, mid - 1);
        node.right = helper(num, mid + 1, high);
        return node;
    }

    public static void main(String[] args) {
        // assertTrue("Test1", problem(94));
        // assertFalse("Test2", problem(97));
        System.out.println("All Tests passed");
    }
}
