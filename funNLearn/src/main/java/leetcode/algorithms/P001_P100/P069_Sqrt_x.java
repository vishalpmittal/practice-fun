/**
 * Tag: integer, math
 * 
 * Implement int sqrt(int x).
 * Compute and return the square root of x.
 */

package leetcode.algorithms.P001_P100;

import static org.junit.Assert.assertTrue;

public class P069_Sqrt_x {

    /* Integer newton method */
    public static int mySqrt(int x) {
        long r = x;
        while (r * r > x) {
            r = (r + x / r) / 2;
        }
        return (int) r;
    }

    /* A Binary Search Solution */
    public static int sqrt(int x) {
        if (x == 0)
            return 0;
        int left = 1, right = Integer.MAX_VALUE;
        while (true) {
            int mid = left + (right - left) / 2;
            if (mid > x / mid) {
                right = mid - 1;
            } else {
                if (mid + 1 > x / (mid + 1))
                    return mid;
                left = mid + 1;
            }
        }
    }

    public static void main(String[] args) {
        assertTrue("Test1", mySqrt(9) == 3);
        assertTrue("Test1", mySqrt(10) == 3);
        assertTrue("Test1", sqrt(9) == 3);
        assertTrue("Test1", sqrt(10) == 3);
        System.out.println("All Tests passed");
    }

}
