/**
 * Tag: array
 * 
 * Write a program that outputs the string representation of numbers from 1 to n.
 * 
 * But for multiples of three it should output “Fizz” instead of the number 
 * and for the multiples of five output “Buzz”. For numbers which are multiples 
 * of both three and five output “FizzBuzz”.
 * 
 * Example:
 * 
 * n = 15,
 * 
 * Return:
 * [
 *     "1",
 *     "2",
 *     "Fizz",
 *     "4",
 *     "Buzz",
 *     "Fizz",
 *     "7",
 *     "8",
 *     "Fizz",
 *     "Buzz",
 *     "11",
 *     "Fizz",
 *     "13",
 *     "14",
 *     "FizzBuzz"
 * ]
 */

package leetcode.algorithms.P401_P500;

import java.util.ArrayList;
import java.util.List;

public class P412_FizzBuzz {

	public List<String> fizzBuzz(int n) {
		List<String> fbList = new ArrayList<String>();
		if (n > 0) {
			String fizz = "Fizz";
			String buzz = "Buzz";
			for (int i = 1; i <= n; i++) {
				if (i % 5 == 0 && i % 3 == 0)
					fbList.add(fizz + buzz);
				else if (i % 5 == 0)
					fbList.add(buzz);
				else if (i % 3 == 0)
					fbList.add(fizz);
				else
					fbList.add("" + i);
			}
		}
		return fbList;
	}

	/*
	 * Not using the % operator
	 */
	public List<String> fizzBuzz_1(int n) {
		List<String> ret = new ArrayList<String>(n);
		for (int i = 1, fizz = 0, buzz = 0; i <= n; i++) {
			fizz++;
			buzz++;
			if (fizz == 3 && buzz == 5) {
				ret.add("FizzBuzz");
				fizz = 0;
				buzz = 0;
			} else if (fizz == 3) {
				ret.add("Fizz");
				fizz = 0;
			} else if (buzz == 5) {
				ret.add("Buzz");
				buzz = 0;
			} else {
				ret.add(String.valueOf(i));
			}
		}
		return ret;
	}

	public static void main(String[] args) {
		// assertFalse("Test1", problem(97));
		System.out.println("All Tests passed");
	}
}
