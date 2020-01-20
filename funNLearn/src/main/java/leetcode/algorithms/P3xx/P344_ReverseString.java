/** 
 * Tag: string
 *
 * Write a function that takes a string as input and returns the string reversed.
 */

package leetcode.algorithms.P3xx;

import static org.junit.Assert.assertTrue;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

public class P344_ReverseString {
	// Recursive, also calculate length once
	public static String reverseString_1(String s) {
		return reverseString_1(s, s.length());
	}

	public static String reverseString_1(String s, int len) {
		if (s == null || len <= 1)
			return s;
		return s.charAt(len - 1) + reverseString_1(s.substring(0, len - 1), len - 1);
	}

	// Better Recursive, also calculate length once
	public static String reverseString_2(String s) {
		int len = s.length();
		if (s == null || len <= 1)
			return s;
		String leftStr = s.substring(0, len / 2);
		String rightStr = s.substring(len / 2, len);
		return reverseString_2(rightStr) + reverseString_2(leftStr);
	}

	// Iterative
	public static String reverseString_3(String s) {
		char[] ca = s.toCharArray();
		int len = s.length();
		for (int i = 0; i < (len / 2); i++) {
			char temp = ca[i];
			ca[i] = ca[len - 1 - i];
			ca[len - 1 - i] = temp;
		}
		return String.valueOf(ca);
	}

	public static String reverseString(String s) {
		return reverseString_2(s);
	}

	@Test
	public void test() {
		//		System.out.println(reverseString("vishal"));
		assertTrue("Test1", reverseString("vishal").compareTo("lahsiv") == 0);
		assertTrue("Test1", reverseString("poorva").compareTo("avroop") == 0);
	}

	public static void main(String[] args) {
		Result result = JUnitCore.runClasses(P344_ReverseString.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}
}
