/** 
 * Tag: array, dp
 * 
 * ---------------------------------------------
 * Given an array of integers A and let n to be its length.
 * 
 * Assume Bk to be an array obtained by rotating the array A k positions 
 * clock-wise, we define a "rotation function" F on A as follow:
 * 
 * F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].
 * 
 * Calculate the maximum value of F(0), F(1), ..., F(n-1).
 * 
 * Note:
 * n is guaranteed to be less than 105.
 * 
 * Example: A = [4, 3, 2, 6]
 * 
 * F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
 * F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
 * F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
 * F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
 * 
 * So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.
 * --------------------------------------------- */


package dsAlgo.leetcode.P3xx;

import static org.junit.Assert.assertTrue;

public class P396_RotateFunction {
    /* ---------------------------------------------
     * O(n2) solution ... memory table
     * ---------------------------------------------
     * i , ae , j , sum , max
     * 0 0 0 0 -2147483648
     * 0 1 1 3 -2147483648
     * 0 2 2 7 -2147483648
     * 0 3 3 25 -2147483648
     * 1 3 0 0 25
     * 1 0 1 4 25
     * 1 1 2 10 25
     * 1 2 3 16 25
     * 2 2 0 0 25
     * 2 3 1 6 25
     * 2 0 2 14 25
     * 2 1 3 23 25
     * 3 1 0 0 25
     * 3 2 1 2 25
     * 3 3 2 14 25
     * 3 0 3 26 25
     * 26 26
     * --------------------------------------------- */
    public static int maxRotateFunction_1(int[] A) {
        if (A.length == 0)
            return 0;

        int max = Integer.MIN_VALUE;

        for (int i = 0; i < A.length; i++) {
            int sum = 0;
            int ae = i == 0 ? 0 : A.length - i;

            for (int j = 0; j < A.length; j++) {
                sum += (A[ae] * j);
                ae = ae < A.length - 1 ? ++ae : 0;
            }
            max = Math.max(max, sum);
        }
        return max;
    }

    /* ---------------------------------------------
     * O(n) solution ...from leetcode
     * ---------------------------------------------
     * Consider we have 5 coins A,B,C,D,E
     * 
     * According to the problem statement
     * F(0) = (0A) + (1B) + (2C) + (3D) + (4E)
     * F(1) = (4A) + (0B) + (1C) + (2D) + (3E)
     * F(2) = (3A) + (4B) + (0C) + (1D) + (2*E)
     * 
     * This problem at a glance seem like a difficult problem.
     * 
     * We can construct F(1) from F(0) by two step:
     * 
     * Step 1. taking away one count of each coin from F(0), this is done by
     * subtracting "sum" from "iteration" in the code below:
     * after step 1 F(0) = (-1A) + (0B) + (1C) + (2D) + (3*E)
     * 
     * Step 2. Add n times the element which didn't contributed in F(0), which is A.
     * This is done by adding "A[j-1]len" in the code below.
     * after step 2 F(0) = (4A) + (0B) + (1C) + (2D) + (3E)
     * 
     * At this point F(0) can be considered as F(1) and F(2) to F(4) can be
     * constructed by repeating the above steps.
     * --------------------------------------------- */
    public static int maxRotateFunction_2(int[] A) {
        if (A.length == 0) {
            return 0;
        }

        int sum = 0, iteration = 0, len = A.length;

        for (int i = 0; i < len; i++) {
            sum += A[i];
            iteration += (A[i] * i);
        }

        int max = iteration;
        for (int j = 0; j < len; j++) {
            // for next iteration lets remove one entry value of each
            // entry and the prev 0 * k
            iteration = iteration - sum + A[j] * len;
            max = Math.max(max, iteration);
        }
        return max;
    }

    public static void main(String[] args) {
        int[] arr = { 4, 3, 2, 6 };
        assertTrue("Test1", maxRotateFunction_1(arr) == 26);
        assertTrue("Test1", maxRotateFunction_2(arr) == 26);
        System.out.println("All Tests passed");
    }
}
