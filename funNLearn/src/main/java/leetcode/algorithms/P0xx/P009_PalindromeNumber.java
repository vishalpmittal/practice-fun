/**
 * Tag: math
 * 
 * Determine whether an integer is a palindrome. 
 * Do this without extra space.
 * 
 * Some hints:
 * Could negative integers be palindromes? (ie, -1)
 * If you are thinking of converting the integer to string, 
 * note the restriction of using extra space.
 * 
 * You could also try reversing an integer. 
 * However, if you have solved the problem "Reverse Integer", you know that the 
 * reversed integer might overflow. How would you handle such case?
 * 
 * There is a more generic way of solving this problem.
 */

package leetcode.algorithms.P0xx;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;

public class P009_PalindromeNumber {
	
	// Idea is to create a reverse number from second half of the 
	// original number. then compare them at the end. 
	public static boolean isPalindrome_1(int x) {
		if (x < 0 || (x != 0 && x % 10 == 0))
			return false;
		int rev = 0;
		while (x > rev) {
			rev = rev * 10 + x % 10;
			x = x / 10;
		}
		return (x == rev || x == rev / 10);
	}

	public static boolean isPalindrome(int n) {
		return isPalindrome_1(n);
	}

	@Test
	public void test() {
		assertTrue("Test1", isPalindrome(1234321));
		assertFalse("Test2", isPalindrome(3215));
	}

	public static void main(String[] args) {
		Result result = JUnitCore.runClasses(P009_PalindromeNumber.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}
}
