/**
 * Tag: math
 * 
 * Given an integer n, return the number of trailing zeroes in n!.
 * Note: Your solution should be in logarithmic time complexity.
 */

package dsAlgo.leetcode.P1xx;

import static org.junit.Assert.assertTrue;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

public class P172_FactorialTrailingZeroes {
	/*
	 * Because all trailing 0 is from factors 5 * 2.
	 * But sometimes one number may have several 5 factors, for example, 
	 * 25 have two 5 factors, 125 have three 5 factors. In the n! operation, 
	 * factors 2 is always ample. So we just count how many 5 factors in all 
	 * number from 1 to n. 
	 */
	public static int trailingZeroes(int n) {
		return n == 0 ? 0 : n / 5 + trailingZeroes(n / 5);
	}

	@Test
	public void test() {
		assertTrue("Test1", trailingZeroes(8) == 1);
		assertTrue("Test2", trailingZeroes(10) == 2);
	}

	public static void main(String[] args) {
		Result result = JUnitCore.runClasses(P172_FactorialTrailingZeroes.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}
}
