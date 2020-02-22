/**
 * Tag: array, integer
 * 
 * Given a non-negative number represented as an array of digits, plus one to the number.
 * The digits are stored such that the most significant digit is at the head of the list.
 */
package dsAlgo.leetcode.P0xx;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import java.util.Arrays;

public class P066_PlusOne {
	public static int[] plusOne_1(int[] digits) {
		int len = digits.length;
		for (int i = len - 1; i >= 0; i--) {
			if (digits[i] != 9) {
				digits[i]++;
				return digits;
			}
			digits[i] = 0;
		}
		int[] newNumber = new int[len + 1];
		newNumber[0] = 1;

		return newNumber;
	}

	@Test
	public void test() {
		int[] digits = { 1, 2, 3, 9 };
		int[] digits1 = { 9, 9, 9, 9 };
		System.out.println(Arrays.toString(plusOne_1(digits)));
		System.out.println(Arrays.toString(plusOne_1(digits1)));
	}

	public static void main(String[] args) {
		Result result = JUnitCore.runClasses(P066_PlusOne.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}
}
