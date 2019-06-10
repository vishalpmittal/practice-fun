/**
 * Tag: string
 *
 * Given a pattern and a string str, find if str follows the same pattern.
 * Here follow means a full match, such that there is a bijection between a 
 * letter in pattern and a non-empty word in str.
 * 
 * Examples:
 * pattern = "abba", str = "dog cat cat dog" should return true.
 * pattern = "abba", str = "dog cat cat fish" should return false.
 * pattern = "aaaa", str = "dog cat cat dog" should return false.
 * pattern = "abba", str = "dog dog dog dog" should return false.
 * 
 * Notes:
 * You may assume pattern contains only lowercase letters, and str 
 * contains lowercase letters separated by a single space.
 */

package leetcode.algorithms.P201_P300;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import java.util.HashMap;
import java.util.Map;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

public class P290_WordPattern {
	public static boolean wordPattern(String pattern, String str) {
		String[] words = str.split(" ");
		if (words.length != pattern.length())
			return false;
		Map index = new HashMap();
		for (Integer i = 0; i < words.length; ++i)
			// Hashmap.put returns the last value of that key if present or returns null
			if (index.put(pattern.charAt(i), i) != index.put(words[i], i))
				return false;
		return true;
	}

	@Test
	public void test() {
		assertTrue("Test1", wordPattern("abba", "dog cat cat dog"));
		assertFalse("Test2", wordPattern("abba", "dog cat cat fish"));
		assertFalse("Test3", wordPattern("aaaa", "dog cat cat dog"));
		assertFalse("Test4", wordPattern("abba", "dog dog dog dog"));
		assertTrue("Test5", wordPattern("aaaa", "dog dog dog dog"));
	}

	public static void main(String[] args) {
		Result result = JUnitCore.runClasses(P290_WordPattern.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}
}
