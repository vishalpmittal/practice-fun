/*
 * Given an integer array nums, find the sum of the elements between 
 * indices i and j (i ≤ j), inclusive.
 * 
 * Example:
 * Given nums = [-2, 0, 3, -5, 2, -1]
 * sumRange(0, 2) -> 1
 * sumRange(2, 5) -> -1
 * sumRange(0, 5) -> -3
 * 
 * Note:
 * You may assume that the array does not change.
 * There are many calls to sumRange function.
 */

package leetcode.lists;

import static org.junit.Assert.assertTrue;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

public class P303_RangeSumQueryImmutable {
	int[] nums;

	// O(N) Initialization and O(1) sum range
	public P303_RangeSumQueryImmutable(int[] nums) {
		for (int i = 1; i < nums.length; i++)
			nums[i] += nums[i - 1];

		this.nums = nums;
	}

	public int sumRange(int i, int j) {
		if (i == 0)
			return nums[j];

		return nums[j] - nums[i - 1];
	}

	@Test
	public void test() {
		int[] nums = { -2, 0, 3, -5, 2, -1 };
		P303_RangeSumQueryImmutable numArray = new P303_RangeSumQueryImmutable(nums);

		assertTrue("Test1", numArray.sumRange(0, 2) == 1);
		assertTrue("Test1", numArray.sumRange(2, 5) == -1);
		assertTrue("Test1", numArray.sumRange(0, 5) == -3);
	}

	public static void main(String[] args) {
		Result result = JUnitCore.runClasses(P303_RangeSumQueryImmutable.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}
}
