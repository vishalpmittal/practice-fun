/**
* Tag: string, integer
* 
* Reverse digits of an integer.
* 
* Example1: x = 123, return 321
* Example2: x = -123, return -321
* 
* If the integer's last digit is 0, what should the output be? 
* ie, cases such as 10, 100.
* 
* Did you notice that the reversed integer might overflow? 
* Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. 
* How should you handle such cases?
* 
* For the purpose of this problem, assume that your function returns 0 
* when the reversed integer overflows.
*/

package leetcode.algorithms.P0xx;

import static org.junit.Assert.assertTrue;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

public class P007_ReverseInteger {
	public static int reverse_1(int x) {
		int ret = 0;

		while (x != 0) {
			int tail = x % 10;
			int temp = ret * 10 + tail;
			if ((temp - tail) / 10 != ret)
				return 0;

			ret = temp;
			x = x / 10;
		}
		return ret;
	}

	public static int reverse(int n) {
		return reverse_1(n);
	}

	@Test
	public void test() {
		assertTrue("Test1", reverse(123) == 321);
		assertTrue("Test2", reverse(-1234) == -4321);
		assertTrue("Test3", reverse(100) == 1);
		assertTrue("Test3", reverse(1534236469) == 0);
	}

	public static void main(String[] args) {
		Result result = JUnitCore.runClasses(P007_ReverseInteger.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}
}
