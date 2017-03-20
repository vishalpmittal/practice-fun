/*
 * Find the contiguous subarray within an array (containing at least one number) 
 * which has the largest sum.
 * 
 * For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
 * the contiguous subarray [4,-1,2,1] has the largest sum = 6.
 * 
 * More practice.
 * If you have figured out the O(n) solution, try coding another solution using the 
 * divide and conquer approach, which is more subtle.
 */

package leetcode;

import static org.junit.Assert.assertTrue;

public class P053_MaximumSubarray {

    public static int maxSubArray(int[] nums) {
        if (nums.length == 0)
            return 0;
        else if (nums.length == 1)
            return nums[0];

        int beg = 0;
        int end = 1;

        int runSum = nums[beg];
        int maxSum = runSum;

        System.out.println(String.format("%-20s|%-20s|%-20s|%-20s", "beg", "end", "maxSum", "runSum"));
        while (end < nums.length) {
            System.out.println(String.format("%-20d|%-20d|%-20d|%-20d", beg, end, maxSum, runSum));
            if (runSum + nums[end] >= runSum) {
                runSum += nums[end];
                end++;
            } else {
                beg = ++end;
                end++;
                runSum = nums[beg];
            }

            maxSum = maxSum > runSum ? maxSum : runSum;
        }

        return maxSum;
    }

    public static void main(String[] args) {
        int[] arr = { -2, 1, -3, 4, -1, 2, 1, -5, 4 };
        assertTrue("Test1", maxSubArray(arr) == 6);
        System.out.println("All Tests passed");
    }
}
