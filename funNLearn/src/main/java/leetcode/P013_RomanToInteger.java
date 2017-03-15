/*
 * Given a roman numeral, convert it to an integer.
 * 
 * Input is guaranteed to be within the range from 1 to 3999.
 * 
 * I -> 1
 * V -> 5
 * X -> 10
 * L -> 50
 * C -> 100
 * D -> 500
 * M -> 1000
 */

package leetcode;

import java.util.HashMap;

public class P013_RomanToInteger {

	public static int romanToInt(String s) {
		HashMap<Character, Integer> romanTable = new HashMap<Character, Integer>();
		romanTable.put('I', 1);
		romanTable.put('V', 5);
		romanTable.put('X', 10);
		romanTable.put('L', 50);
		romanTable.put('C', 100);
		romanTable.put('D', 500);
		romanTable.put('M', 1000);

		int num = 0;
		for (int i = 0; i < s.length(); i++) {
			if (i < (s.length() - 1) && romanTable.get(s.charAt(i)) < romanTable.get(s.charAt(i + 1))) {
				num += (romanTable.get(s.charAt(i + 1)) - romanTable.get(s.charAt(i)));
				i++;
			} else {
				num += romanTable.get(s.charAt(i));
			}
		}
		return num;
	}

	public static void main(String[] args) {
		System.out.println("" + romanToInt("D"));
	}

}
