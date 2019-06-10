/**
 * Tag: Math
 * 
 * A strobogrammatic number is a number that looks the same when 
 * rotated 180 degrees (looked at upside down).
 * 
 * Write a function to determine if a number is strobogrammatic. 
 * The number is represented as a string.
 * 
 * For example, the numbers "69", "88", and "818" are all strobogrammatic.
 */

package leetcode.algorithms.P201_P300;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

public class P246_StrobogrammaticNumber {

	public static boolean isStrobogrammatic(String num) {
		int[] spairs = { 0, 1, -1, -1, -1, -1, 9, -1, 8, 6 };
		int len = num.length();
		int i = 0;
		for (i = 0; i <= len / 2; i++) {
			if (spairs[Character.getNumericValue(num.charAt(i))] != Character
					.getNumericValue(num.charAt(len - 1 - i))) {
				return false;
			}
		}
		return true;
	}

	public static void main(String[] args) {
		assertTrue("Test1", isStrobogrammatic("1"));
		assertTrue("Test1", isStrobogrammatic("69"));
		assertFalse("Test1", isStrobogrammatic("44"));
		assertTrue("Test1", isStrobogrammatic("88"));
		assertTrue("Test1", isStrobogrammatic("818"));
		assertFalse("Test1", isStrobogrammatic("848"));
		assertFalse("Test1", isStrobogrammatic("3"));
		assertFalse("Test1", isStrobogrammatic("6"));

		System.out.println("All Tests passed");
	}
}
