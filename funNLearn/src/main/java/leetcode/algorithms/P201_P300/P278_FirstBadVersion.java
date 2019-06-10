/**
 * Tag: array, math
 *
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

package leetcode.algorithms.P201_P300;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

class VersionControl {
	boolean isBadVersion(int version) {
		return true;
	}
}

public class P278_FirstBadVersion extends VersionControl {
	public int firstBadVersion(int n) {
		int lo = 1, hi = n;
		while (lo < hi) {
			int med = lo + (hi - lo) / 2;
			if (isBadVersion(med)) {
				hi = med;
			} else {
				lo = med + 1;
			}
		}
		return lo;
	}

	@Test
	public void test() {
	}

	public static void main(String[] args) {
		Result result = JUnitCore.runClasses(P278_FirstBadVersion.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}
}
