/*
 * The count-and-say sequence is the sequence of integers beginning as follows:
 * 1, 11, 21, 1211, 111221, ...
 * 
 * 1 is read off as "one 1" or 11.
 * 11 is read off as "two 1s" or 21.
 * 21 is read off as "one 2, then one 1" or 1211.
 * Given an integer n, generate the nth sequence.
 * 
 * Note: The sequence of integers will be represented as a string.
 */

package dsAlgo.leetcode.P0xx;

import static org.junit.Assert.assertTrue;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

public class P038_CountAndSay {
	public static String countAndSay(int n) {
		String prev = "1";
		for (int i = 2; i <= n; i++) {
			String curr = "";
			int digit = Character.getNumericValue(prev.charAt(0));
			int count = 1;
			for (int j = 1; j < prev.length(); j++) {
				if (Character.getNumericValue(prev.charAt(j)) == digit) {
					count++;
				} else {
					curr = curr + count + digit;
					count = 1;
					digit = Character.getNumericValue(prev.charAt(j));
				}
			}
			prev = curr + count + digit;
			curr = "";
		}
		return prev;
	}

	@Test
	public void test() {
		assertTrue("Test1", countAndSay(1).compareTo("1") == 0);
		assertTrue("Test2", countAndSay(2).compareTo("11") == 0);
		assertTrue("Test3", countAndSay(3).compareTo("21") == 0);
		assertTrue("Test4", countAndSay(4).compareTo("1211") == 0);
		assertTrue("Test5", countAndSay(5).compareTo("111221") == 0);
	}

	public static void main(String[] args) {
		Result result = JUnitCore.runClasses(P038_CountAndSay.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}
}
