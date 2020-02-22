/**
 * Tag: math, algo, Floyd Cycle Detection Algorithm
 *
 * Write an algorithm to determine if a number is "happy".
 * A happy number is a number defined by the following process: 
 * Starting with any positive integer, replace the number by the sum of 
 * the squares of its digits, and repeat the process until the number 
 * equals 1 (where it will stay), or it loops endlessly in a cycle which 
 * does not include 1. Those numbers for which this process 
 * ends in 1 are happy numbers.
 * 
 * Example: 19 is a happy number
 * 1^2 + 9^2 = 82
 * 8^2 + 2^2 = 68
 * 6^2 + 8^2 = 100
 * 1^2 + 0^2 + 0^2 = 1
 * 
 */

package dsAlgo.leetcode.P2xx;

import java.util.HashSet;
import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

public class P202_HappyNumber {

	/*
	 * O(n) Space.
	 */
	public static boolean isHappy_1(int n) {
		HashSet<Integer> repos = new HashSet<Integer>();
		while (n != 1 && repos.add(n)) {
			int temp = n;
			n = 0;
			while (temp > 0) {
				n += (temp % 10) * (temp % 10);
				temp /= 10;
			}
		}
		if (n == 1)
			return true;
		return false;
	}

	/*
	 * O(1) Space Using Floyd Cycle Detection Algorithm like the one in linked list
	 * colliding problem
	 */
	public static int digitSquareSum(int n) {
		int sum = 0;
		while (n > 0) {
			sum += (int) Math.pow(n % 10, 2);
			n /= 10;
		}
		return sum;
	}

	public static boolean isHappy_2(int n) {
		int slow = n, fast = n;
		do {
			slow = digitSquareSum(slow);
			fast = digitSquareSum(fast);
			fast = digitSquareSum(fast);
		} while (slow != fast);
		if (slow == 1)
			return true;
		else
			return false;
	}

	public static boolean isHappy(int n) {
		return isHappy_1(n);
	}

	@Test
	public void test() {
		assertTrue("Test1", isHappy(94));
		assertTrue("Test2", isHappy(97));
		assertFalse("Test3", isHappy(101));
		assertTrue("Test4", isHappy(103));
		assertTrue("Test5", isHappy(109));
		assertTrue("Test6", isHappy(622));
		assertTrue("Test7", isHappy(623));
		assertTrue("Test8", isHappy(899));
		assertTrue("Test9", isHappy(901));
		assertTrue("Test10", isHappy(989));
		assertTrue("Test11", isHappy(998));
		assertTrue("Test12", isHappy(1000));
	}

	public static void main(String[] args) {
		Result result = JUnitCore.runClasses(P202_HappyNumber.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}
}
