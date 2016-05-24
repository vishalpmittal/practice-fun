/*
 * You are a product manager and currently leading a team to develop a new product. 
 * Unfortunately, the latest version of your product fails the quality check. 
 * Since each version is developed based on the previous version, all the versions 
 * after a bad version are also bad.
 * 
 * Suppose you have n versions [1, 2, ..., n] and you want to find out the first 
 * bad one, which causes all the following ones to be bad.
 * 
 * You are given an API bool isBadVersion(version) which will return whether version 
 * is bad. Implement a function to find the first bad version. You should minimize 
 * the number of calls to the API.
 */

package leetcode;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;

public class P278_FirstBadVersion {
    public int firstBadVersion(int n) {
    	
    	
    	
    	
    	return 0;
    }
	
	public static boolean problem_1(int n) {
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
		Result result = JUnitCore.runClasses(P278_FirstBadVersion.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}
}
