/**
 *  Tag: math
 *
 * Related to question P171_ExcelSheetColumnNumber
 * 
 * Given a positive integer, return its corresponding column title as appear in an Excel sheet.
 * 
 * For example:
 * 1 -> A
 * 2 -> B
 * 3 -> C
 * ...
 * 26 -> Z
 * 27 -> AA
 * 28 -> AB 
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

public class P168_ExcelSheetColumnTitle {

	public static String convertToTitle_0(int n) {
		StringBuilder sb = new StringBuilder("");
		while (n > 0) {
			int rem = n % 26;
			n = n / 26;
			if (rem == 0) {
				sb.insert(0, 'Z');
				n = n - 1;
			} else {
				sb.insert(0, (char) ('A' - 1 + rem));
			}
		}
		return sb.toString();
	}

	public static String convertToTitle_1(int n) {
		return n == 0 ? "" : convertToTitle_1(--n / 26) + (char) ('A' + (n % 26));
	}

	public static String convertToTitle_2(int n) {
		StringBuilder result = new StringBuilder();
		while (n > 0) {
			n--;
			result.insert(0, (char) ('A' + n % 26));
			n /= 26;
		}
		return result.toString();
	}

	public static String convertToTitle(int n) {
		return convertToTitle_1(n);
	}

	public static void main(String[] args) {
		System.out.println("" + convertToTitle(25)); //Y
		System.out.println("" + convertToTitle(26)); //Z
		System.out.println("" + convertToTitle(27)); //AA
		System.out.println("" + convertToTitle(28)); //AB
		System.out.println("" + convertToTitle(52)); //AZ
	}

}
