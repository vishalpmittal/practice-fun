/**
 * Tag: string, array
 *
 * Write a function that takes a string as input and reverse only the vowels of a string.
 * 
 * Example 1:
 * Given s = "hello", return "holle".
 * 
 * Example 2:
 * Given s = "leetcode", return "leotcede"
 * 
 */

package leetcode.algorithms.P3xx;

import static org.junit.Assert.assertTrue;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

public class P345_ReverseVowelsOfAString {
	// Iterative Solution, 20ms
	public static String reverseVowels_1(String s) {
		HashSet<Character> vowels = new HashSet<Character>(
				Arrays.asList('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'));

		char[] sa = s.toCharArray();
		int len = sa.length;

		List<Integer> vowLoc = new ArrayList<Integer>();

		// Capture all vowels location first
		for (int i = 0; i < len; i++)
			if (vowels.contains(sa[i]))
				vowLoc.add(i);

		// swap characters on those vowel locations
		int vowListSize = vowLoc.size();
		for (int i = 0; i < vowListSize / 2; i++) {
			char temp = sa[vowLoc.get(i)];
			sa[vowLoc.get(i)] = sa[vowLoc.get(vowListSize - 1 - i)];
			sa[vowLoc.get(vowListSize - 1 - i)] = temp;
		}

		return String.valueOf(sa);
	}

	// Two pointers solution, 14ms
	public static String reverseVowels_2(String s) {
		if (s == null || s.length() == 0)
			return s;

		HashSet<Character> vowels = new HashSet<Character>(
				Arrays.asList('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'));

		char[] sa = s.toCharArray();
		int start = 0;
		int end = s.length() - 1;

		while (start < end) {
			while (start < end && !vowels.contains(sa[start]))
				start++;

			while (start < end && !vowels.contains(sa[end]))
				end--;

			char temp = sa[start];
			sa[start] = sa[end];
			sa[end] = temp;

			start++;
			end--;
		}
		return new String(sa);
	}

	public static String reverseVowels(String s) {
		return reverseVowels_2(s);
	}

	@Test
	public void test() {
		assertTrue("Test1", reverseVowels("zzddxabacee").compareTo("zzddxebecaa") == 0);
		assertTrue("Test2", reverseVowels("hello").compareTo("holle") == 0);
		assertTrue("Test3", reverseVowels("leetcode").compareTo("leotcede") == 0);
		assertTrue("Test4", reverseVowels("aA").compareTo("Aa") == 0);
	}

	public static void main(String[] args) {
		Result result = JUnitCore.runClasses(P345_ReverseVowelsOfAString.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}
}
