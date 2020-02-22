/**
 * Tag: math 
 *
 * Related to question Excel Sheet Column Title (P168_ExcelSheetColumnTitle)
 * 
 * Given a column title as appear in an Excel sheet, return its corresponding column number.
 * 
 * For example:
 *  A -> 1
 *  B -> 2
 *  C -> 3
 *  ...
 *  Z -> 26
 *  AA -> 27
 *  AB -> 28
 *     
 *   This is similar to how we generate decimal numbers
 *   like 256 can be generated as 
 *   2 = 0*10 +2
 *   25 = 2*10 + 5
 *   256 = 25 * 10 + 6
 *   
 *   here the base is 26 instead of 10, that is it
 */

package dsAlgo.leetcode.P1xx;

public class P171_ExcelSheetColumnNumber {

	public static int titleToNumber(String s) {
		int colNum = 0;
		for (int i = 0; i < s.length(); colNum = colNum * 26 + (s.charAt(i) - 'A' + 1), i++) {
		}
		return colNum;
	}

	public static void main(String[] args) {
		System.out.println("" + titleToNumber("DF")); //110
	}

}
