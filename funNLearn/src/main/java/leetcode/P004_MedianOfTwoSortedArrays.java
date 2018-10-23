/**
 * There are two sorted arrays nums1 and nums2 of size m and n respectively.
 * Find the median of the two sorted arrays. 
 * The overall run time complexity should be O(log (m+n)).
 * 
 * You may assume nums1 and nums2 cannot be both empty.
 * 
 * Example 1:
 * nums1 = [1, 3]
 * nums2 = [2]
 * The median is 2.0
 * 
 * Example 2:
 * nums1 = [1, 2]
 * nums2 = [3, 4]
 * The median is (2 + 3)/2 = 2.5
 */

package leetcode;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

public class P004_MedianOfTwoSortedArrays {
    
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        
        return 1;
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
