/*
 * 
 */

package leetcode;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;

public class Template {
	/*
	 * 
	 */
	public static boolean problem_1(int n) {
		return false;
	}

	/*
	 * 
	 */
	public static boolean problem_2(int n) {
		return false;
	}

	public static boolean problem(int n) {
		return problem_1(n);
	}

	@Test
	public void test() {
		assertTrue("Test1", problem(94));
		assertFalse("Test2", problem(97));
	}

	public static void main(String[] args) {
		Result result = JUnitCore.runClasses(Template.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}

}
