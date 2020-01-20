/**
 * Tag: math
 *
 * Given an integer, write a function to determine if it is a power of two.
 */

package leetcode.algorithms.P2xx;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;

public class P231_PowerOfTwo {
	/*
	 * Recursive solution O(log n)
	 */
	public static boolean isPowerOfTwo_1(int n) {
		if (n == 0)
			return false;
		if (n == 1 || n == 2)
			return true;
		if (n % 2 == 0)
			return isPowerOfTwo_1(n / 2);
		return false;
	}

	/*
	 * Bit Manipulation
	 * Power of 2 means only one bit of n is '1', 
	 * so use the trick n&(n-1)==0 to judge whether that is the case
	 */
	public static boolean isPowerOfTwo_2(int n) {
		return ((n & (n-1))==0 && n>0);
	}

	public static boolean isPowerOfTwo(int n) {
		return isPowerOfTwo_2(n);
	}

	@Test
	public void test() {
		assertTrue("Test1", isPowerOfTwo(8));
		assertTrue("Test2", isPowerOfTwo(16));
		assertFalse("Test3", isPowerOfTwo(25));
	}

	public static void main(String[] args) {
		Result result = JUnitCore.runClasses(P231_PowerOfTwo.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}

}
