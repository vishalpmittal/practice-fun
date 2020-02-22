/*
 * Given two binary strings, return their sum (also a binary string).
 * 
 * For example,
 * a = "11"
 * b = "1"
 * Return "100".
 */

package dsAlgo.leetcode.P0xx;

import static org.junit.Assert.assertTrue;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

public class P067_AddBinary {
	public static String addBinary_1(String a, String b) {
		if (a == null && b == null)
			return null;

		int lena = a.length();
		int lenb = b.length();

		if (lena == 0 || lenb == 0)
			return lena > lenb ? a : b;

		int i = lena - 1;
		int j = lenb - 1;
		int carryOver = 0;
		StringBuilder sum = new StringBuilder("");
		while (i >= 0 || j >= 0) {
			int temp = carryOver;
			if (i >= 0)
				temp += Character.getNumericValue(a.charAt(i));
			if (j >= 0)
				temp += Character.getNumericValue(b.charAt(j));
			sum.insert(0, (temp % 2));
			if (temp > 1)
				carryOver = 1;
			else
				carryOver = 0;
			i--;
			j--;
		}
		if (carryOver == 1)
			sum.insert(0, 1);

		return sum.toString();
	}

	public static String addBinary(String a, String b) {
		return addBinary_1(a, b);
	}

	@Test
	public void test() {
		assertTrue("Test1", addBinary("11", "1").compareTo("100") == 0);
	}

	public static void main(String[] args) {
		Result result = JUnitCore.runClasses(P067_AddBinary.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}
}
