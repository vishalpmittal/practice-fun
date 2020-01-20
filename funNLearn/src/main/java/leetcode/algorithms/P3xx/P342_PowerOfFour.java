/**
 * 
 * Tag: integer, bit, math
 *
 * Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
 * 
 * Example:
 * Given num = 16, return true. Given num = 5, return false.
 * 
 * Follow up: Could you solve it without loops/recursion?
 */

package leetcode.algorithms.P3xx;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;

public class P342_PowerOfFour {
	//
	public static boolean isPowerOfFour_1(int num) {
		while (num > 4) {
			if (num % 4 != 0)
				return false;
			else
				num = num / 4;
		}
		return num == 4 || num == 1 ? true : false;
	}
	
	// convert the original number into radix-4 format and 
	// check if it is of format 10* where 0* means k zeros with k>=0
	public static boolean isPowerOfFour_2(int num) {
		return Integer.toString(num, 4).matches("10*");
	}

	/*
	 * The basic idea is from power of 2, We can use "n&(n-1) == 0" to determine 
	 * if n is power of 2. For power of 4, the additional restriction is that in 
	 * binary form, the only "1" should always located at the odd position. 
	 * For example, 4^0 = 1, 4^1 = 100, 4^2 = 10000. So we can use "num & 0x55555555==num" 
	 * to check if "1" is located at the odd position.
	 */
	public static boolean isPowerOfFour_3(int num) {
		return (num > 0) && ((num & (num - 1)) == 0) && ((num & 0x55555555) == num);
	}
	
	public static boolean isPowerOfFour(int n) {
		return isPowerOfFour_2(n);
	}

	@Test
	public void test() {
		assertTrue("Test1", isPowerOfFour(16));
		assertTrue("Test1", isPowerOfFour(1));
		assertFalse("Test2", isPowerOfFour(15));
	}

	public static void main(String[] args) {
		Result result = JUnitCore.runClasses(P342_PowerOfFour.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}
}
