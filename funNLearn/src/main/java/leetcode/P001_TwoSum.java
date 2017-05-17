/**
 * Given an array of integers, 
 * return indices of the two numbers such that they add up to a specific target.
 * You may assume that each input would have exactly one solution.
 * 
 * Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
 */
package leetcode;

import java.util.Arrays;
import java.util.HashMap;

public class P001_TwoSum {
    /* O(n^2) runtime, O(1) space – Brute force:
     * The brute force approach is simple. Loop through each element
     * x and find if there is another value that equals to target – x.
     * As finding another value requires looping through the rest of
     * array, its runtime complexity is O(n2). */
    public static int[] twoSum(int[] nums, int target) {
        int[] indexes = new int[2];
        for (int x = 0; x < nums.length - 1; x++) {
            for (int y = x + 1; y < nums.length; y++) {
                if (nums[x] + nums[y] == target) {
                    indexes[0] = x;
                    indexes[1] = y;
                    return indexes;
                }
            }
        }
        return indexes;
    }

    /* O(n) runtime, O(n) space – Hash table:
     * We could reduce the runtime complexity of looking up a value
     * to O(1) using a hash map that maps a value to its index. */
    public static int[] twoSum2(int[] nums, int target) {
        int[] indexes = new int[2];
        HashMap<Integer, Integer> hm = new HashMap<Integer, Integer>();

        for (int x = 0; x < nums.length; x++) {
            if (hm.containsKey(target - nums[x])) {
                indexes[0] = hm.get(target - nums[x]);
                indexes[1] = x;
                return indexes;
            } else {
                hm.put(nums[x], x);
            }
        }
        return indexes;
    }

    public static void main(String args[]) {
        int[] nums = { 2, 11, 15, 7 };
        System.out.println(Arrays.toString(twoSum2(nums, 9)));
    }

}
