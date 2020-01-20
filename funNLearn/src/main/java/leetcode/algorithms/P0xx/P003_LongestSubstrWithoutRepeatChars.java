/**
 * Tag: string
 * 
 * Given a string, find the length of the longest substring without 
 * repeating characters. 
 * 
 * For example, the longest substring without repeating letters 
 * for "abcabcbb" is "abc", which the length is 3. 
 * For "bbbbb" the longest substring is "b", with the length of 1.
 */

package leetcode.algorithms.P0xx;

import static org.junit.Assert.assertEquals;

import java.util.HashMap;

public class P003_LongestSubstrWithoutRepeatChars {

	public static int lengthOfLongestSubstring(String s) {

		if (s == null || s.length() == 0)
			return 0;
		
		HashMap<Character, Integer> map = new HashMap<Character, Integer>();
		int maxLen = 0;
		
		for (int i = 0, currStrStartIndex = 0; i < s.length(); ++i) {
			// if duplicate char found
			if (map.containsKey(s.charAt(i))) {
				// keep the highest of 
				//  -  duplicate chars index
				//  -  currStrStartIndex which may be higher because of other char
				currStrStartIndex = Math.max(currStrStartIndex, map.get(s.charAt(i)) + 1);
			}
			
			map.put(s.charAt(i), i);
			
			// at each loop maxLength is the max of 
			//  -  curr maxLength
			//  -  currIndex minus currStrStartIndex and one
			maxLen = Math.max(maxLen, i - currStrStartIndex + 1);
		}
		return maxLen;
	}

	public static void main(String[] args) {
		assertEquals(3, lengthOfLongestSubstring("dvdf"));
		assertEquals(6, lengthOfLongestSubstring("vishal"));
		assertEquals(2, lengthOfLongestSubstring("aab"));
		assertEquals(3, lengthOfLongestSubstring("abcabcbb"));
		assertEquals(1, lengthOfLongestSubstring("c"));
		assertEquals(1, lengthOfLongestSubstring("bbbbbbbbb"));
		assertEquals(0, lengthOfLongestSubstring(""));
		assertEquals(0, lengthOfLongestSubstring(null));
		System.out.println("Tests Passed!");
	}
}
