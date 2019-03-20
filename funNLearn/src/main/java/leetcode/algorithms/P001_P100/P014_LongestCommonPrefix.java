/**
 * Tag: string
 * 
 * Write a function to find the longest common prefix string amongst an array of strings.
 * 
 * Example 1:
 * Input: ["flower","flow","flight"]
 * Output: "fl"
 * 
 * Example 2:
 * Input: ["dog","racecar","car"]
 * Output: ""
 * Explanation: There is no common prefix among the input strings.
 * 
 */

package leetcode.algorithms.P001_P100;

import static org.junit.Assert.assertTrue;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

public class P014_LongestCommonPrefix {
	public static String longestCommonPrefix_1(String[] strs) {
		if (strs == null || strs.length == 0)
			return "";

		String prefix = strs[0];
		for (int i = 0; i < strs.length; i++) {
			StringBuilder sb = new StringBuilder("");
			for (int j = 0; j < prefix.length() && j < strs[i].length(); j++) {
				if (prefix.charAt(j) == strs[i].charAt(j))
					sb.append(prefix.charAt(j));
				else
					break;
			}
			prefix = sb.toString();
		}
		return prefix;
	}

	public static String longestCommonPrefix_2(String[] strs) {
		if (strs == null || strs.length == 0)
			return "";
		String pre = strs[0];
		int i = 1;
		while (i < strs.length) {
			// Keep removing one char from pre everytime it is not found in strs[i]
			while (strs[i].indexOf(pre) != 0)
				pre = pre.substring(0, pre.length() - 1);
			i++;
		}
		return pre;
	}

	public static String longestCommonPrefix(String[] strs) {
		return longestCommonPrefix_1(strs);
	}

	@Test
	public void test() {
		assertTrue("Test1", longestCommonPrefix(new String[] { "abcdef", "abce", "abbbba" }).compareTo("ab") == 0);
	}

	public static void main(String[] args) {
		Result result = JUnitCore.runClasses(P014_LongestCommonPrefix.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}
}
