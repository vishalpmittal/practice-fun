/** 
 * Tag: array
 * 
 * ---------------------------------------------
 * Given two arrays, write a function to compute their intersection.
 * 
 * Example:
 * Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
 * 
 * Note:
 *  -  Each element in the result should appear as many times as it shows in both arrays.
 *  -  The result can be in any order.
 * 
 * Follow up:
 *  -  What if the given array is already sorted? How would you optimize your algorithm?
 *  -  What if nums1's size is small compared to nums2's size? Which algorithm is better?
 *  -  What if elements of nums2 are stored on disk, and the memory is limited such that 
 *     you cannot load all elements into the memory at once?
 *  --------------------------------------------- */

package leetcode.algorithms.P301_P400;

import static org.junit.Assert.assertTrue;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

public class P350_IntersectionOfTwoArrays_II {

    /*
     * ---------------------------------------------
     * using Java HashMap
     * ---------------------------------------------
     */
    public static int[] intersection_II_1(int[] nums1, int[] nums2) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        ArrayList<Integer> result = new ArrayList<Integer>();
        for (int i = 0; i < nums1.length; i++) {
            if (map.containsKey(nums1[i]))
                map.put(nums1[i], map.get(nums1[i]) + 1);
            else
                map.put(nums1[i], 1);
        }

        for (int i = 0; i < nums2.length; i++) {
            if (map.containsKey(nums2[i]) && map.get(nums2[i]) > 0) {
                result.add(nums2[i]);
                map.put(nums2[i], map.get(nums2[i]) - 1);
            }
        }

        int[] r = new int[result.size()];
        for (int i = 0; i < result.size(); i++) {
            r[i] = result.get(i);
        }

        return r;
    }

    /*
     * ---------------------------------------------
     * using Sorting
     * ---------------------------------------------
     */
    public static int[] intersection_II_2(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        int pnt1 = 0;
        int pnt2 = 0;
        ArrayList<Integer> myList = new ArrayList<Integer>();
        while ((pnt1 < nums1.length) && (pnt2 < nums2.length)) {
            if (nums1[pnt1] < nums2[pnt2]) {
                pnt1++;
            } else {
                if (nums1[pnt1] > nums2[pnt2]) {
                    pnt2++;
                } else {
                    myList.add(nums1[pnt1]);
                    pnt1++;
                    pnt2++;
                }
            }
        }
        int[] res = new int[myList.size()];
        for (int i = 0; i < res.length; i++) {
            res[i] = (Integer) myList.get(i);
        }
        return res;
    }

    /*
     * ---------------------------------------------
     * Answer to part three:
     * 
     * - If only nums2 cannot fit in memory, put all elements of nums1 into a HashMap,
     * read chunks of array that fit into the memory, and record the intersections.
     * 
     * - If both nums1 and nums2 are so huge that neither fit into the memory, sort them
     * individually (external sort), then read 2 elements from each array at a time in memory,
     * record intersections.
     * 
     * -----------------
     * From a data engineer's perspective, basically there are three ideas to solve the question:
     * 1. Store the two strings in distributed system(whether self designed or not),
     * then using MapReduce technique to solve the problem;
     * 
     * 2. Processing the Strings by chunk, which fits the memory,
     * then deal with each chunk of data at a time;
     * 
     * 3. Processing the Strings by streaming, then check.
     * ---------------------------------------------
     */

    public static int[] intersection_II(int[] nums1, int[] nums2) {
        return intersection_II_1(nums1, nums2);
    }

    public static void main(String[] args) {
        int[] nums1 = { 1, 2, 2, 1 };
        int[] nums2 = { 2, 2 };
        int[] exp = { 2, 2 };

        assertTrue("Test1", Arrays.equals(intersection_II_1(nums1, nums2), exp));
        assertTrue("Test1", Arrays.equals(intersection_II_2(nums1, nums2), exp));
        System.out.println("All Tests passed");
    }
}
