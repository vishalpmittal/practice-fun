/*
 * You are a professional robber planning to rob houses along a street. 
 * Each house has a certain amount of money stashed, the only constraint stopping 
 * you from robbing each of them is that adjacent houses have security system 
 * connected and it will automatically contact the police if two adjacent houses 
 * were broken into on the same night.
 * 
 * Given a list of non-negative integers representing the amount of money of each house, 
 * determine the maximum amount of money you can rob tonight without alerting the police.
 * 
 */

package leetcode.dp;

import static org.junit.Assert.assertTrue;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

public class P198_HouseRobber {
	public static int rob_1(int[] nums) {
		int sum1 = 0, sum2 = 0;
		for (int i = 0; i < nums.length; i++) {
			if (i % 2 == 0)
				sum1 = Math.max(sum1 + nums[i], sum2);
			else
				sum2 = Math.max(sum2 + nums[i], sum1);
		}
		return Math.max(sum1, sum2);
	}

	// DP solution
	public static int rob_2(int[] nums) {
		//max monney can get if rob current house
		int rob = 0;

		//max money can get if not rob current house
		int notrob = 0;

		for (int i = 0; i < nums.length; i++) {
			//if rob current value, previous house must not be robbed
			int currob = notrob + nums[i];

			//if not rob ith house, take the max value of robbed (i-1)th house and not rob (i-1)th house
			notrob = Math.max(notrob, rob);
			
			rob = currob;
		}
		return Math.max(rob, notrob);

	}

	public static int rob(int[] nums) {
		return rob_1(nums);
	}

	@Test
	public void test() {
		assertTrue("Test1", rob(new int[] { 1, 2, 3, 4, 5, 6 }) == 12);
		assertTrue("Test2", rob(new int[] { 1, 2, 3, 4, 5 }) == 9);
		assertTrue("Test3", rob(new int[] { 2, 1, 1, 2 }) == 4);
	}

	public static void main(String[] args) {
		Result result = JUnitCore.runClasses(P198_HouseRobber.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}
}
