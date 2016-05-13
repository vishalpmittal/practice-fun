/*
 * Given two strings s and t, determine if they are isomorphic.
 * 
 * Two strings are isomorphic if the characters in s can be replaced to get t.
 * All occurrences of a character must be replaced with another character 
 * while preserving the order of characters. No two characters may map to 
 * the same character but a character may map to itself.
 * 
 * For example:
 * Given "egg", "add", return true.
 * Given "foo", "bar", return false.
 * Given "paper", "title", return true.
 * 
 * Note:
 * You may assume both s and t have the same length.
 */

package leetcode;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

public class P205_IsomorphicStrings {
	/*
	 * The main idea is to store the last seen positions of current (i-th) 
	 * characters in both strings. If previously stored positions are different 
	 * then we know that the fact they're occuring in the current i-th position 
	 * simultaneously is a mistake. We could use a map for storing but as we deal 
	 * with chars which are basically ints and can be used as indices we can do
	 * the whole thing with an array.
	 */
	public boolean isIsomorphic_1(String s, String t) {
		int[] m = new int[512];
		for (int i = 0; i < s.length(); i++) {
			if (m[s.charAt(i)] != m[t.charAt(i) + 256])
				return false;
			m[s.charAt(i)] = m[t.charAt(i) + 256] = i + 1;
		}
		return true;
	}

	public boolean isIsomorphic(String s, String t) {
		return isIsomorphic_1(s, t);
	}

	@Test
	public void test() {
		assertTrue("Test1", isIsomorphic("egg", "add"));
		assertFalse("Test2", isIsomorphic("foo", "bar"));
		assertTrue("Test1", isIsomorphic("paper", "title"));
		assertFalse("Test2", isIsomorphic("aba", "baa"));
		assertFalse("Test2", isIsomorphic("aa", "ab"));
	}

	public static void main(String[] args) {
		Result result = JUnitCore.runClasses(P205_IsomorphicStrings.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}
}
