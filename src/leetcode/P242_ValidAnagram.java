/*
 * Given two strings s and t, write a function to determine if t is an anagram of s.
 * 
 * For example,
 * s = "anagram", t = "nagaram", return true.
 * s = "rat", t = "car", return false.
 * 
 * Note:
 * You may assume the string contains only lowercase alphabets.
 * 
 * Follow up:
 * What if the inputs contain unicode characters? 
 * How would you adapt your solution to such case?
 * 
 */

package leetcode;

import java.util.HashMap;

public class P242_ValidAnagram {

	public static boolean isAnagram(String s, String t) {
		HashMap<Character, Integer> counter = new HashMap<Character, Integer>();

		if (s == null || t == null || (s.length() != t.length()))
			return false;

		for (Character c : s.toCharArray()) {
			int temp = counter.containsKey(c) ? counter.get(c) + 1 : 1;
			counter.put(c, temp);
		}

		for (Character c : t.toCharArray()) {
			if (!counter.containsKey(c))
				return false;
			counter.put(c, counter.get(c) - 1);
		}

		for (Character c : counter.keySet()) {
			if (counter.get(c) != 0) {
				return false;
			}
		}

		return true;
	}

	public static boolean isAnagram_2(String s, String t) {
		HashMap<Character, Integer> counter = new HashMap<Character, Integer>();

		if (s == null || t == null || (s.length() != t.length()))
			return false;

		for (int i = 0; i < s.toCharArray().length; i++) {
			Character cs = s.charAt(i);
			Character ct = t.charAt(i);
			if (cs == ct)
				continue;

			int temps = counter.containsKey(cs) ? counter.get(cs) + 1 : 1;
			int tempt = counter.containsKey(ct) ? counter.get(ct) - 1 : -1;

			counter.put(cs, temps);
			counter.put(ct, tempt);
		}

		for (Character c : counter.keySet()) {
			if (counter.get(c) != 0) {
				return false;
			}
		}

		return true;
	}

	public static void main(String[] args) {
		System.out.println(isAnagram("anagram", "nagaram"));
		System.out.println(isAnagram("vishal", "asdfl"));
		System.out.println(isAnagram("vishal", "visham"));
	}

}
