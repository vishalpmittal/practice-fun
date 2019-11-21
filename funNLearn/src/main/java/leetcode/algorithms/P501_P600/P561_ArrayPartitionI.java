/*
 * Given an array of 2n integers, your task is to group these integers into n pairs of 
 * integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all 
 * i from 1 to n as large as possible.
 * 
 * Example 1:
 * Input: [1,4,3,2]
 * 
 * Output: 4
 * Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
 * 
 * Note:
 * n is a positive integer, which is in the range of [1, 10000].
 * All the integers in the array will be in the range of [-10000, 10000].
 */

package leetcode.algorithms.P501_P600;

import static org.junit.Assert.assertTrue;

import java.util.Arrays;

public class P561_ArrayPartitionI {

    /* first sort the input array and then the sum of 1st, 3rd, 5th..., is the answer.
     * - Assume in each pair i, bi >= ai.
     * - Denote Sm = min(a1, b1) + min(a2, b2) + ... + min(an, bn). The biggest Sm is the answer
     * of this problem. Given 1, Sm = a1 + a2 + ... + an.
     * - Denote Sa = a1 + b1 + a2 + b2 + ... + an + bn. Sa is constant for a given input.
     * - Denote di = |ai - bi|. Given 1, di = bi - ai. Denote Sd = d1 + d2 + ... + dn.
     * - So Sa = a1 + a1 + d1 + a2 + a2 + d2 + ... + an + an + di = 2Sm + Sd => Sm = (Sa - Sd) / 2.
     * - To get the max Sm, given Sa is constant, we need to make Sd as small as possible.
     * - So this problem becomes finding pairs in an array that makes sum of di (distance between ai and bi) as small as
     * possible.
     * - Apparently, sum of these distances of adjacent elements is the smallest. */

    public static int arrayPairSum(int[] nums) {
        Arrays.sort(nums);
        int result = 0;
        for (int i = 0; i < nums.length; i += 2) {
            result += nums[i];
        }
        return result;
    }

    /* create a Hash of all the numbers, browse through the hash and keep adding every alternative number
     * also consider duplicates while adding */
    public static int arrayPairSum_fast(int[] nums) {
        int[] hash = new int[20001];
        for (int ele : nums) {
            hash[ele + 10000]++;
        }
        int sum = 0;
        int p = 0;
        for (int i = 0; i < 20001; i++) {
            if (hash[i] == 0)
                continue;
            while (hash[i] != 0) {
                if (p % 2 == 0) {
                    sum += (i - 10000);
                }
                p++;
                hash[i]--;
            }
        }
        return sum;
    }

    public static int problem(int[] nums) {
        // return arrayPairSum(nums);
        return arrayPairSum_fast(nums);
    }

    public static void main(String[] args) {
        int[] arr = { 1, 4, 3, 2 };
        assertTrue("Test1", problem(arr) == 4);
        System.out.println("All Tests passed");
    }
}
