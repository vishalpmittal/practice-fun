/*
 * Tag: integer, bit, math
 * 
 * Given an integer, write a function to determine if it is a power of three.
 * 
 * Example 1: Input: 27, Output: true
 * Example 2: Input: 0, Output: false
 * Example 3: Input: 9, Output: true
 * Example 4: Input: 45, Output: false
 * 
 * Follow up: 
 * Could you do it without using any loop / recursion?
 */

package leetcode.algorithms.P3xx;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;

public class P326_PowerOfThree {
	// Recursive O(log n)
	public static boolean isPowerOfThree_1(int n) {
		if (n == 0 || n == 2)
			return false;
		if (n == 1 || n == 3)
			return true;
		if (n % 3 == 0)
			return isPowerOfThree_1(n / 3);
		return false;
	}

	// Iterative solution
	public static boolean isPowerOfThree_2(int n) {
		if (n > 1)
			while (n % 3 == 0)
				n /= 3;
		return n == 1;
	}

	// 1162261467 is 3^19,  3^20 is bigger than int
	// or use following to find max int 3's power
	// int maxPowerOfThree = (int)Math.pow(3, (int)(Math.log(0x7fffffff) / Math.log(3)));
	public static boolean isPowerOfThree_3(int n) {
		return (n > 0 && 1162261467 % n == 0);
	}

	// log10(243) = 2.385606273598312    log10(3) = 0.47712125471966244
	//	   	==> log10(243)/log10(3) = 5.0
	public static boolean isPowerOfThree_4(int n) {
		return (Math.log10(n) / Math.log10(3)) % 1 == 0;
	}

	// convert the original number into radix-3 format and 
	// check if it is of format 10* where 0* means k zeros with k>=0
	public static boolean isPowerOfThree_5(int n) {
		return Integer.toString(n, 3).matches("10*");
	}

	public static boolean isPowerOfThree(int n) {
		return isPowerOfThree_2(n);
	}

	@Test
	public void test() {
		assertTrue("Test1", isPowerOfThree(81));
		assertFalse("Test2", isPowerOfThree(82));
	}

	public static void main(String[] args) {
		Result result = JUnitCore.runClasses(P326_PowerOfThree.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}

}
