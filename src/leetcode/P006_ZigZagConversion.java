/*
* The string "PAYPALISHIRING" is written in a zigzag pattern on a given number 
* of rows like this: (you may want to display this pattern in a fixed font 
* for better legibility)
* 
* P   A   H   N
* A P L S I I G
* Y   I   R
* 
* And then read line by line: "PAHNAPLSIIGYIR"
* Write the code that will take a string and make this conversion given a number of rows:
* 
* string convert(string text, int nRows);
* 
* convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
*/

package leetcode;

import static org.junit.Assert.assertTrue;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

public class P006_ZigZagConversion {
	public static String convert_1(String s, int numRows) {
		if (s == null || s.length() == 0 || numRows < 2)
			return s;

		StringBuilder[] sb = new StringBuilder[numRows];
		int c = 0;
		int sbNum = 0;
		boolean up = true;
		while (c < s.length()) {
			sb[sbNum] = sb[sbNum] == null ? new StringBuilder("") : sb[sbNum];
			sb[sbNum].append(s.charAt(c));
			c++;
			sbNum = up ? sbNum + 1 : sbNum - 1;
			if (sbNum == numRows - 1)
				up = false;
			else if (sbNum == 0)
				up = true;
		}

		for (int i = 1; i < sb.length; i++)
			if (sb[i] != null)
				sb[0].append(sb[i].toString());

		return sb[0].toString();
	}

	/*
	 * 
	 */
	public static String convert_2(String s, int numRows) {
		if (s == null || s.length() == 0 || numRows < 2)
			return s;

		int len = s.length();
		StringBuilder sb = new StringBuilder("");

		int idx = 0;
		while (idx < len && idx < (2 * numRows) - 2) {
			int iter = idx;
			while (iter < len) {
				sb.append(s.charAt(iter));
				iter = iter + ((2 * numRows) - 2);
			}
			idx++;
		}
		return sb.toString();
	}

	public static String convert(String s, int numRows) {
		return convert_2(s, numRows);
	}

	@Test
	public void test() {
		//		assertTrue("Test1", convert("PAYPALISHIRING", 3).compareTo("PAHNAPLSIIGYIR") == 0);
		//		assertTrue("Test2", convert("ABC", 4).compareTo("ABC") == 0);
	}

	public static void main(String[] args) {
		System.out.println(convert("PAYPALISHIRING", 3));
		System.out.println(convert("ABC", 3));
		//		Result result = JUnitCore.runClasses(P006_ZigZagConversion.class);
		//		System.out.println("All Tests passed : " + result.wasSuccessful());
		//		for (Failure failure : result.getFailures()) {
		//			System.out.println("Failed Test cases" + failure.toString());
		//		}
	}
}
