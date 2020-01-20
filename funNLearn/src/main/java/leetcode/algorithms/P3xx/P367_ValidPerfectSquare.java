/**
 * Tag: math
 * 
 * Given a positive integer num, write a function which returns True if num 
 * is a perfect square else False.
 * 
 * Note: Do not use any built-in library function such as sqrt.
 * 
 * Example 1: Input: 16, Output: true
 * Example 2: Input: 14, Output: false
 * 
 */

package leetcode.algorithms.P3xx;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

public class P367_ValidPerfectSquare {

    /* a square number is 1+3+5+7+...
     * Time Complexity O(sqrt(N)) */
    public boolean isPerfectSquare_v1(int num) {
        if (num < 1)
            return false;
        for (int i = 1; num > 0; i += 2)
            num -= i;
        return num == 0;
    }

    // binary search. Time Complexity O(logN)
    public boolean isPerfectSquare_v2(int num) {
        if (num < 1)
            return false;

        // long type to avoid 2147483647 case
        long left = 1, right = num;

        while (left <= right) {
            long mid = left + (right - left) / 2;
            long t = mid * mid;
            if (t > num) {
                right = mid - 1;
            } else if (t < num) {
                left = mid + 1;
            } else {
                return true;
            }
        }

        return false;
    }

    /* Newton Method.
     * Time Complexity is close to constant, given a positive integer.
     * Find the square root of num and square the integer */
    public boolean isPerfectSquare_v3(int num) {
        long t = num;
        while (t * t > num) {
            t = (t + num / t) / 2;
        }
        return t * t == num;
    }

    public static boolean problem_1(int n) {
        return false;
    }

    public static boolean problem(int n) {
        return problem_1(n);
    }

    public static void main(String[] args) {
        assertTrue("Test1", problem(94));
        assertFalse("Test2", problem(97));
        System.out.println("All Tests passed");
    }
}
