/**
 * Tag: math, array 
 *
 * Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
 * find the one that is missing from the array.
 * 
 * Example 1: Input: [3,0,1], Output: 2
 * Example 2: Input: [9,6,4,2,3,5,7,0,1], Output: 8
 * 
 * Note:
 * Your algorithm should run in linear runtime complexity. Could you implement it 
 * using only constant extra space complexity?
 */

package leetcode.algorithms.P2xx;

import static org.junit.Assert.assertTrue;

public class P268_MissingNumber {

    public static int missingNumber(int[] nums) {
        if (nums == null || nums.length == 0)
            return -1;

        int sum = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
        }
        return nums.length * (nums.length + 1) / 2 - sum;
    }

    public static void main(String[] args) {
        int[] arr1 = new int[] { 3, 0, 1 };
        int[] arr2 = new int[] { 9, 6, 4, 2, 3, 5, 7, 0, 1 };
        assertTrue("Test1", missingNumber(arr1) == 2);
        assertTrue("Test2", missingNumber(arr2) == 8);
        System.out.println("All Tests passed");
    }
}
