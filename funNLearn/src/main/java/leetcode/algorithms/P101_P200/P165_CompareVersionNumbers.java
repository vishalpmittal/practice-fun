/**
 * Tag: math, array
 *
 * Compare two version numbers version1 and version2.
 * If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.
 * 
 * You may assume that the version strings are non-empty and contain only digits and the . character.
 * The . character does not represent a decimal point and is used to separate number sequences.
 * 
 * For instance, 2.5 is not "two and a half" or "half way to version three", 
 * it is the fifth second-level revision of the second first-level revision.
 * 
 * Here is an example of version numbers ordering:
 * 0.1 < 1.1 < 1.2 < 13.37
 */

package leetcode.algorithms.P101_P200;

import static org.junit.Assert.assertTrue;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

public class P165_CompareVersionNumbers {
	public static int compareVersion_0(String version1, String version2) {
		String[] v1 = version1.split("\\.");
		String[] v2 = version2.split("\\.");

		int i = 0;
		while (i < v1.length && i < v2.length) {
			int pv1 = Integer.parseInt(v1[i]);
			int pv2 = Integer.parseInt(v2[i]);
			if (pv1 > pv2)
				return 1;
			else if (pv2 > pv1)
				return -1;
			i++;
		}

		while (i < v1.length) {
			if (Integer.parseInt(v1[i]) != 0)
				return 1;
			i++;
		}

		while (i < v2.length) {
			if (Integer.parseInt(v2[i]) != 0)
				return -1;
			i++;
		}

		return 0;
	}

	public static int compareVersion_1(String version1, String version2) {
		String[] v1 = version1.split("\\.");
		String[] v2 = version2.split("\\.");

		for (int i = 0; i < Math.max(v1.length, v2.length); i++) {
			int num1 = i < v1.length ? Integer.parseInt(v1[i]) : 0;
			int num2 = i < v2.length ? Integer.parseInt(v2[i]) : 0;
			if (num1 < num2) {
				return -1;
			} else if (num1 > num2) {
				return +1;
			}
		}
		return 0;
	}

	public static int compareVersion(String version1, String version2) {
		return compareVersion_0(version1, version2);
	}

	@Test
	public void test() {
		assertTrue("Test1", compareVersion("1.2", "1.3") == -1);
		assertTrue("Test2", compareVersion("1.3", "1.1") == 1);
		assertTrue("Test3", compareVersion("1.1.4", "1.1.4") == 0);
		assertTrue("Test4", compareVersion("1.1.4", "1.1") == 1);
		assertTrue("Test5", compareVersion("1.0.4", "1") == 1);
		assertTrue("Test6", compareVersion("1.0", "1") == 0);
	}

	public static void main(String[] args) {
		Result result = JUnitCore.runClasses(P165_CompareVersionNumbers.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}
}
