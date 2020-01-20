/** 
 * Tag: array
 * 
 * ---------------------------------------------
 * Given two arrays, write a function to compute their intersection.
 * 
 * Example:
 * Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
 * 
 * Note:
 * Each element in the result must be unique.
 * The result can be in any order. 
--------------------------------------------- */

package leetcode.algorithms.P3xx;

import static org.junit.Assert.assertTrue;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class P349_IntersectionOfTwoArrays {
    /*
     * ---------------------------------------------
     * Use two hash sets, Time complexity: O(n)
     * ---------------------------------------------
     */
    public static int[] intersection_1(int[] nums1, int[] nums2) {
        Set<Integer> set = new HashSet<>();
        Set<Integer> intersect = new HashSet<>();
        for (int i = 0; i < nums1.length; i++) {
            set.add(nums1[i]);
        }
        for (int i = 0; i < nums2.length; i++) {
            if (set.contains(nums2[i])) {
                intersect.add(nums2[i]);
            }
        }
        int[] result = new int[intersect.size()];
        int i = 0;
        for (Integer num : intersect) {
            result[i++] = num;
        }
        return result;
    }

    /*
     * ---------------------------------------------
     * Sort both arrays, use two pointers
     * Time complexity: O(nlogn)
     * ---------------------------------------------
     */
    public static int[] intersection_2(int[] nums1, int[] nums2) {
        Set<Integer> set = new HashSet<>();
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        int i = 0;
        int j = 0;
        while (i < nums1.length && j < nums2.length) {
            if (nums1[i] < nums2[j]) {
                i++;
            } else if (nums1[i] > nums2[j]) {
                j++;
            } else {
                set.add(nums1[i]);
                i++;
                j++;
            }
        }
        int[] result = new int[set.size()];
        int k = 0;
        for (Integer num : set) {
            result[k++] = num;
        }
        return result;
    }

    /*
     * ---------------------------------------------
     * Binary search
     * Time complexity: O(nlogn)
     * ---------------------------------------------
     */
    public static int[] intersection_3(int[] nums1, int[] nums2) {
        Set<Integer> set = new HashSet<>();
        Arrays.sort(nums2);
        for (Integer num : nums1) {
            if (binarySearch(nums2, num)) {
                set.add(num);
            }
        }
        int i = 0;
        int[] result = new int[set.size()];
        for (Integer num : set) {
            result[i++] = num;
        }
        return result;
    }

    public static boolean binarySearch(int[] nums, int target) {
        int low = 0;
        int high = nums.length - 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (nums[mid] == target) {
                return true;
            }
            if (nums[mid] > target) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return false;
    }

    public static int[] intersection(int[] nums1, int[] nums2) {
        return intersection_1(nums1, nums2);
    }

    public static void main(String[] args) {
        int[] nums1 = { 1, 2, 2, 1 };
        int[] nums2 = { 2, 2 };
        int[] exp = { 2 };

        assertTrue("Test1", Arrays.equals(intersection_1(nums1, nums2), exp));
        assertTrue("Test1", Arrays.equals(intersection_2(nums1, nums2), exp));
        assertTrue("Test1", Arrays.equals(intersection_3(nums1, nums2), exp));
        System.out.println("All Tests passed");
    }
}
