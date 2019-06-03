/**
 * Tag: palindrome, array
 * 
 * Given a string, determine if it is a palindrome, considering only 
 * alphanumeric characters and ignoring cases.
 * 
 * For example,
 * "A man, a plan, a canal: Panama" is a palindrome.
 * "race a car" is not a palindrome.
 * 
 * Note:
 * Have you consider that the string might be empty? 
 * This is a good question to ask during an interview.
 * 
 * For the purpose of this problem, we define empty string as valid palindrome.
 */

package leetcode.algorithms.P101_P200;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;

public class P125_ValidPalindrome {
	public static boolean isPalindrome(String s) {
		if (s == null)
			return false;

		int len = s.length();
		if (len < 2)
			return true;

		int fw = 0;
		int bw = len - 1;
		while (fw <= bw) {
			while (fw < len && !isValidChar(s.charAt(fw))) {
				fw++;
			}
			while (bw >= 0 && !isValidChar(s.charAt(bw))) {
				bw--;
			}
			if (fw < len && bw > 0)
				if (Character.toLowerCase(s.charAt(fw)) != Character.toLowerCase(s.charAt(bw)))
					return false;
			fw++;
			bw--;
		}
		return true;
	}

	public static boolean isValidChar(Character c) {
		return Character.isAlphabetic(c) || Character.isDigit(c);
	}

	@Test
	public void test() {
		assertTrue("Test1", isPalindrome("A man, a plan, a canal: Panama"));
		assertFalse("Test2", isPalindrome("race a car"));
		assertTrue("Test3", isPalindrome(".,"));
	}

	public static void main(String[] args) {
		Result result = JUnitCore.runClasses(P125_ValidPalindrome.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}
}
