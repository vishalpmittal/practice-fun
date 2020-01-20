/**
* Tag: string, array
*
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

package leetcode.algorithms.P0xx;

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
	* The distribution of the elements is period.
	* 
	* P   A   H   N
	* A P L S I I G
	* Y   I   R
	* For example, the following has 4 periods(cycles):
	* 
	* P   | A   | H   | N
	* A P | L S | I I | G
	* Y   | I   | R   |
	* The size of every period is defined as "cycle"
	* 
	* cycle = (2*nRows - 2), except nRows == 1.
	* In this example, (2*nRows - 2) = 4.
	* 
	* In every period, every row has 2 elements, except the first row and the last row.
	* 
	* Suppose the current row is i, the index of the first element is j:
	* 
	* j = i + cycle*k, k = 0, 1, 2, ...
	* The index of the second element is secondJ:
	* 
	* secondJ = (j - i) + cycle - i
	* (j-i) is the start of current period, (j-i) + cycle is the start of next period.
	*/
	public static String convert_2(String s, int numRows) {
		if (numRows <= 1)
			return s;
		String result = "";

		//the size of a cycle(period)
		int cycle = 2 * numRows - 2;
		for (int i = 0; i < numRows; ++i) {
			for (int j = i; j < s.length(); j = j + cycle) {
				result = result + s.charAt(j);
				int secondJ = (j - i) + cycle - i;
				if (i != 0 && i != numRows - 1 && secondJ < s.length())
					result = result + s.charAt(secondJ);
			}
		}
		return result;
	}

	public static String convert(String s, int numRows) {
		return convert_2(s, numRows);
	}

	@Test
	public void test() {
		assertTrue("Test1", convert("PAYPALISHIRING", 3).compareTo("PAHNAPLSIIGYIR") == 0);
		assertTrue("Test2", convert("ABC", 4).compareTo("ABC") == 0);
	}

	public static void main(String[] args) {
		Result result = JUnitCore.runClasses(P006_ZigZagConversion.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}
}
