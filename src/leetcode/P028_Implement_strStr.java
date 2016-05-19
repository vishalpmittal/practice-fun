/*
 * Implement strStr().
 * 
 * Returns the index of the first occurrence of needle in haystack, 
 * or -1 if needle is not part of haystack.
 */

package leetcode;

import static org.junit.Assert.assertTrue;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

public class P028_Implement_strStr {

	public int strStr(String haystack, String needle) {
		if (haystack == null || needle == null)
			return -1;

		int hp = 0, np = 0, fo = -1, hl = haystack.length(), nl = needle.length();
		if (nl > hl)
			return -1;

		if (nl == 0)
			return 0;

		while (np < nl && hp < hl) {
			if (haystack.charAt(hp) == needle.charAt(np)) {
				fo = fo == -1 ? hp : fo;
				np++;
				hp++;
			} else {
				np = 0;
				hp = fo == -1 ? hp + 1 : fo + 1;
				fo = -1;
			}
		}
		return np == nl ? fo : -1;
	}

	@Test
	public void test() {
		assertTrue("Test1", strStr("", "") == 0);
		assertTrue("Test1", strStr("vishalaab", "shal") == 2);
		assertTrue("Test2", strStr("vishalaab", "blah") == -1);
		assertTrue("Test2", strStr("mississippi", "issip") == 4);
	}

	public static void main(String[] args) {
		Result result = JUnitCore.runClasses(P028_Implement_strStr.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}
}
