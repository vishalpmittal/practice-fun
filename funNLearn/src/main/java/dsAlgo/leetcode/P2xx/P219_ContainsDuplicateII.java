/**
 * Tag: array
 *
 * Given an array of integers and an integer k, find out whether there 
 * are two distinct indices i and j in the array such that nums[i] = nums[j] 
 * and the difference between i and j is at most k.
 */

package dsAlgo.leetcode.P2xx;

import static org.junit.Assert.assertTrue;

import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

public class P219_ContainsDuplicateII {

	public boolean containsNearbyDuplicate_1(int[] nums, int k) {
		HashMap<Integer, Integer> loc = new HashMap<Integer, Integer>();
		for (int i = 0; i < nums.length; i++) {
			if (loc.containsKey(nums[i])) {
				if (i - loc.get(nums[i]) <= k) {
					return true;
				}
			} else
				loc.put(nums[i], i);
		}
		return false;
	}

	public boolean containsNearbyDuplicate_2(int[] nums, int k) {
		Set<Integer> set = new HashSet<Integer>();
		for (int i = 0; i < nums.length; i++) {
			if (i > k)
				set.remove(nums[i - k - 1]);
			if (!set.add(nums[i]))
				return true;
		}
		return false;
	}

	public boolean containsNearbyDuplicate_3(int[] nums, int k) {
		int[] locs = new int[Integer.MAX_VALUE];
		Arrays.fill(locs, -1);
		for (int i = 0; i < nums.length; i++) {
			if (locs[nums[i]] != -1) {
				if (i - locs[nums[i]] <= k) {
					return true;
				}
			} else
				locs[nums[i]] = i;
		}
		return false;
	}

	@Test
	public void test() {
		int[] arr = { 1, 2, 3, 4, 5, 6, 7, 8, 1, 5, 4, 6 };
		assertTrue("Test1", containsNearbyDuplicate_1(arr, 3));
	}

	public static void main(String[] args) {
		Result result = JUnitCore.runClasses(P219_ContainsDuplicateII.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}
}
