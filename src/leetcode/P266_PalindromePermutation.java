/**
 * Given a string, determine if a permutation of the string could form a palindrome.
 * 
 * For example,
 * "code" -> False, "aab" -> True, "carerac" -> True.
 * 
 * Hint:
 * -  Consider the palindromes of odd vs even length. What difference do you notice?
 * -  Count the frequency of each character.
 * -  If each character occurs even number of times, then it must be a palindrome. 
 * 	  How about character which occurs odd number of times?
 */

package leetcode;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import java.util.HashSet;
import java.util.Set;

public class P266_PalindromePermutation {

	public static boolean canPermutePalindrome(String s) {
		Set<Character> set = new HashSet<Character>();
		for (int i = 0; i < s.length(); ++i) {
			if (!set.contains(s.charAt(i)))
				set.add(s.charAt(i));
			else
				set.remove(s.charAt(i));
		}
		return set.size() == 0 || set.size() == 1;
	}

	public static void main(String[] args) {
		assertTrue("Test1", canPermutePalindrome("aba"));
		assertTrue("Test1", canPermutePalindrome("carerac"));
		assertFalse("Test2", canPermutePalindrome("code"));
		System.out.println("All Tests passed");
	}
}
